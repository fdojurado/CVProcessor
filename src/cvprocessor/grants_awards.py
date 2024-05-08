import pandas as pd


class GrantsAwardsData:
    def __init__(self, filename):
        self._filename = filename
        self._year = None
        self._description = None
        self._institution = None
        self._country = None
        self._value = None
        self._load_grants_awards()

    @property
    def filename(self):
        return self._filename

    @property
    def year(self):
        return self._year

    @property
    def description(self):
        return self._description

    @property
    def institution(self):
        return self._institution

    @property
    def country(self):
        return self._country

    @property
    def value(self):
        return self._value

    def _load_grants_awards(self):
        self._year = self.filename["Year"]
        self._year = pd.to_datetime(self.year, format="%Y").year
        self._description = self.filename["Description"]
        self._institution = self.filename["Institution"]
        self._country = self.filename["Country"]
        self._value = self.filename["Value"]

    def print(self):
        print(f"Year: {self.year}")
        print(f"Description: {self.description}")
        print(f"Institution: {self.institution}")
        print(f"Country: {self.country}")
        print(f"Value: {self.value}")
        print("\n")


class GrantsAwards:
    def __init__(self, filename):
        self._filename = filename
        self._grants_awards = self._load_grants_awards()
        # sort the grants_awards data by year
        self._grants_awards = sorted(
            self.grants_awards, key=lambda x: x.year, reverse=True)

    @property
    def filename(self):
        return self._filename

    @property
    def grants_awards(self):
        return self._grants_awards

    def get_oldest_year(self):
        return self.grants_awards[-1].year

    def _load_grants_awards(self):
        self._filename = pd.read_excel(
            self.filename, sheet_name="Grants_awards")
        return [GrantsAwardsData(row) for index, row in self.filename.iterrows()]

    def print(self):
        for grant_award in self.grants_awards:
            grant_award.print()
