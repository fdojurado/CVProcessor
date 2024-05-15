"""
This module contains the ExperienceData and Experience classes.
"""
import pandas as pd
from cvprocessor import year_data as yd


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
        return yd.get_start_year(self.years)

    def get_end_year(self):
        """
        Get the end year of this experience.
        """
        return yd.get_end_year(self.years)

    def get_position(self):
        """
        Get the position of this experience.
        """
        return self.position

    def get_institution(self):
        """
        Get the institution of this experience.
        """
        return self.institution

    def get_description(self):
        """
        Get the description of this experience.
        """
        return self.description

    def get_responsibilities(self):
        """
        Get the responsibilities of this experience.
        """
        return self.responsibilities

    def process_year_data(self, filename):
        """
        Process the year data.
        """
        self.years = yd.process_year_data(filename, self.years)

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

    def __iter__(self):
        return iter(self.experiences)
