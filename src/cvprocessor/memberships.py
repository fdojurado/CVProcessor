"""
This module contains the Memberships class and the MembershipData class.
"""
import pandas as pd


class MembershipData:
    """
    The MembershipData class is used to store the membership data.

    Attributes:
    year (pd.Timestamp): The year of the membership.
    membership (str): The membership.
    """

    def __init__(self):
        self.year: pd.Timestamp = pd.Timestamp("NaT")
        self.membership = str()

    def get_year(self):
        """
        Get the year of the membership.
        """
        return self.year

    def get_membership(self):
        """
        Get the membership.
        """
        return self.membership

    def load(self, filename):
        """
        Load the membership data.
        """
        self.year = filename["Year"]
        self.membership = filename["Membership"]

    def __str__(self):
        string = f"Year: {self.year}\n"
        string += f"Membership: {self.membership}\n"
        return string

    def __repr__(self):
        return f"MembershipData({repr(self.year)}, {repr(self.membership)})\n"


class Memberships:
    """
    The Memberships class is used to store the memberships data.
    """

    def __init__(self):
        self.memberships = []

    def load(self, filename):
        """
        Load the memberships data.
        """
        membership_df = pd.read_excel(
            filename, sheet_name="Professional_memberships")
        for _, row in membership_df.iterrows():
            membership = MembershipData()
            membership.load(row)
            self.memberships.append(membership)

    def __str__(self):
        string = ""
        for membership in self.memberships:
            string += str(membership) + "\n"
        return string

    def __repr__(self):
        return f"Memberships(memberships={repr(list(map(repr, self.memberships)))})\n"

    def __iter__(self):
        return iter(self.memberships)
