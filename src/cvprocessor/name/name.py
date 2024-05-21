"""
This module contains the class Name.
"""


class Name:
    """
    A class to represent the name and abbreviation of an institute/author.

    Attributes:
    name (str): The name of the institute/author.
    abbrv (str): The abbreviation of the institute/author.
    """

    def __init__(self):
        self.name = str()
        self.abbrv = str()

    def get_name(self):
        """
        Get the name of the institute/author.
        """
        return self.name

    def get_abbrv(self):
        """
        Get the abbreviation of the institute/author.
        """
        return self.abbrv

    def load(self, name: str, abbrv: str):
        """
        Load the institute/author information.
        """
        self.name = name
        self.abbrv = abbrv

    def __repr__(self):
        string = (
            f"Name("
            f"name={self.name}, "
            f"abbrv={self.abbrv})"
        )
        return string
