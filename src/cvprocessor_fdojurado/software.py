import pandas as pd


class SofwareData:
    def __init__(self, filename):
        self._filename = filename
        self._id = None
        self._name = None
        self._version = None
        self._description = None
        self._repository = None
        self._demo = None
        self._website = None
        self._summary = None
        self._license = None
        self._load_software()

    @property
    def filename(self):
        return self._filename

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def description(self):
        return self._description

    @property
    def repository(self):
        return self._repository

    @property
    def demo(self):
        return self._demo

    @property
    def website(self):
        return self._website

    @property
    def summary(self):
        return self._summary

    @property
    def license(self):
        return self._license

    # @property
    # def doi(self):
    #     return self._doi

    def _load_software(self):
        self._id = self.filename["id"]
        self._name = self.filename["Name"]
        self._version = self.filename["Version"]
        self._description = self.filename["Description"]
        self._repository = self.filename["Repository"]
        self._demo = self.filename["Demo"]
        self._website = self.filename["Website"]
        self._summary = self.filename["Summary"]
        self._license = self.filename["License"]

    def print(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Version: {self.version}")
        print(f"Description: {self.description}")
        print(f"repository: {self.repository}")
        print(f"Demo: {self.demo}")
        print(f"Website: {self.website}")
        print(f"Summary: {self.summary}")
        print(f"License: {self.license}")
        print("\n")


class Software:
    def __init__(self, filename):
        self._filename = filename
        self._software = self._load_software()

    @property
    def filename(self):
        return self._filename

    @property
    def software(self):
        return self._software

    def get_software(self, software_id):
        if not software_id:
            return None
        if isinstance(software_id, str):
            software_id = int(software_id)
        for software in self.software:
            if software.id == software_id:
                return software
        return None

    def get_software_alphabetically(self):
        return sorted(self.software, key=lambda x: x.name)

    def _load_software(self):
        software_df = pd.read_excel(self.filename, sheet_name="Software")
        return [SofwareData(software) for index, software in software_df.iterrows()]

    def print(self):
        for software in self.software:
            software.print()
