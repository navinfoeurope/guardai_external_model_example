import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from external_server.models.model_structure import ModelStructure  # noqa: E501
from external_server import util

from external_server.implementation.handlers import handle_predict, handle_structure


def predict(data=None):  # noqa: E501
    """Perform prediction on a model

    Perform prediction on a model # noqa: E501

    :param data:
    :type data: str

    :rtype: Union[file, Tuple[file, int], Tuple[file, int, Dict[str, str]]
    """
    return handle_predict(data)


def structure():  # noqa: E501
    """Get model input and output structures

    Get model input and output structures # noqa: E501


    :rtype: Union[ModelStructure, Tuple[ModelStructure, int], Tuple[ModelStructure, int, Dict[str, str]]
    """
    return handle_structure()
