import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from external_server.models.dataset_structure import DatasetStructure  # noqa: E501
from external_server import util
from external_server.implementation.handlers import handle_dataset_structure
from external_server.implementation.handlers import get_dataset_item


def dataset_structure():  # noqa: E501
    """Get the dataset output structure

    Get the dataset output structure # noqa: E501


    :rtype: Union[DatasetStructure, Tuple[DatasetStructure, int], Tuple[DatasetStructure, int, Dict[str, str]]
    """
    return handle_dataset_structure()


def get_item(item_idx):  # noqa: E501
    """Get a dataset item

     # noqa: E501

    :param item_idx: Dataset item index
    :type item_idx: int

    :rtype: Union[DatasetItem, Tuple[DatasetItem, int], Tuple[DatasetItem, int, Dict[str, str]]
    """
    return get_dataset_item(item_idx)
