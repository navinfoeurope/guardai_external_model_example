#  Copyright (C) 2022 by NavInfo Europe B.V. The Netherlands - All rights reserved
#  Information classification: Confidential
#  This content is protected by international copyright laws.
#  Reproduction and distribution is prohibited without written permission.

"""Demo model handler for ONNX models."""

__author__ = "Kobus Grobler"

import io

import numpy as np
import onnxruntime as ort

from external_server.models.model_structure import ModelStructure
from external_server.models.model_structure_inputs_inner import ModelStructureInputsInner

# model from https://github.com/onnx/models/blob/main/vision/object_detection_segmentation/ssd/model/ssd-12.onnx
_path_to_model = "ssd-12.onnx"

_ort_session = ort.InferenceSession(_path_to_model, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])

_outputs = _ort_session.get_outputs()
_inputs = _ort_session.get_inputs()


def handle_predict(file_storage):
    with file_storage.stream as f:
        # file_storage stream is not seekable, so first copy to buf
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


def handle_structure():
    return ModelStructure(
        [ModelStructureInputsInner(i.name, i.shape) for i in _inputs],
        [ModelStructureInputsInner(o.name, o.shape) for o in _outputs],
    )
