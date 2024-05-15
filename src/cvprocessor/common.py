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


class YearData:
    """
    A class to represent the year data.

    Attributes:
    year_range (str): The year range.
    start_year (datetime): The start year.
    end_year (datetime): The end year.
    """

    def __init__(self):
        self.year_range = None
        self.start_year = None
        self.end_year = None

    def format_year(self, year):
        """
        Format the year to a datetime object.
        """
        year = year.strip()
        year = pd.to_datetime(year, format="%b %Y")
        return year

    def process_year_range(self, year_range):
        """
        Process the year range.
        """
        year_range = year_range.split("-")
        self.start_year = self.format_year(year_range[0])
        self.start_year = pd.to_datetime(self.start_year, format="%b %Y")
        if len(year_range) > 1:
            self.end_year = self.format_year(year_range[1])
            self.end_year = pd.to_datetime(self.end_year, format="%b %Y")
        else:
            self.end_year = None

    def __str__(self):
        string = f"Year range: {self.year_range}\n"
        string += f"Start year: {self.start_year}\n"
        string += f"End year: {self.end_year}\n"
        return string

    def __repr__(self):
        string = (
            f"YearData("
            f"year_range={self.year_range}, "
            f"start_year={self.start_year}, "
            f"end_year={self.end_year})"
        )
        return string


def get_start_year(years: list[YearData]) -> pd.Timestamp:
    """
    Get the start year from a list of year data.

    :param years: The list of year data.
    :type years: list[YearData]
    :return: The start year.
    :rtype: pd.Timestamp
    """
    start_year = min(
        [year.start_year for year in years if year.start_year is not None])
    return start_year


def get_end_year(years: list[YearData]) -> pd.Timestamp:
    """
    Get the end year from a list of year data.

    :param years: The list of year data.
    :type years: list[YearData]
    :return: The end year.
    :rtype: pd.Timestamp
    """
    end_year = max(
        [year.end_year for year in years if year.end_year is not None])
    return end_year
