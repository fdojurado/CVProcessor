"""
This module contains common functions that are used in the cvprocessor module.
"""
import pandas as pd


def check_nan(value) -> bool:
    """
    Check if a value is NaN.

    :param value: The value to check.
    :type value: Any
    :return: True if the value is NaN, False otherwise.
    :rtype: bool
    """
    is_nan = pd.isna(value)
    return is_nan
