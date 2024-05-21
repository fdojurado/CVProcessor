"""
This module contains the Memberships class and the MembershipData class.
"""
import pandas as pd

from cvprocessor.date.date import Dates


class MembershipData:
    """
    The MembershipData class is used to store the membership data.

    Attributes:
    date (pd.Timestamp): The date of the membership.
    membership (str): The membership.
    """

    def __init__(self):
        self.dates: Dates = Dates()
        self.membership = str()

    def get_membership(self):
        """
        Get the membership.
        """
        return self.membership

    def load(self, filename):
        """
        Load the membership data.
        """
        self.dates.load(filename)
        self.membership = filename["Membership"]

    def __repr__(self):
        return f"MembershipData({repr(self.dates)}, {repr(self.membership)})\n"


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

    def __repr__(self):
        return f"Memberships(memberships={repr(list(map(repr, self.memberships)))})\n"

    def __iter__(self):
        return iter(self.memberships)
