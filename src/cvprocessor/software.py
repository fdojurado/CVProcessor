"""
This module contains the Software class and SofwareData class.
"""
import pandas as pd


class SoftwareInfo:
    """
    A class to represent the information of a software.

    Attributes:
    id (int): The ID of the software.
    name (str): The name of the software.
    version (str): The version of the software.
    description (str): The description of the software.
    """

    def __init__(self):
        self.id = str()
        self.name = str()
        self.version = str()
        self.description = str()

    def load(self, filename):
        """
        Load the software information.
        """
        self.id = filename["id"]
        self.name = filename["Name"]
        self.version = filename["Version"]
        self.description = filename["Description"]

    def __str__(self) -> str:
        string = f"ID: {self.id}\n"
        string += f"Name: {self.name}\n"
        string += f"Version: {self.version}\n"
        string += f"Description: {self.description}\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"SoftwareInfo("
            f"id={self.id}, "
            f"name={self.name}, "
            f"version={self.version}, "
            f"description={self.description})"
        )
        return string


class SoftwareResources:
    """
    A class to represent the resources of a software.

    Attributes:
    repository (str): The repository link of the software.
    demo (str): The demo link of the software.
    website (str): The website link of the software.
    """

    def __init__(self):
        self.repository = str()
        self.demo = str()
        self.website = str()

    def load(self, filename):
        """
        Load the software resources.
        """
        self.repository = filename["Repository"]
        self.demo = filename["Demo"]
        self.website = filename["Website"]

    def __str__(self) -> str:
        string = f"Repository: {self.repository}\n"
        string += f"Demo: {self.demo}\n"
        string += f"Website: {self.website}\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"SoftwareResources("
            f"repository={self.repository}, "
            f"demo={self.demo}, "
            f"website={self.website})"
        )
        return string


class SoftwareData:
    """
    The SoftwareData class is used to store the software data.

    Attributes:
    info (SoftwareInfo): The information of the software.
    resources (SoftwareResources): The resources of the software.
    summary (str): The summary of the software.
    license (str): The license of the software.
    """

    def __init__(self):
        self.info = SoftwareInfo()
        self.resources = SoftwareResources()
        self.summary = str()
        self.license = str()

    def get_id(self):
        """
        Get the ID of the software.
        """
        return self.info.id

    def get_name(self):
        """
        Get the name of the software.
        """
        return self.info.name

    def get_version(self):
        """
        Get the version of the software.
        """
        return self.info.version

    def get_description(self):
        """
        Get the description of the software.
        """
        return self.info.description

    def get_repository(self):
        """
        Get the repository link of the software.
        """
        return self.resources.repository

    def get_demo(self):
        """
        Get the demo link of the software.
        """
        return self.resources.demo

    def get_website(self):
        """
        Get the website link of the software.
        """
        return self.resources.website

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
        self.info.load(filename)
        self.resources.load(filename)
        self.summary = filename["Summary"]
        self.license = filename["License"]

    def __str__(self) -> str:
        string = str(self.info)
        string += str(self.resources)
        string += f"Summary: {self.summary}\n"
        string += f"License: {self.license}\n\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"SoftwareData("
            f"info={repr(self.info)}, "
            f"resources={repr(self.resources)}, "
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
            software_id = int(software_id)
        for software in self.softwares:
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

    def __str__(self) -> str:
        string = ""
        for software in self.softwares:
            string += str(software) + "\n"
        return string

    def __repr__(self) -> str:
        string = f"Software(software={repr(self.softwares)})"
        return string

    def __iter__(self):
        return iter(self.softwares)
