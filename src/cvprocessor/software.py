"""
This module contains the Software class and SofwareData class.
"""
import pandas as pd

from cvprocessor.links.links import Links


class SoftwareData:
    """
    The SoftwareData class is used to store the software data.

    Attributes:
    info (Details): The information of the software.
    resources (Social): The resources of the software.
    summary (str): The summary of the software.
    license (str): The license of the software.
    """

    def __init__(self):
        self.id = int()
        self.name = str()
        self.version = str()
        self.description = str()
        self.links = Links()
        self.summary = str()
        self.license = str()

    def get_id(self):
        """
        Get the ID of the software.
        """
        return self.id

    def get_name(self):
        """
        Get the name of the software.
        """
        return self.name

    def get_version(self):
        """
        Get the version of the software.
        """
        return self.version

    def get_description(self):
        """
        Get the description of the software.
        """
        return self.description

    def get_summary(self):
        """
        Get the summary of the software.
        """
        return self.summary

    def get_license(self):
        """
        Get the license of the software.
        """
        return self.license

    def load(self, filename) -> None:
        """
        Load the software data from a file.
        """
        self.id = filename["id"]
        self.name = filename["Name"]
        self.version = filename["Version"]
        self.description = filename["Description"]
        self.links.load(filename)
        self.summary = filename["Summary"]
        self.license = filename["License"]

    def __repr__(self) -> str:
        string = (
            f"SoftwareData("
            f"id={self.id}, "
            f"name={self.name}, "
            f"version={self.version}, "
            f"description={self.description}, "
            f"links={repr(self.links)}, "
            f"summary={self.summary}, "
            f"license={self.license})"
        )
        return string


class Software:
    """
    The Software class is used to store the software data.

    Attributes:
    filename (str): The filename of the software data.
    """

    def __init__(self):
        self.softwares = []

    def get_software(self, software_id):
        """
        Get the software by ID.
        """
        if not software_id:
            return None
        if isinstance(software_id, str):
            try:
                software_id = int(float(software_id))
            except ValueError:
                return None
        for software in self:
            if software.get_id() == software_id:
                return software
        return None

    def get_software_alphabetically(self):
        """
        Get the software alphabetically.
        """
        return sorted(self.softwares, key=lambda x: x.info.name)

    def load(self, filename):
        """
        Load the software data.
        """
        software_df = pd.read_excel(filename, sheet_name="Software")
        for _, row in software_df.iterrows():
            self.softwares.append(SoftwareData())
            self.softwares[-1].load(row)

    def __repr__(self) -> str:
        string = f"Software(software={repr(self.softwares)})"
        return string

    def __iter__(self):
        return iter(self.softwares)
