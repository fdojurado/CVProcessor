"""
This module contains the Date class and functions to process the date data from the CV.
"""
import pandas as pd


class Date:
    """
    A class to represent the date.

    Attributes:
    range (str): The date range.
    start (datetime): The start date.
    end (datetime): The end date.
    """

    def __init__(self):
        self.range = None
        self.start = None
        self.end = None

    def get_range(self):
        """
        Get the date range.
        """
        return self.range

    def get_start(self):
        """
        Get the date start.
        """
        return self.start

    def get_end(self):
        """
        Get the date end.
        """
        return self.end

    def format_date(self, date):
        """
        Format the date to a datetime object.
        """
        date = date.strip()
        date = pd.to_datetime(date, format="%b %Y")
        return date

    def process_date_range(self, date_range):
        """
        Process the date range.
        """
        date_range = date_range.split("-")
        self.start = self.format_date(date_range[0])
        self.start = pd.to_datetime(self.start, format="%b %Y")
        if len(date_range) > 1:
            self.end = self.format_date(date_range[1])
            self.end = pd.to_datetime(self.end, format="%b %Y")
        else:
            self.end = None

    def __repr__(self):
        string = (
            f"Date("
            f"range={self.range}, "
            f"start={self.start}, "
            f"end={self.end})"
        )
        return string


class Dates:
    """
    Links class is used to store an array of dates.
    """

    def __init__(self):
        """
        Initialize the Links class.
        """
        self.dates: list[Date] = []

    def add_date(self, date: Date):
        """
        Add a date to the list of dates.
        """
        self.dates.append(date)

    def get_start(self):
        """
        Get the start date.
        """
        if len(self.dates) > 1:
            start = min(
                (date.start for date in self.dates if date.start is not None))
        else:
            start = self.dates[0].start
        return start

    def get_end(self):
        """
        Get the end date.
        """
        if len(self.dates) > 1:
            end = max(
                (date.end for date in self.dates if date.end is not None))
        else:
            end = self.dates[0].end
        return end

    def sort_dates(self):
        """
        Sort the dates.
        """
        self.dates = sorted(
            self.dates, key=lambda x: x.start if x.start is not None else 0, reverse=True)

    def load(self, df: pd.DataFrame):
        """
        Add dates to the list of dates.
        """
        dates = df["Dates"].split(";")
        dates = list(filter(None, dates))
        for date in dates:
            date_obj = Date()
            if "-" in date:
                date_obj.range = date
                date_obj.process_date_range(date)
            else:
                date_obj.range = date
                if len(date) == 4:
                    date = "Jan " + date
                date_obj.start = date_obj.format_date(date)
            self.add_date(date_obj)
        self.sort_dates()

    def __iter__(self):
        return iter(self.dates)

    def __repr__(self):
        string = f"Dates({[repr(date) for date in self.dates]})"
        return string
