"""
This module contains the ExperienceData and Experience classes.
"""
import pandas as pd
from cvprocessor.date.date import Dates


class ExperienceData:
    """
    The ExperienceData class is used to store the experience data.

    Attributes:
    date (Dates): The date of the experience.
    position (str): The position of the experience.
    institution (str): The institution of the experience.
    description (str): The description of the experience.
    responsibilities (str): The responsibilities of the experience.
    """

    def __init__(self):
        self.dates = Dates()
        self.position = str()
        self.institution_id = int()
        self.description = str()
        self.responsibilities = str()

    def get_position(self):
        """
        Get the position of this experience.
        """
        return self.position

    def get_institution_id(self):
        """
        Get the institution id of this experience.
        """
        return self.institution_id

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

    def load(self, filename):
        """
        Load the experience data.
        """
        self.dates.load(filename)
        self.position = filename["Position"]
        self.institution_id = filename["Institution id"]
        self.description = filename["Description"]
        self.responsibilities = filename["Responsibilities"]

    def __repr__(self) -> str:
        string = (
            f"ExperienceData("
            f"dates={repr(self.dates)}, "
            f"position={self.position}, "
            f"institution id={self.institution_id}, "
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

    def get_num_experiences(self):
        """
        Get the number of experiences.
        """
        return len(self.experiences)

    def load(self, filename):
        """
        Load the experience data.
        """
        experience_df = pd.read_excel(filename, sheet_name="Experience")
        for _, row in experience_df.iterrows():
            self.experiences.append(ExperienceData())
            self.experiences[-1].load(row)
        self.experiences = sorted(
            self.experiences, key=lambda x: x.dates.get_end(), reverse=True)

    def __repr__(self) -> str:
        string = f"Experience(experience={repr(self.experiences)})"
        return string

    def __iter__(self):
        return iter(self.experiences)
