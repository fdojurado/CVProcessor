"""
This module contains the classes to handle the references section of the CV.
"""
import pandas as pd


class ReferenceData:
    """
    The ReferenceData class is used to store the reference data.

    Attributes:
    author_id (str): The author ID of the reference.
    """

    def __init__(self):
        self.author_id = str()

    def get_author_id(self):
        """
        Get the author ID of the reference.
        """
        return self.author_id

    def load(self, filename):
        """
        Load the reference data.
        """
        if "Author id" not in filename:
            raise ValueError(
                "Author id column not found in the references data.")
        self.author_id = filename["Author id"]

    def __repr__(self):
        string = (
            f"ReferenceData("
            f"author_id={self.author_id})"
        )
        return string


class References:
    """
    The References class is used to store the references data.

    Attributes:
    references (list): The list of references.

    Methods:
    load(): Load the references data.
    """

    def __init__(self):
        self.references = []

    def load(self, filename):
        """
        Load the references data.
        """
        reference_df = pd.read_excel(filename, sheet_name="References")
        for _, row in reference_df.iterrows():
            reference = ReferenceData()
            reference.load(row)
            self.references.append(reference)

    def __repr__(self):
        return f"References({repr(self.references)})"

    def __iter__(self):
        return iter(self.references)
