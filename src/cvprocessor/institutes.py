"""
This module contains the classes to handle the data of the institutes.
"""
import pandas as pd


class InstituteInfo:
    """
    A class to represent the information of an institute.
    """

    def __init__(self):
        self.id = None
        self.name = None
        self.name_abbr = None
        self.department = None
        self.department_abbr = None

    def load(self, filename):
        """
        Load the institute information.
        """
        self.id = filename["id"]
        self.name = filename["Name"]
        self.name_abbr = filename["Name Abbreviation"]
        self.department = filename["Department"]
        self.department_abbr = filename["Department Abbreviation"]

    def __str__(self):
        string = f"Institute ID: {self.id}\n"
        string += f"Institute Name: {self.name}\n"
        string += f"Institute Name Abbreviation: {self.name_abbr}\n"
        string += f"Institute Department: {self.department}\n"
        string += f"Institute Department Abbreviation: {self.department_abbr}\n"
        return string

    def __repr__(self):
        string = (
            f"InstituteInfo("
            f"id={self.id}, "
            f"name={self.name}, "
            f"name_abbr={self.name_abbr}, "
            f"department={self.department}, "
            f"department_abbr={self.department_abbr})"
        )
        return string


class InstituteLocation:
    """
    A class to represent the location of an institute.
    """

    def __init__(self):
        self.address = str()
        self.city = str()
        self.country = str()
        self.coordinates = tuple()

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
            f"InstituteLocation("
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
        self.info = InstituteInfo()
        self.location = InstituteLocation()
        self.url = None

    def get_id(self):
        """
        Get the ID of the institute.
        """
        return self.info.id

    def get_name(self):
        """
        Get the name of the institute.
        """
        return self.info.name

    def get_name_abbr(self):
        """
        Get the name abbreviation of the institute.
        """
        return self.info.name_abbr

    def get_department(self):
        """
        Get the department of the institute.
        """
        return self.info.department

    def get_department_abbr(self):
        """
        Get the department abbreviation of the institute.
        """
        return self.info.department_abbr

    def get_address(self):
        """
        Get the address of the institute.
        """
        return self.location.address

    def get_city(self):
        """
        Get the city of the institute.
        """
        return self.location.city

    def get_country(self):
        """
        Get the country of the institute.
        """
        return self.location.country

    def get_coordinates(self):
        """
        Get the coordinates of the institute.
        """
        return self.location.coordinates

    def get_url(self):
        """
        Get the URL of the institute.
        """
        return self.url

    def load(self, pd_dataframe):
        """
        Load the data from a pandas dataframe.
        """
        self.info.load(pd_dataframe)
        self.location.load(pd_dataframe)
        self.url = pd_dataframe["URL"]

    def __str__(self):
        string = str(self.info)
        string += str(self.location)
        string += f"url: \n{self.url}\n"
        return string

    def __repr__(self):
        string = (
            f"InstituteData("
            f"info={repr(self.info)}, "
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
