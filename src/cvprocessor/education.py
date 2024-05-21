"""
This module contains the classes to represent the education data of an author.
"""
import pandas as pd
from cvprocessor.date.date import Dates
from cvprocessor.links.links import Links


class Education:
    """
    A class to represent the education data of an author.
    """

    def __init__(self):
        self.degree = str()
        self.institution_id = int()
        self.award = str()
        self.dates = Dates()
        self.thesis = str()
        self.links = Links()
        self.advisor_ids: list[int] = []

    def get_degree(self):
        """
        Get the degree.
        """
        return self.degree

    def get_institution_id(self):
        """
        Get the institution.
        """
        return self.institution_id

    def get_award(self):
        """
        Get the award.
        """
        return self.award

    def get_thesis(self):
        """
        Get the thesis.
        """
        return self.thesis

    def get_advisor_ids(self):
        """
        Get the advisor IDs.
        """
        return self.advisor_ids

    def load(self, filename):
        """
        Load the education data from the filename.
        """
        if "Degree" in filename:
            self.degree = filename["Degree"]
        if "Institution id" in filename:
            self.institution_id = filename["Institution id"]
        if "Award" in filename:
            self.award = filename["Award"]
        self.dates.load(filename)
        if "Thesis" in filename:
            self.thesis = filename["Thesis"]
        self.links.load(filename)
        if "Advisor ids" in filename:
            self.advisor_ids = filename["Advisor ids"].split(",")
            self.advisor_ids = [int(advisor_id)
                                for advisor_id in self.advisor_ids]

    def __repr__(self) -> str:
        string = (
            f"EducationData("
            f"degree={self.degree}, "
            f"institution id={self.institution_id}, "
            f"award={self.award}, "
            f"dates={repr(self.dates)}, "
            f"thesis={self.thesis}, "
            f"links={repr(self.links)}, "
            f"thesis_advisor={self.advisor_ids})"
        )
        return string


class Educations:
    """
    A class to represent the education data of an author.

    Attributes:
    educations (list): The list of education data.
    """

    def __init__(self):
        self.educations = []

    def get_oldest_end_date(self):
        """
        Gets the oldest end date of the education data.
        """
        return self.educations[-1].dates.get_end()

    def load(self, filename):
        """
        Load the education data.
        """
        education_df = pd.read_excel(filename, sheet_name="Education")
        for _, row in education_df.iterrows():
            self.educations.append(Education())
            self.educations[-1].load(row)
        self.educations = sorted(
            self.educations, key=lambda x: x.dates.get_end(), reverse=True)

    def __repr__(self) -> str:
        string = f"Education(educations={repr(self.educations)})"
        return string

    def __iter__(self):
        return iter(self.educations)
