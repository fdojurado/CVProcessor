"""
This module contains the classes to represent the education data of an author.
"""
import pandas as pd
from cvprocessor import year_data as yd


class ThesisInfo:
    """
    A class to represent the thesis information of an author.

    Attributes:
    thesis: The thesis.
    thesis_link: The thesis link.
    advisor: The advisor.

    Methods:
    __str__: Returns the string representation of the thesis information.
    __repr__: Returns the string representation of the thesis information.
    """

    def __init__(self):
        self.thesis = None
        self.thesis_link = None
        self.advisor = None

    def get_thesis(self):
        """
        Get the thesis.
        """
        return self.thesis

    def get_thesis_link(self):
        """
        Get the thesis link.
        """
        return self.thesis_link

    def get_advisor(self):
        """
        Get the advisor.
        """
        return self.advisor

    def load(self, filename):
        """
        Load the thesis information.
        """
        self.thesis = filename["Thesis"]
        self.thesis_link = filename["Thesis link"]
        self.advisor = filename["Advisor"]

    def __str__(self):
        string = f"Thesis: {self.thesis}\n"
        string += f"Thesis link: {self.thesis_link}\n"
        string += f"Advisor: {self.advisor}\n"
        return string

    def __repr__(self):
        string = (
            f"ThesisInfo("
            f"thesis={self.thesis}, "
            f"thesis_link={self.thesis_link}, "
            f"advisor={self.advisor})"
        )
        return string


class EducationData:
    """
    A class to represent the education data of an author.
    """

    def __init__(self):
        self.degree = str()
        self.award = str()
        self.institution = str()
        self.education_period = []
        self.thesis_info = ThesisInfo()

    def get_degree(self):
        """
        Get the degree.
        """
        return self.degree

    def get_institution(self):
        """
        Get the institution.
        """
        return self.institution

    def get_award(self):
        """
        Get the award.
        """
        return self.award

    def get_start_year(self):
        """
        Get the start year of this experience.
        """
        return yd.get_start_year(self.education_period)

    def get_end_year(self):
        """
        Get the end year of this experience.
        """
        return yd.get_end_year(self.education_period)

    def process_year_data(self, filename):
        """
        Process the year data.
        """
        self.education_period = yd.process_year_data(
            filename, self.education_period)

    def load(self, filename):
        """
        Load the education data from the filename.
        """
        self.degree = filename["Degree"]
        self.award = filename["Award"]
        self.institution = filename["Institution"]
        self.process_year_data(filename)
        self.thesis_info.load(filename)

    def __str__(self):
        string = f"Degree: {self.degree}\n"
        string += f"Award: {self.award}\n"
        string += f"Institution: {self.institution}\n"
        string += str(self.education_period)
        string += str(self.thesis_info)
        return string

    def __repr__(self) -> str:
        string = (
            f"EducationData("
            f"degree={repr(self.degree)}, "
            f"award={repr(self.award)}, "
            f"institution={repr(self.institution)}, "
            f"education_period={repr(self.education_period)}, "
            f"thesis_info={repr(self.thesis_info)})"
        )
        return string


class Education:
    """
    A class to represent the education data of an author.

    Attributes:
    educations (list): The list of education data.
    """

    def __init__(self):
        self.educations = []

    # Get the oldest end year
    def get_oldest_end_year(self):
        """
        Gets the oldest end year of the education data.
        """
        return self.educations[-1].education_period.end_year

    def load(self, filename):
        """
        Load the education data.
        """
        education_df = pd.read_excel(filename, sheet_name="Education")
        for _, row in education_df.iterrows():
            self.educations.append(EducationData())
            self.educations[-1].load(row)
        # sort the education data by end year
        self.educations = sorted(
            self.educations, key=lambda x: x.get_end_year(), reverse=True)

    def __str__(self) -> str:
        string = ""
        for education in self.educations:
            string += str(education) + "\n"
        return string

    def __repr__(self) -> str:
        string = f"Education(educations={repr(self.educations)})"
        return string

    def __iter__(self):
        return iter(self.educations)
