import pandas as pd


class EducationData:
    def __init__(self, filename):
        self._filename = filename
        self._year = None
        self._start_year = None
        self._end_year = None
        self._degree = None
        self._advisor = None
        self._thesis = None
        self._thesis_link = None
        self._award = None
        self._institution = None
        self._country = None
        self._load_education()

    @property
    def filename(self):
        return self._filename

    @property
    def year(self):
        return self._year

    @property
    def start_year(self):
        return self._start_year

    @property
    def end_year(self):
        return self._end_year

    @property
    def degree(self):
        return self._degree

    @property
    def advisor(self):
        return self._advisor

    @property
    def thesis(self):
        return self._thesis

    @property
    def thesis_link(self):
        return self._thesis_link

    @property
    def award(self):
        return self._award

    @property
    def institution(self):
        return self._institution

    @property
    def country(self):
        return self._country

    def process_year_data(self):
        self._year = self.filename["Year"]
        self._year = self._year.split(";")
        self._year = list(filter(None, self._year))
        self._start_year = self._year[0].split("-")[0].strip()
        self._end_year = self._year[-1].split("-")[-1].strip()
        # data can come as month year or date month year
        # convert to datetime
        if len(self._start_year.split()) == 2:
            self._start_year = '1 '+self._start_year
        if len(self._end_year.split()) == 2:
            self._end_year = "1 "+self._end_year
        self._start_year = pd.to_datetime(self._start_year, format="%d %b %Y")
        self._end_year = pd.to_datetime(self._end_year, format="%d %b %Y")

    def _load_education(self):
        self.process_year_data()
        self._degree = self.filename["Degree"]
        self._advisor = self.filename["Advisor"]
        self._thesis = self.filename["Thesis"]
        self._thesis_link = self.filename["Thesis link"]
        self._award = self.filename["Award"]
        self._institution = self.filename["Institution"]
        self._country = self.filename["Country"]

    def print(self):
        print(f"Year: {self.year}")
        print(f"Start year: {self.start_year}")
        print(f"End year: {self.end_year}")
        print(f"Degree: {self.degree}")
        print(f"Advisor: {self.advisor}")
        print(f"Thesis: {self.thesis}")
        print(f"Thesis link: {self.thesis_link}")
        print(f"Award: {self.award}")
        print(f"Institution: {self.institution}")
        print(f"Country: {self.country}")
        print("\n")


class Education:
    def __init__(self, filename):
        self._filename = filename
        self._educations = self._load_educations()
        # sort the education data by end year
        self._educations = sorted(
            self.educations, key=lambda x: x.end_year, reverse=True)

    @property
    def filename(self):
        return self._filename

    @property
    def educations(self):
        return self._educations

    # Get the oldest end year
    def get_oldest_end_year(self):
        return self.educations[-1].end_year.year

    def _load_educations(self):
        education_df = pd.read_excel(self.filename, sheet_name="Education")
        return [EducationData(row) for _, row in education_df.iterrows()]

    def print(self):
        for education in self.educations:
            education.print()
