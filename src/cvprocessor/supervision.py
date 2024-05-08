import pandas as pd


class SupervisionData:
    def __init__(self, filename, cv):
        self._filename = filename
        self._cv = cv
        self._students = None
        self._year = None
        self._title = None
        self._program = None
        self._type = None
        self._institution = None
        self._supervisors = None
        self._load_supervision()

    @property
    def filename(self):
        return self._filename

    @property
    def cv(self):
        return self._cv

    @property
    def students(self):
        return self._students

    @property
    def year(self):
        return self._year

    @property
    def title(self):
        return self._title

    @property
    def program(self):
        return self._program

    @property
    def type(self):
        return self._type

    @property
    def institution(self):
        return self._institution

    @property
    def supervisors(self):
        return self._supervisors

    def process_students(self):
        self._students = self.filename['Students'].split(",")

    def _load_supervision(self):
        self.process_students()
        self._year = self.filename["Year"]
        self._year = pd.to_datetime(self.year, format="%Y").year
        self._title = self.filename["Title"]
        self._program = self.filename["Program"]
        self._type = self.filename["Type"]
        self._institution = self.filename["Institution"]
        self._supervisors = self.filename["Supervisors"]

    def __str__(self) -> str:
        string = f"Students: {self.students}\n"
        string += f"Year: {self.year}\n"
        string += f"Title: {self.title}\n"
        string += f"Program: {self.program}\n"
        string += f"Type: {self.type}\n"
        institution = self.cv.institutes.get_institute(self.institution)
        string += f"Institution: {institution.name}\n"
        string += f"Supervisors: {self.supervisors}\n\n"
        return string

    def __repr__(self) -> str:
        string = f"SupervisionData(students={self.students}, year={self.year}, title={self.title}, program={self.program}, type={self.type}, institution={self.institution}, supervisors={self.supervisors})"
        return string


class Supervision:
    def __init__(self, filename, cv):
        self._filename = filename
        self._cv = cv
        self._supervision = self._load_supervision()
        # Sort the supervision by type then by year
        self._supervision = sorted(
            self._supervision, key=lambda x: (x.type, x.year), reverse=True)

    @property
    def filename(self):
        return self._filename

    @property
    def cv(self):
        return self._cv

    @property
    def supervision(self):
        return self._supervision

    def get_supervision_types_ordered(self):
        supervision_types = []
        for supervision in self.supervision:
            if supervision.type not in supervision_types:
                supervision_types.append(supervision.type)
        return supervision_types

    def get_num_supervision_by_document_type(self, supervision_type):
        count = 0
        for supervision in self.supervision:
            if supervision.type == supervision_type:
                count += 1
        return count

    def _load_supervision(self):
        supervision_df = pd.read_excel(self.filename, sheet_name="Supervision")
        return [SupervisionData(row, self.cv) for _, row in supervision_df.iterrows()]

    def __str__(self) -> str:
        string = ""
        for supervision in self.supervision:
            string += str(supervision)
        return string

    def __repr__(self) -> str:
        string = f"Supervision(filename={self.filename}, supervision={self.supervision})"
        return string
