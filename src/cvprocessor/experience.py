import pandas as pd


class ExperienceData:
    def __init__(self, filename, cv):
        self._filename = filename
        self._cv = cv
        self._year = None
        self._start_year = None
        self._end_year = None
        self._position = None
        self._institution = None
        self._description = None
        self._responsibilities = None
        self._load_experience()

    @property
    def filename(self):
        return self._filename

    @property
    def cv(self):
        return self._cv

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
    def position(self):
        return self._position

    @property
    def institution(self):
        return self._institution

    @property
    def description(self):
        return self._description

    @property
    def responsibilities(self):
        return self._responsibilities

    def get_start_year(self):
        year = 1e6
        date = None
        for start, _ in self.year:
            if not start:
                continue
            if int(start.year) < year:
                year = int(start.year)
                date = start
        return date

    def get_end_year(self):
        year = 0
        date = None
        for _, end in self.year:
            if not end:
                continue
            if end == "present":
                end = pd.to_datetime("today")
            if int(end.year) > year:
                year = int(end.year)
                date = end
        return date

    def format_year(self, year):
        year = year.strip()
        if year != "present":
            year = pd.to_datetime(year, format="%b %Y")
        return year

    def process_year_data(self):
        self._year = self.filename["Year"]
        self._year = self._year.split(";")
        self._year = list(filter(None, self._year))
        year_list = []
        for year in self._year:
            year_split = year.split("-")
            if len(year_split) > 1:
                start_year = year_split[0]
                end_year = year_split[1]
            else:
                start_year = year_split[0]
                end_year = None
            start_year = self.format_year(start_year)
            if end_year:
                end_year = self.format_year(end_year)
            year_list.append((start_year, end_year))
        self._year = year_list

    def _load_experience(self):
        self.process_year_data()
        self._start_year = self.get_start_year()
        self._end_year = self.get_end_year()
        self._position = self.filename["Position"]
        self._institution = self.filename["Institution"]
        self._description = self.filename["Description"]
        self._responsibilities = self.filename["Responsibilities"]

    def __str__(self) -> str:
        string = f"Year: {self.year}\n"
        string += f"Position: {self.position}\n"
        institution = self.cv.institutes.get_institute(self.institution)
        string += f"Institution: {institution.name}\n"
        string += f"Description: {self.description}\n"
        string += f"Responsibilities: {self.responsibilities}\n\n"
        return string

    def __repr__(self) -> str:
        string = f"ExperienceData(year={self.year}, position={self.position}, institution={self.institution}, description={self.description}, responsibilities={self.responsibilities})"
        return string


class Experience:
    def __init__(self, filename, cv):
        self._filename = filename
        self._cv = cv
        self._experience = self._load_experience()
        # sort the experience data by end year but keep in mind that maybe there is a 'present' in the end year
        self._experience = sorted(
            self.experience, key=lambda x: x.end_year if x.end_year else pd.to_datetime('today'), reverse=True)

    @property
    def filename(self):
        return self._filename

    @property
    def cv(self):
        return self._cv

    @property
    def experience(self):
        return self._experience

    def _load_experience(self):
        experience_df = pd.read_excel(self.filename, sheet_name="Experience")
        return [ExperienceData(row, self.cv) for _, row in experience_df.iterrows()]

    def __str__(self) -> str:
        string = ""
        for experience in self.experience:
            string += str(experience)
        return string

    def __repr__(self) -> str:
        string = f"Experience(experience={self.experience})"
        return string
