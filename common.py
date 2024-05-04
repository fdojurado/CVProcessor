import pandas as pd


def check_nan(value) -> bool:
    if pd.isna(value):
        is_nan = True
    else:
        is_nan = False
    return is_nan
