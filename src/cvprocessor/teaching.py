"""
This module contains the classes to process the teaching data from the CV.
"""
import pandas as pd
from cvprocessor import common


class TeachingInfo:
    """
    A class to represent the teaching information.

    Attributes:
    year (list): The years range of the teaching.
    position (str): The position.
    course (str): The course.
    link (str): The link.
    type (str): The type.
    """

    def __init__(self):
        self.years = []
        self.position = str()
        self.course = str()
        self.link = str()
        self.type = str()

    def get_start_year(self):
        """
        Get the start year of the teaching.
        """
        return common.get_start_year(self.years)

    def get_end_year(self):
        """
        Get the end year of the teaching.
        """
        return common.get_end_year(self.years)

    def get_position(self):
        """
        Get the position of the teaching.
        """
        return self.position

    def get_course(self):
        """
        Get the course of the teaching.
        """
        return self.course

    def get_link(self):
        """
        Get the link of the teaching.
        """
        return self.link

    def get_type(self):
        """
        Get the type of the teaching.
        """
        return self.type

    def add_year(self, year):
        """
        Add a year to the year list.
        """
        assert isinstance(year, common.YearData)
        self.years.append(year)

    def sort_years(self):
        """
        Sort the years by start year.
        """
        self.years = sorted(
            self.years, key=lambda x: x.start_year, reverse=True)

    def __str__(self):
        string = f"Year: {list(map(str, self.years))}\n"
        string += f"Position: {self.position}\n"
        string += f"Course: {self.course}\n"
        string += f"Link: {self.link}\n"
        string += f"Type: {self.type}\n"
        return string

    def __repr__(self):
        string = (
            f"TeachingInfo("
            f"year={[repr(year) for year in self.years]}, "
            f"position={self.position}, "
            f"course={self.course}, "
            f"link={self.link}, "
            f"type={self.type})"
        )
        return string


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
        self.info = TeachingInfo()
        self.institution = str()
        self.supervisor = str()
        self.responsibilities = str()

    def get_start_year(self):
        """
        Get the start year of this teaching activity.
        """
        return self.info.get_start_year()

    def get_end_year(self):
        """
        Get the end year of this teaching activity.
        """
        return self.info.get_end_year()

    def process_year_data(self, filename):
        """
        Process the year data.
        """
        year_range = filename["Year"].split(";")
        year_range = list(filter(None, year_range))
        for year in year_range:
            year_data = common.YearData()
            year_data.year_range = year
            year_data.process_year_range(year)
            self.info.add_year(year_data)
        self.info.sort_years()

    def load(self, filename):
        """
        Load the teaching data.
        """
        self.process_year_data(filename)
        self.info.position = filename["Position"]
        self.info.course = filename["Course"]
        self.info.link = filename["Link"]
        self.info.type = filename["Type"]
        self.institution = filename["Institution"]
        self.supervisor = filename["Supervisor"]
        self.responsibilities = filename["Responsibilities"]

    def __str__(self):
        string = str(self.info)
        string += f"Institution: {self.institution}\n"
        string += f"Supervisor: {self.supervisor}\n"
        string += f"Responsibilities: {self.responsibilities}\n"
        return string

    def __repr__(self):
        string = (
            f"TeachingData("
            f"info={repr(self.info)}, "
            f"institution={self.institution}, "
            f"supervisor={self.supervisor}, "
            f"responsibilities={self.responsibilities})"
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

    def get_teaching_type_ordered(self):
        """
        Get the teaching types in order.
        """
        teaching_type = []
        for teaching in self.teaching:
            if teaching.info.type not in teaching_type:
                teaching_type.append(teaching.info.type)
        return teaching_type

    def get_num_teaching_by_document_type(self, teaching_type):
        """
        Get the number of teaching by document type.
        """
        count = 0
        for teaching in self.teaching:
            if teaching.info.type == teaching_type:
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

    def __str__(self):
        string = ""
        for teaching in self.teaching:
            string += str(teaching) + "\n"
        return string

    def __repr__(self):
        string = f"Teaching(teaching={repr(self.teaching)})"
        return string

    def __iter__(self):
        return iter(self.teaching)
