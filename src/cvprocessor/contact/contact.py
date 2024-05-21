"""
This module contains the class Contact, which is used to store the contact information
of the author.
"""
import pandas as pd

contact_types = {
    "email": "Email",
    "telephone": "Telephone",
    "address": "Address",
    "location": "Location",
    "city": "City",
    "country": "Country",
    "coordinates": "Coordinates"
}


class Contact:
    """
    A class to represent the contact information of an author.

    Attributes:
    email (str): The email of the author.
    telephone (str): The telephone of the author.
    address (str): The address of the author.
    location (str): The location of the author.
    """

    def __init__(self):
        self.email = str()
        self.telephone = str()
        self.address = str()
        self.location = str()
        self.city = str()
        self.country = str()
        self.coordinates = tuple()

    def get_email(self):
        """
        Returns the email of the author.
        """
        return self.email

    def get_telephone(self):
        """
        Returns the telephone of the author.
        """
        return self.telephone

    def get_address(self):
        """
        Returns the address of the author.
        """
        return self.address

    def get_location(self):
        """
        Returns the location of the author.
        """
        return self.location

    def get_city(self):
        """
        Returns the city of the author.
        """
        return self.city

    def get_country(self):
        """
        Returns the country of the author.
        """
        return self.country

    def get_coordinates(self):
        """
        Returns the coordinates of the author.
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

    def load(self, df):
        """
        Loads the contact information of the author.
        """
        for key, value in contact_types.items():
            if value in df and not pd.isnull(df[value]):
                # check if we are processing the coordinates
                if key == "coordinates":
                    self.process_coordinates(df[value])
                else:
                    setattr(self, key, df[value])
            else:
                setattr(self, key, str())

    def __repr__(self):
        # print the variables
        string = (
            f"Contact("
            f"email={self.email}, "
            f"telephone={self.telephone}, "
            f"address={self.address}, "
            f"location={self.location}, "
            f"city={self.city}, "
            f"country={self.country}, "
            f"coordinates={self.coordinates})"
        )
        return string
