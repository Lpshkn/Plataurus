"""
This module contains auxiliary functions to work with different variables of database, system or other important
parts of the project.
"""
import os
from plataurus.logger import get_logger

logger = get_logger(__name__)


def get_env_value(key: str, default=None):
    """
    Get a variable from the environment. Function is similar to os.getenv function except was added the printing
    a message if the default value was used. It helps for tracking unexpected errors when the default value
    should not have been used or when the variable is None.
    Parameters
    ----------
    key : string
        The name of a variable that should be get from the environment.

    default : any
        A default value that will be returned if the variable wasn't get from the environment.

    Return
    ------
    variable : any
        Whether a variable from the environment or the default value, or None.
    """
    if (value := os.getenv(key)) is None:
        if default is not None:
            value = default
            logger.info(f'For the key "{key}" will be used the default value: "{value}"')
        else:
            value = None
            logger.warning(f'Key "{key}" has not default and environment values')

    return value
