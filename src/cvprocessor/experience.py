"""
This module contains the ExperienceData and Experience classes.
"""
import pandas as pd


class YearData:
    """
    A class to represent the year data.

    Attributes:
    year_range (str): The year range.
    start_year (datetime): The start year.
    end_year (datetime): The end year.
    """

    def __init__(self):
        self.year_range = str()
        self.start_year = None
        self.end_year = None

    def format_year(self, year):
        """
        Format the year to a datetime object.
        """
        year = year.strip()
        year = pd.to_datetime(year, format="%b %Y")
        return year

    def process_year_range(self):
        """
        Process the year range.
        """
        year_range = self.year_range.split("-")
        self.start_year = self.format_year(year_range[0])
        self.start_year = pd.to_datetime(self.start_year, format="%b %Y")
        if len(year_range) > 1:
            self.end_year = self.format_year(year_range[1])
            self.end_year = pd.to_datetime(self.end_year, format="%b %Y")
        else:
            self.end_year = None

    def __str__(self):
        string = f"Year range: {self.year_range}\n"
        string += f"Start year: {self.start_year}\n"
        string += f"End year: {self.end_year}\n"
        return string

    def __repr__(self):
        string = (
            f"YearData("
            f"year_range={self.year_range}, "
            f"start_year={self.start_year}, "
            f"end_year={self.end_year})"
        )
        return string


class ExperienceData:
    """
    The ExperienceData class is used to store the experience data.

    Attributes:
    year (YearData): The year of the experience.
    position (str): The position of the experience.
    institution (str): The institution of the experience.
    description (str): The description of the experience.
    responsibilities (str): The responsibilities of the experience.
    """

    def __init__(self):
        self.years = []
        self.position = None
        self.institution = None
        self.description = None
        self.responsibilities = None

    def get_start_year(self):
        """
        Get the start year of this experience.
        """
        min_year = 1e6
        date = None
        for year in self.years:
            if int(year.start_year.year) < min_year:
                min_year = int(year.start_year.year)
                date = year.start_year
        return date

    def get_end_year(self):
        """
        Get the end year of this experience.
        """
        max_year = -1
        date = None
        for year in self.years:
            if year.end_year is not None:
                if int(year.end_year.year) > max_year:
                    max_year = int(year.end_year.year)
                    date = year.end_year
        return date

    def add_year(self, year):
        """
        Add a year to the experience.
        """
        assert isinstance(year, YearData)
        self.years.append(year)

    def sort_years(self):
        """
        Sort the years.
        """
        self.years = sorted(
            self.years, key=lambda x: x.start_year, reverse=True)

    def process_year_data(self, filename):
        """
        Process the year data.
        """
        year_range = filename["Year"].split(";")
        year_range = list(filter(None, year_range))
        for year in year_range:
            year_data = YearData()
            year_data.year_range = year
            year_data.process_year_range()
            self.add_year(year_data)
        self.sort_years()

    def load(self, filename):
        """
        Load the experience data.
        """
        self.process_year_data(filename)
        self.position = filename["Position"]
        self.institution = filename["Institution"]
        self.description = filename["Description"]
        self.responsibilities = filename["Responsibilities"]

    def __str__(self) -> str:
        string = f"Years: {list(map(str, self.years))}\n"
        string += f"Position: {self.position}\n"
        string += f"Institution: {self.institution}\n"
        string += f"Description: {self.description}\n"
        string += f"Responsibilities: {self.responsibilities}\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"ExperienceData("
            f"years={[repr(year) for year in self.years]}, "
            f"position={self.position}, "
            f"institution={self.institution}, "
            f"description={self.description}, "
            f"responsibilities={self.responsibilities})"
        )
        return string


class Experience:
    """
    The Experience class is used to store the experience data.

    Attributes:
    experience (list): The list of experience data.
    """

    def __init__(self):
        self.experiences = []

    def load(self, filename):
        """
        Load the experience data.
        """
        experience_df = pd.read_excel(filename, sheet_name="Experience")
        for _, row in experience_df.iterrows():
            self.experiences.append(ExperienceData())
            self.experiences[-1].load(row)
        self.experiences = sorted(
            self.experiences, key=lambda x: x.get_start_year(), reverse=True)

    def __str__(self) -> str:
        string = ""
        for experience in self.experiences:
            string += str(experience) + "\n"
        return string

    def __repr__(self) -> str:
        string = f"Experience(experience={repr(self.experiences)})"
        return string
