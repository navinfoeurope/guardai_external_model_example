#  Copyright (C) 2022 by NavInfo Europe B.V. The Netherlands - All rights reserved
#  Information classification: Confidential
#  This content is protected by international copyright laws.
#  Reproduction and distribution is prohibited without written permission.

"""Demo handler for ONNX models and a COCO dataset."""

__author__ = "Kobus Grobler"

import base64
import io
import json
import os
from typing import Tuple, Any

import numpy as np
import onnxruntime as ort
import torchvision

from external_server.models import DatasetItem, DatasetStructureFeaturesInner
from external_server.models.dataset_structure import DatasetStructure
from external_server.models.model_structure import ModelStructure
from external_server.models.model_structure_inputs_inner import ModelStructureInputsInner

# this should point to the root of the dataset - coco 2017 in this case
DS_ROOT = "data"
MODE_PATH = "ssd-12.onnx"

_ort_session = None
_inputs = None
_outputs = None
_ds = None


class CocoDetection(torchvision.datasets.CocoDetection):
    """
    Wrapper around dataset to return file path for the image instead of the loaded image.
    """
    def __init__(
        self,
        root: str,
        annFile: str,
    ):
        super().__init__(root, annFile)
        self.ids = list(self.coco.imgToAnns.keys())

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        id = self.ids[index]
        path = self.coco.loadImgs(id)[0]["file_name"]
        img = os.path.join(self.root, path)
        with open(img, "rb") as f:
            data = f.read()
        target = self.coco.loadAnns(self.coco.getAnnIds(id))
        return data, target


def _lazy_load_model():
    global _ort_session, _inputs, _outputs
    if _ort_session is None:
        # model from https://github.com/onnx/models/blob/main/vision/object_detection_segmentation/ssd/model/ssd-12.onnx
        _ort_session = ort.InferenceSession(MODE_PATH, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])
        _outputs = _ort_session.get_outputs()
        _inputs = _ort_session.get_inputs()


def _lazy_load_ds():
    global _ds
    if _ds is None:
        _ds = CocoDetection(DS_ROOT + "/val2017", DS_ROOT + "/annotations/instances_val2017.json")


def handle_predict(file_storage) -> bytes:
    _lazy_load_model()
    # file_storage stream is not seekable, first copy to buffer
    with file_storage.stream as f:
        byte_arr = io.BytesIO()
        byte_arr.write(f.read())
        byte_arr.seek(0)
        with np.load(byte_arr) as npz:
            inp = {k: np.expand_dims(npz[k], axis=0) for k in npz.files}
            pred = _ort_session.run(None, inp)
            out = {o.name: value for o, value in zip(_outputs, pred)}
            byte_arr = io.BytesIO()
            np.savez_compressed(byte_arr, **out)
            byte_arr.name = "data.npz"
            byte_arr.seek(0)
            return byte_arr.getvalue()


def handle_structure() -> ModelStructure:
    _lazy_load_model()
    return ModelStructure(
        [ModelStructureInputsInner(i.name, i.shape) for i in _inputs],
        [ModelStructureInputsInner(o.name, o.shape) for o in _outputs],
    )


def handle_dataset_structure() -> DatasetStructure:
    _lazy_load_ds()
    return DatasetStructure(
        len(_ds),
        [
            DatasetStructureFeaturesInner("image", type="image/jpeg"),
            DatasetStructureFeaturesInner("target", type="application/json"),
        ],
    )


def get_dataset_item(index: int) -> DatasetItem:
    _lazy_load_ds()
    image, target = _ds[index]
    features = {
        "image": base64.b64encode(image).decode("ascii"),
        "target": base64.b64encode(bytes(json.dumps(target), "ascii")).decode("ascii"),
    }
    return DatasetItem(features)
