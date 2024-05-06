import pandas as pd


class InstituteData:
    def __init__(self, pd_dataframe):
        self._pd_dataframe = pd_dataframe
        self._id = None
        self._name = None
        self._address = None
        self._city = None
        self._country = None
        self._coordinates = None
        self._url = None
        self._load_institute()

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @property
    def city(self):
        return self._city

    @property
    def country(self):
        return self._country

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def url(self):
        return self._url

    def convert_coordinates(self, lalng):
        lalng = lalng.replace("°", "").strip()
        if "S" in lalng or "W" in lalng:
            lalng = lalng.replace("S", "").replace("W", "")
            lalng = "-" + lalng
        else:
            lalng = lalng.replace("N", "").replace("E", "")
        return float(lalng)

    def process_coordinates(self):
        # Coordinates can be of the form 37.7983° S, 144.9610° E or 3.342119819025848, -76.5306449189542
        # We will convert them to the form 37.7983, 144.9610
        if self._coordinates is not None:
            # split into latitude and longitude
            coordinates = self._coordinates.split(", ")
            coordinates = [self.convert_coordinates(
                coord) for coord in coordinates]
            self._coordinates = tuple(coordinates)

    def _load_institute(self):
        self._id = self._pd_dataframe["id"]
        self._name = self._pd_dataframe["Name"]
        self._address = self._pd_dataframe["Address"]
        self._city = self._pd_dataframe["City"]
        self._country = self._pd_dataframe["Country"]
        self._url = self._pd_dataframe["URL"]
        self._coordinates = self._pd_dataframe["Coordinates"]
        self.process_coordinates()

    def print(self):
        print(f"Institute ID: {self._id}")
        print(f"Institute Name: {self._name}")
        print(f"Institute Address: {self._address}")
        print(f"Institute City: {self._city}")
        print(f"Institute Country: {self._country}")
        print(f"Institute URL: {self._url}")
        print(f"Institute Coordinates: {self._coordinates}")
        print("\n")


class Institutes:
    def __init__(self, filename):
        self._filename = filename
        self._institute = self._load_institutes()

    @property
    def filename(self):
        return self._filename

    @property
    def institute(self):
        return self._institute

    def get_institute(self, institute_id):
        if isinstance(institute_id, str):
            institute_id = int(institute_id)
        for institute in self.institute:
            if institute.id == institute_id:
                return institute
        return None

    def _load_institutes(self):
        institutes_df = pd.read_excel(self.filename, sheet_name="Institutes")
        return [InstituteData(institute) for index, institute in institutes_df.iterrows()]

    def print(self):
        for institute in self.institute:
            institute.print()
