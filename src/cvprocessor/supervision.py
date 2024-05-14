"""
This module contains the classes and methods to process the supervision data from the CV.
"""
import pandas as pd


class SupervisionInfo:
    """
    A class to represent the information of a supervision.

    Attributes:
    students (list): The students of the supervision.
    year (int): The year of the supervision.
    title (str): The title of the supervision.
    program (str): The program of the supervision.
    type (str): The type of the supervision.
    """

    def __init__(self):
        self.students = str()
        self.year = str()
        self.title = str()
        self.program = str()
        self.type = str()

    def load(self, filename):
        """
        Load the supervision information.
        """
        self.students = filename["Students"]
        self.year = filename["Year"]
        self.title = filename["Title"]
        self.program = filename["Program"]
        self.type = filename["Type"]

    def __str__(self) -> str:
        string = f"Students: {self.students}\n"
        string += f"Year: {self.year}\n"
        string += f"Title: {self.title}\n"
        string += f"Program: {self.program}\n"
        string += f"Type: {self.type}\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"SupervisionInfo("
            f"students={self.students}, "
            f"year={self.year}, "
            f"title={self.title}, "
            f"program={self.program}, "
            f"type={self.type})"
        )
        return string


class SupervisionData:
    """
    A class to represent the data of a supervision.

    Attributes:
    info (SupervisionInfo): The information of the supervision.
    institution (str): The institution of the supervision.
    supervisors (list): The supervisors of the supervision.
    students (list): The students of the supervision.
    """

    def __init__(self):
        self.info = SupervisionInfo()
        self.institution = str()
        self.supervisors = str()
        self.students = str()

    def load(self, filename):
        """
        Load the supervision data.
        """
        self.info.load(filename)
        self.institution = filename["Institution"]
        self.supervisors = filename["Supervisors"]

    def __str__(self) -> str:
        string = str(self.info)
        string += f"Institution: {self.institution}\n"
        string += f"Supervisors: {self.supervisors}\n"
        string += f"Students: {self.students}\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"SupervisionData("
            f"info={repr(self.info)}, "
            f"institution={self.institution}, "
            f"supervisors={self.supervisors}, "
            f"students={self.students})"
        )
        return string


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
            if supervision.info.type not in supervision_types:
                supervision_types.append(supervision.info.type)
        return supervision_types

    def get_num_supervision_by_document_type(self, supervision_type):
        """
        Get the number of supervision by document type.
        """
        count = 0
        for supervision in self.supervisions:
            if supervision.info.type == supervision_type:
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
            self.supervisions, key=lambda x: (x.info.type, x.info.year), reverse=True)

    def __str__(self) -> str:
        string = ""
        for supervision in self.supervisions:
            string += str(supervision) + "\n"
        return string

    def __repr__(self) -> str:
        string = f"Supervision(supervision={repr(list(self.supervisions))})"
        return string
