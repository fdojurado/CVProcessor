"""
This module contains the classes to represent the education data of an author.
"""
import pandas as pd


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


class EducationPeriod:
    """
    A class to represent the education period of an author.

    Attributes:
    year: The year.
    start_year: The start year.
    end_year: The end year.

    Methods:
    __str__: Returns the string representation of the education period.
    __repr__: Returns the string representation of the education period.
    """

    def __init__(self):
        self.start_year = None
        self.end_year = None
        self.year = None

    def load(self, filename):
        """
        Load the education period.
        """
        years = filename["Year"]
        years = years.split(";")
        years = list(filter(None, years))
        self.year = years[0]
        start_year = years[0].split("-")[0].strip()
        end_year = years[-1].split("-")[-1].strip()
        if len(start_year.split()) == 2:
            start_year = '1 '+start_year
        if len(end_year.split()) == 2:
            end_year = "1 "+end_year
        self.start_year = pd.to_datetime(
            start_year, format="%d %b %Y")
        self.end_year = pd.to_datetime(
            end_year, format="%d %b %Y")

    def __str__(self):
        string = f"Year: {self.year}\n"
        string += f"Start year: {self.start_year}\n"
        string += f"End year: {self.end_year}\n"
        return string

    def __repr__(self):
        string = (
            f"EducationPeriod("
            f"year={self.year}, "
            f"start_year={self.start_year}, "
            f"end_year={self.end_year})"
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
        self.education_period = EducationPeriod()
        self.thesis_info = ThesisInfo()

    def load(self, filename):
        """
        Load the education data from the filename.
        """
        self.degree = filename["Degree"]
        self.award = filename["Award"]
        self.institution = filename["Institution"]
        self.education_period.load(filename)
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
            self.educations, key=lambda x: x.education_period.end_year, reverse=True)

    def __str__(self) -> str:
        string = ""
        for education in self.educations:
            string += str(education) + "\n"
        return string

    def __repr__(self) -> str:
        string = f"Education(educations={repr(self.educations)})"
        return string
