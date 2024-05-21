"""
This module contains the GrantsAwards class and GrantsAwardsData class.
"""
import pandas as pd

from cvprocessor.date.date import Dates


class GrantsAwardsData:
    """
    A class to represent the grants and awards data.

    Attributes:
    date: The date of the grant or award.
    description: The description of the grant or award.
    institution: The institution that awarded the grant or award.
    country: The country where the grant or award was awarded.
    value: The value of the grant or award.

    Methods:
    __str__: Returns the string representation of the grants and awards data.
    __repr__: Returns the string representation of the grants and awards data.
    """

    def __init__(self):
        self.dates: Dates = Dates()
        self.description = str()
        self.institution_id = str()
        self.value = str()

    def get_description(self):
        """
        Get the description of the grant or award.
        """
        return self.description

    def get_institution_id(self):
        """
        Get the institution id of the grant or award.
        """
        return self.institution_id

    def get_value(self):
        """
        Get the value of the grant or award.
        """
        return self.value

    def load(self, filename):
        """
        Load the grants and awards data from the given file.
        """
        self.dates.load(filename)
        self.description = filename["Description"]
        self.institution_id = filename["Institution id"]
        self.value = filename["Value"]

    def __repr__(self) -> str:
        string = (
            f"GrantsAwardsData("
            f"dates={repr(self.dates)}, "
            f"description={self.description}, "
            f"institution id={self.institution_id}, "
            f"value={self.value})"
        )
        return string


class GrantsAwards:
    """
    A class to represent the grants and awards data.

    Attributes:
    grants_awards: The grants and awards data.

    Methods:
    get_oldest_date: Returns the oldest date in the grants and awards data.
    load: Loads the grants and awards data from the given file.
    __str__: Returns the string representation of the grants and awards data.
    __repr__: Returns the string representation of the grants and awards data.
    """

    def __init__(self):
        self.grants_awards = []

    def get_oldest_date(self):
        """
        Returns the oldest date in the grants and awards data.
        """
        return self.grants_awards[-1].dates.get_start()

    def load(self, filename):
        """
        Load the grants and awards data from the given file.
        """
        grants_rewards_df = pd.read_excel(
            filename, sheet_name="Grants_awards")
        for _, row in grants_rewards_df.iterrows():
            self.grants_awards.append(GrantsAwardsData())
            self.grants_awards[-1].load(row)
        self.grants_awards = sorted(
            self.grants_awards, key=lambda x: x.dates.get_start(), reverse=True)

    def __repr__(self) -> str:
        string = f"GrantsAwards(grants_awards={repr(list(self.grants_awards))})"
        return string

    def __iter__(self):
        return iter(self.grants_awards)
