"""
This module contains the classes to handle the data of the institutes.
"""
import pandas as pd
from cvprocessor.name.name import Name
from cvprocessor.contact.contact import Contact
from cvprocessor.links.links import Links


class InstituteData:
    """
    A class to represent the data of an institute.
    """

    def __init__(self):
        self.id = str()
        self.name = Name()
        self.department = Name()
        self.group = Name()
        self.contact = Contact()
        self.links = Links()

    def get_id(self):
        """
        Get the ID of the institute.
        """
        return self.id

    def load(self, pd_dataframe):
        """
        Load the data from a pandas dataframe.
        """
        self.id = pd_dataframe["id"]
        if "Name" in pd_dataframe:
            if "Name Abbreviation" in pd_dataframe:
                self.name.load(pd_dataframe["Name"],
                               pd_dataframe["Name Abbreviation"])
            else:
                self.name.load(pd_dataframe["Name"], "")
        if "Department" in pd_dataframe:
            if "Department Abbreviation" in pd_dataframe:
                self.department.load(pd_dataframe["Department"],
                                     pd_dataframe["Department Abbreviation"])
            else:
                self.department.load(pd_dataframe["Department"], "")
        if "Group" in pd_dataframe:
            if "Group Abbreviation" in pd_dataframe:
                self.group.load(pd_dataframe["Group"],
                                pd_dataframe["Group Abbreviation"])
            else:
                self.group.load(pd_dataframe["Group"], "")
        self.contact.load(pd_dataframe)
        self.links.load(pd_dataframe)

    def __repr__(self):
        string = (
            f"InstituteData("
            f"id={self.id}, "
            f"name={repr(self.name)}, "
            f"department={repr(self.department)}, "
            f"group={repr(self.group)}, "
            f"contact={repr(self.contact)}, "
            f"links={repr(self.links)})"
        )
        return string


class Institutes:
    """
    A class to represent the institutes.

    Attributes:
    institutes (list): A list of InstituteData objects.

    Methods:
    get_institute(): Get the institute by its ID.
    load(): Load the institutes from the filename.
    """

    def __init__(self):
        self.institutes = []

    def get_institute(self, institute_id):
        """
        Get the institute by its ID.
        """
        if isinstance(institute_id, str):
            institute_id = int(institute_id)
        for institute in self.institutes:
            if institute.get_id() == institute_id:
                return institute
        return None

    def load(self, filename):
        """
        Load the institutes from the filename.
        """
        institutes_df = pd.read_excel(filename, sheet_name="Institutes")
        for _, institute in institutes_df.iterrows():
            institute_data = InstituteData()
            institute_data.load(institute)
            self.institutes.append(institute_data)

    def __repr__(self):
        string = f"Institutes(Institute={repr(self.institutes)})"
        return string

    def __iter__(self):
        return iter(self.institutes)
