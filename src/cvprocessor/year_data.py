"""
This module contains the YearData class and functions to process year data.
"""
import pandas as pd


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
        (year.start_year for year in years if year.start_year is not None))
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
        (year.end_year for year in years if year.end_year is not None))
    return end_year


def add_year(years: list[YearData], year: YearData):
    """
    Add a year to the list of year data.

    :param years: The list of year data.
    :type years: list[YearData]
    :param year: The year to add.
    :type year: YearData
    """
    assert isinstance(year, YearData)
    years.append(year)


def sort_years(years: list[YearData]) -> list[YearData]:
    """
    Sort the years.

    :param years: The list of year data.
    :type years: list[YearData]
    """
    years = sorted(
        years, key=lambda x: x.start_year if x.start_year is not None else 0, reverse=True)
    return years


def process_year_data(filename: pd.DataFrame, years: list[YearData]) -> list[YearData]:
    """
    Process the year data.

    :param filename: The filename.
    :type filename: pd.DataFrame
    :param year_data: The year data.
    :type year_data: list[YearData]
    """
    year_range = filename["Year"].split(";")
    year_range = list(filter(None, year_range))
    for year in year_range:
        year_obj = YearData()
        year_obj.year_range = year
        year_obj.process_year_range(year)
        add_year(years, year_obj)
    years = sort_years(years)
    return years
