"""
This module contains the classes and methods to process the supervision data from the CV.
"""
import pandas as pd

from cvprocessor.education import Education


class SupervisionData:
    """
    The Supervision class is used to store the supervision data.

    Attributes:
    info (AcademicDetails): The academic details.
    institution (str): The institution.
    """

    def __init__(self):
        self.education = Education()
        self.students = str()
        self.supervisor_ids = str()
        self.type = str()

    def get_students(self):
        """
        Get the students.
        """
        return self.students

    def get_supervisor_ids(self):
        """
        Get the supervisor IDs.
        """
        return self.supervisor_ids

    def get_type(self):
        """
        Get the type.
        """
        return self.type

    def load(self, df):
        """
        Load the supervision data.
        """
        self.education.load(df)
        self.students = df["Students"]
        self.supervisor_ids = df["Supervisor ids"]
        self.type = df["Type"]


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

    def get_types_ordered(self):
        """
        Get the supervision types in order.
        """
        supervision_types = []
        for supervision in self.supervisions:
            if supervision.type not in supervision_types:
                supervision_types.append(supervision.type)
        return supervision_types

    def get_num_by_type(self, supervision_type):
        """
        Get the number of supervision by document type.
        """
        count = 0
        for supervision in self.supervisions:
            if supervision.type == supervision_type:
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
            self.supervisions, key=lambda x: (x.type, x.education.dates.get_end()), reverse=True)

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
