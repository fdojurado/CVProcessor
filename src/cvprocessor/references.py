"""
This module contains the classes to handle the references section of the CV.
"""
import pandas as pd


class ReferenceData:
    """
    The ReferenceData class is used to store the reference data.

    Attributes:
    name (str): The name of the reference.
    email (str): The email of the reference.
    position (str): The position of the reference.
    institution (str): The institution of the reference.
    """

    def __init__(self):
        self.name = str()
        self.email = str()
        self.position = str()
        self.institution = str()

    def load(self, filename):
        """
        Load the reference data.
        """
        self.name = filename["Name"]
        self.email = filename["Email"]
        self.position = filename["Position"]
        self.institution = filename["Institution"]

    def __str__(self):
        string = f"Name: {self.name}\n"
        string += f"Email: {self.email}\n"
        string += f"Position: {self.position}\n"
        string += f"Institution: {self.institution}\n"
        return string

    def __repr__(self):
        string = (
            f"ReferenceData("
            f"name={self.name}, "
            f"email={self.email}, "
            f"position={self.position}, "
            f"institution={self.institution})"
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

    def __str__(self):
        string = ""
        for reference in self.references:
            string += str(reference) + "\n"
        return string

    def __repr__(self):
        return f"References({repr(self.references)})"
