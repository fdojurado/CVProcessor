"""
This module contains the classes and methods to process the supervision data from the CV.
"""
import pandas as pd


class AcademicDetails:
    """
    The AcademicDetails class is used to store the academic details.

    Attributes:
    year (str): The year.
    title (str): The title.
    program (str): The program.
    type (str): The type.
    """

    def __init__(self):
        self.year = str()
        self.title = str()
        self.program = str()
        self.type = str()

    def get_year(self):
        """
        Get the year.
        """
        return self.year

    def get_title(self):
        """
        Get the title.
        """
        return self.title

    def get_program(self):
        """
        Get the program.
        """
        return self.program

    def get_type(self):
        """
        Get the type.
        """
        return self.type

    def load(self, filename):
        """
        Load the academic details.
        """
        self.year = filename["Year"]
        self.title = filename["Title"]
        self.program = filename["Program"]
        self.type = filename["Type"]

    def __repr__(self) -> str:
        return (
            f"AcademicDetails("
            f"year={self.year}, "
            f"title={self.title}, "
            f"program={self.program}, "
            f"type={self.type})"
        )


class SupervisionDetails:
    """
    The SupervisionDetails class is used to store the supervision details.

    Attributes:
    institution (str): The institution.
    supervisors (str): The supervisors.
    students (str): The students.
    """

    def __init__(self):
        self.institution = str()
        self.supervisors = str()
        self.students = str()

    def get_institution(self):
        """
        Get the institution.
        """
        return self.institution

    def get_supervisors(self):
        """
        Get the supervisors.
        """
        return self.supervisors

    def get_students(self):
        """
        Get the students.
        """
        return self.students

    def load(self, filename):
        """
        Load the supervision details.
        """
        self.institution = filename["Institution"]
        self.supervisors = filename["Supervisors"]
        self.students = filename["Students"]

    def __repr__(self) -> str:
        return (
            f"SupervisionDetails("
            f"institution={self.institution}, "
            f"supervisors={self.supervisors}, "
            f"students={self.students})"
        )


class SupervisionData:
    """
    The Supervision class is used to store the supervision data.

    Attributes:
    info (AcademicDetails): The academic details.
    institution (str): The institution.
    """

    def __init__(self):
        self.academic = AcademicDetails()
        self.supervision = SupervisionDetails()

    def load(self, filename):
        """
        Load the supervision data.
        """
        self.academic.load(filename)
        self.supervision.load(filename)

    def __repr__(self) -> str:
        return (
            f"SupervisionData("
            f"info={repr(self.academic)}, "
            f"institution={self.supervision.institution})"
        )


class Supervision:
    """
    A class to represent the supervision data.

    Attributes:
    supervision (list): The list of supervision data.

    Methods:
    get_supervision_types_ordered: Get the supervision types in order.
    get_num_supervision_by_document_type: Get the number of supervision by document type.
    load: Load the supervision data.
    """

    def __init__(self):
        self.supervisions = []

    def get_supervision_types_ordered(self):
        """
        Get the supervision types in order.
        """
        supervision_types = []
        for supervision in self.supervisions:
            if supervision.academic.type not in supervision_types:
                supervision_types.append(supervision.academic.type)
        return supervision_types

    def get_num_supervision_by_document_type(self, supervision_type):
        """
        Get the number of supervision by document type.
        """
        count = 0
        for supervision in self.supervisions:
            if supervision.academic.type == supervision_type:
                count += 1
        return count

    def load(self, filename):
        """
        Load the supervision data.
        """
        supervision_df = pd.read_excel(filename, sheet_name="Supervision")
        for _, row in supervision_df.iterrows():
            supervision_data = SupervisionData()
            supervision_data.load(row)
            self.supervisions.append(supervision_data)
        # sort the supervision data by type and year
        self.supervisions = sorted(
            self.supervisions, key=lambda x: (x.academic.type, x.academic.year), reverse=True)

    def __str__(self) -> str:
        string = ""
        for supervision in self.supervisions:
            string += str(supervision) + "\n"
        return string

    def __repr__(self) -> str:
        string = f"Supervision(supervision={repr(list(self.supervisions))})"
        return string

    def __iter__(self):
        return iter(self.supervisions)
