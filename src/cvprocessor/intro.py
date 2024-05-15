"""
This module contains the class Intro, which is used to store the introduction
"""
import pandas as pd


class Intro:
    """
    The Intro class is used to store the introduction of the CV file.

    Attributes:
    short_summary (str): A short summary of the CV file.
    long_summary (str): A long summary of the CV file.
    tagline (str): A tagline of the CV file.

    Methods:
    __init__(filename): Initializes the Intro class by loading the introduction from the given file.
    __str__(): Returns a string representation of the Intro class.
    __repr__(): Returns a string representation of the Intro class.
    """

    def __init__(self):
        self.short_summary = str()
        self.long_summary = str()
        self.tagline = str()

    def get_short_summary(self):
        """
        Get the short summary of the CV file.
        """
        return self.short_summary

    def get_long_summary(self):
        """
        Get the long summary of the CV file.
        """
        return self.long_summary

    def get_tagline(self):
        """
        Get the tagline of the CV file.
        """
        return self.tagline

    def load(self, filename):
        """
        Load the introduction from the given file.
        """
        intro = pd.read_excel(filename, sheet_name="Intro")
        self.short_summary = intro["Short summary"].values[0]
        self.long_summary = intro["Welcome"].values[0]
        self.tagline = intro["Tagline"].values[0]

    def __str__(self) -> str:
        string = f"Short summary: {self.short_summary}\n"
        string += f"Long summary: {self.long_summary}\n"
        string += f"Tagline: {self.tagline}\n\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"Intro("
            f"short_summary={self.short_summary}, "
            f"long_summary={self.long_summary}, "
            f"tagline={self.tagline})"
        )
        return string
