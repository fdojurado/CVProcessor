"""
This module contains the classes to process the teaching data from the CV.
"""
import pandas as pd
from cvprocessor.education import Education


class TeachingData:
    """
    A class to represent the teaching data.

    Attributes:
    info (TeachingInfo): The teaching information.
    institution (str): The institution.
    supervisor (str): The supervisor.
    responsibilities (str): The responsibilities.
    """

    def __init__(self):
        self.education = Education()
        self.type = str()
        self.responsibilities = str()

    def get_responsibilities(self):
        """
        Get the responsibilities.
        """
        return self.responsibilities

    def get_type(self):
        """
        Get the type.
        """
        return self.type

    def load(self, filename):
        """
        Load the teaching data.
        """
        self.education.load(filename)
        self.responsibilities = filename["Responsibilities"]
        self.type = filename["Type"]

    def __repr__(self):
        string = (
            f"TeachingData("
            f"education={repr(self.education)}, "
            f"responsibilities={repr(self.responsibilities)})"
        )
        return string


class Teaching:
    """
    The Teaching class is used to store the teaching data.

    Attributes:
    teaching (list): The list of teaching data.
    """

    def __init__(self):
        self.teaching = []

    def get_type_ordered(self):
        """
        Get the teaching types in order.
        """
        teaching_type = []
        for teaching in self.teaching:
            if teaching.type not in teaching_type:
                teaching_type.append(teaching.type)
        return teaching_type

    def get_num_by_type(self, teaching_type):
        """
        Get the number of teaching by document type.
        """
        count = 0
        for teaching in self.teaching:
            if teaching.type == teaching_type:
                count += 1
        return count

    def load(self, filename):
        """
        Load the teaching data.
        """
        teaching_df = pd.read_excel(filename, sheet_name="Teaching")
        for _, row in teaching_df.iterrows():
            self.teaching.append(TeachingData())
            self.teaching[-1].load(row)
        self.teaching = sorted(
            self.teaching, key=lambda x: x.education.dates.get_end(), reverse=True)

    def __repr__(self):
        string = f"Teaching(teaching={repr(self.teaching)})"
        return string

    def __iter__(self):
        return iter(self.teaching)
