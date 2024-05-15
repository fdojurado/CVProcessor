"""
This module contains the classes to handle the data of the institutes.
"""
import pandas as pd


class Personal:
    """
    A class to represent the personal information of an institute.

    Attributes:
    name (str): The name of the institute.
    name_abbr (str): The abbreviation of the institute.
    """

    def __init__(self):
        self.name = None
        self.abbrv = None

    def get_name(self):
        """
        Get the name of the institute.
        """
        return self.name

    def get_abbrv(self):
        """
        Get the abbreviation of the institute.
        """
        return self.abbrv

    def load(self, filename):
        """
        Load the institute information.
        """
        self.name = filename["Name"]
        self.abbrv = filename["Name Abbreviation"]

    def __str__(self):
        string = f"Institute Name: {self.name}\n"
        string += f"Institute Abbreviation: {self.abbrv}\n"
        return string

    def __repr__(self):
        string = (
            f"Personal("
            f"name={self.name}, "
            f"name_abbr={self.abbrv})"
        )
        return string


class Department:
    """
    A class to represent the department of an institute.

    Attributes:
    department (str): The name of the department.
    department_abbr (str): The abbreviation of the department.
    """

    def __init__(self):
        self.name = None
        self.abbrv = None

    def get_name(self):
        """
        Get the name of the department.
        """
        return self.name

    def get_abbrv(self):
        """
        Get the abbreviation of the department.
        """
        return self.abbrv

    def load(self, filename):
        """
        Load the institute information.
        """
        self.name = filename["Department"]
        self.abbrv = filename["Department Abbreviation"]

    def __str__(self):
        string = f"Institute Department: {self.name}\n"
        string += f"Institute Department Abbreviation: {self.abbrv}\n"
        return string

    def __repr__(self):
        string = (
            f"Department("
            f"department={self.name}, "
            f"department_abbr={self.abbrv})"
        )
        return string


class Location:
    """
    A class to represent the location of an institute.
    """

    def __init__(self):
        self.address = str()
        self.city = str()
        self.country = str()
        self.coordinates = tuple()

    def get_address(self):
        """
        Get the address of the institute.
        """
        return self.address

    def get_city(self):
        """
        Get the city of the institute.
        """
        return self.city

    def get_country(self):
        """
        Get the country of the institute.
        """
        return self.country

    def get_coordinates(self):
        """
        Get the coordinates of the institute.
        """
        return self.coordinates

    def convert_coordinates(self, lalng):
        """
        Convert the latitude and longitude coordinates to a float value.
        """
        lalng = lalng.replace("°", "").strip()
        if "S" in lalng or "W" in lalng:
            lalng = lalng.replace("S", "").replace("W", "")
            lalng = "-" + lalng
        else:
            lalng = lalng.replace("N", "").replace("E", "")
        return float(lalng)

    def process_coordinates(self, coordinates):
        """
        Process the coordinates to convert them to a tuple of floats.
        """
        if coordinates is not None:
            # split into latitude and longitude
            coordinates = coordinates.split(", ")
            coordinates = [self.convert_coordinates(
                coord) for coord in coordinates]
            self.coordinates = tuple(coordinates)

    def load(self, filename):
        """
        Load the location data.
        """
        self.address = filename["Address"]
        self.city = filename["City"]
        self.country = filename["Country"]
        coordinates = filename["Coordinates"]
        self.process_coordinates(coordinates)

    def __str__(self):
        string = f"Institute Address: {self.address}\n"
        string += f"Institute City: {self.city}\n"
        string += f"Institute Country: {self.country}\n"
        string += f"Institute Coordinates: {self.coordinates}\n"
        return string

    def __repr__(self):
        string = (
            f"Location("
            f"address={self.address}, "
            f"city={self.city}, "
            f"country={self.country}, "
            f"coordinates={self.coordinates})"
        )
        return string


class InstituteData:
    """
    A class to represent the data of an institute.
    """

    def __init__(self):
        self.id = str()
        self.personal = Personal()
        self.department = Department()
        self.location = Location()
        self.url = str()

    def get_id(self):
        """
        Get the ID of the institute.
        """
        return self.id

    def get_url(self):
        """
        Get the URL of the institute.
        """
        return self.url

    def load(self, pd_dataframe):
        """
        Load the data from a pandas dataframe.
        """
        self.id = pd_dataframe["id"]
        self.personal.load(pd_dataframe)
        self.department.load(pd_dataframe)
        self.location.load(pd_dataframe)
        self.url = pd_dataframe["URL"]

    def __repr__(self):
        string = (
            f"InstituteData("
            f"id={self.id}, "
            f"personal={repr(self.personal)}, "
            f"department={repr(self.department)}, "
            f"location={repr(self.location)}, "
            f"url={self.url})"
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

    def __str__(self):
        string = ""
        for institute in self.institutes:
            string += str(institute) + "\n"
        return string

    def __repr__(self):
        string = f"Institutes(Institute={repr(self.institutes)})"
        return string

    def __iter__(self):
        return iter(self.institutes)
