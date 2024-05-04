import pandas as pd


class InstituteData:
    def __init__(self, pd_dataframe):
        self._pd_dataframe = pd_dataframe
        self._id = None
        self._name = None
        self._location = None
        self._website = None
        self._load_institute()

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def website(self):
        return self._website

    def _load_institute(self):
        self._id = self._pd_dataframe["id"]
        self._name = self._pd_dataframe["Name"]
        self._location = self._pd_dataframe["Location"]
        self._website = self._pd_dataframe["Website"]
        # self._doi = self.filename["doi"]

    def print(self):
        print(f"Institute ID: {self._id}")
        print(f"Institute name: {self._name}")
        print(f"Location: {self._location}")
        print(f"Website: {self._website}")
        # print(f"DOI: {self._doi}")
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

    def get_institute(self, institute_name):
        for institute in self.institute:
            if institute.name == institute_name:
                return institute
        return None

    def _load_institutes(self):
        institutes_df = pd.read_excel(self.filename, sheet_name="Institutes")
        return [InstituteData(institute) for index, institute in institutes_df.iterrows()]

    def print(self):
        for institute in self.institute:
            institute.print()
