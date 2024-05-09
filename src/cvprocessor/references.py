import pandas as pd


class ReferenceData:
    def __init__(self, filename):
        self._filename = filename
        self._name = None
        self._email = None
        self._position = None
        self._institution = None
        self._load_reference()

    @property
    def filename(self):
        return self._filename

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def position(self):
        return self._position

    @property
    def institution(self):
        return self._institution

    def _load_reference(self):
        self._name = self.filename["Name"]
        self._email = self.filename["Email"]
        self._position = self.filename["Position"]
        self._institution = self.filename["Institution"]

    def __str__(self):
        string = f"Name: {self.name}\n"
        string += f"Email: {self.email}\n"
        string += f"Position: {self.position}\n"
        string += f"Institution: {self.institution}\n\n"
        return string

    def __repr__(self):
        return f"ReferenceData({self.name}, {self.email}, {self.position}, {self.institution})\n"


class References:
    def __init__(self, filename):
        self._filename = filename
        self._references = self._load_references()

    @property
    def filename(self):
        return self._filename

    @property
    def references(self):
        return self._references

    def _load_references(self):
        reference_df = pd.read_excel(self.filename, sheet_name="References")
        return [ReferenceData(row) for _, row in reference_df.iterrows()]

    def __str__(self):
        string = ""
        for reference in self.references:
            string += str(reference)
        return string

    def __repr__(self):
        return f"References({self.references})\n"
