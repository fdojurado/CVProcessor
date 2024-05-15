"""
This module contains the GrantsAwards class and GrantsAwardsData class.
"""
import pandas as pd


class GrantsAwardsData:
    """
    A class to represent the grants and awards data.

    Attributes:
    year: The year of the grant or award.
    description: The description of the grant or award.
    institution: The institution that awarded the grant or award.
    country: The country where the grant or award was awarded.
    value: The value of the grant or award.

    Methods:
    __str__: Returns the string representation of the grants and awards data.
    __repr__: Returns the string representation of the grants and awards data.
    """

    def __init__(self):
        self.year: pd.Timestamp = pd.Timestamp("NaT")
        self.description = str()
        self.institution = str()
        self.country = str()
        self.value = str()

    def get_year(self):
        """
        Get the year of the grant or award.
        """
        return self.year

    def get_description(self):
        """
        Get the description of the grant or award.
        """
        return self.description

    def get_institution(self):
        """
        Get the institution that awarded the grant or award.
        """
        return self.institution

    def get_country(self):
        """
        Get the country where the grant or award was awarded.
        """
        return self.country

    def get_value(self):
        """
        Get the value of the grant or award.
        """
        return self.value

    def load(self, filename):
        """
        Load the grants and awards data from the given file.
        """
        year = filename["Year"]
        self.year = pd.to_datetime(year, format="%Y").year
        self.description = filename["Description"]
        self.institution = filename["Institution"]
        self.country = filename["Country"]
        self.value = filename["Value"]

    def __str__(self) -> str:
        string = f"Year: {self.year}\n"
        string += f"Description: {self.description}\n"
        string += f"Institution: {self.institution}\n"
        string += f"Country: {self.country}\n"
        string += f"Value: {self.value}\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"GrantsAwardsData("
            f"year={self.year}, "
            f"description={self.description}, "
            f"institution={self.institution}, "
            f"country={self.country}, "
            f"value={self.value})"
        )
        return string


class GrantsAwards:
    """
    A class to represent the grants and awards data.

    Attributes:
    grants_awards: The grants and awards data.

    Methods:
    get_oldest_year: Returns the oldest year in the grants and awards data.
    load: Loads the grants and awards data from the given file.
    __str__: Returns the string representation of the grants and awards data.
    __repr__: Returns the string representation of the grants and awards data.
    """

    def __init__(self):
        self.grants_awards = []

    def get_oldest_year(self):
        """
        Returns the oldest year in the grants and awards data.
        """
        return self.grants_awards[-1].year

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
            self.grants_awards, key=lambda x: x.year, reverse=True)

    def __str__(self) -> str:
        string = ""
        for grants_award in self.grants_awards:
            string += str(grants_award) + "\n"
        return string

    def __repr__(self) -> str:
        string = f"GrantsAwards(grants_awards={repr(list(self.grants_awards))})"
        return string

    def __iter__(self):
        return iter(self.grants_awards)
