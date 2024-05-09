import pandas as pd


class MembershipData:
    def __init__(self, filename):
        self._filename = filename
        self._year = None
        self._membership = None
        self._load_membership()

    @property
    def filename(self):
        return self._filename

    @property
    def year(self):
        return self._year

    @property
    def membership(self):
        return self._membership

    def _load_membership(self):
        self._year = self.filename["Year"]
        self._membership = self.filename["Membership"]

    def __str__(self):
        string = f"Year: {self.year}\n"
        string += f"Membership: {self.membership}\n\n"
        return string

    def __repr__(self):
        return f"MembershipData({self.year}, {self.membership})\n"


class Memberships:
    def __init__(self, filename):
        self._filename = filename
        self._memberships = self._load_memberships()

    @property
    def filename(self):
        return self._filename

    @property
    def memberships(self):
        return self._memberships

    def _load_memberships(self):
        membership_df = pd.read_excel(
            self.filename, sheet_name="Professional_memberships")
        return [MembershipData(row) for _, row in membership_df.iterrows()]

    def __str__(self):
        string = ""
        for membership in self.memberships:
            string += str(membership)
        return string

    def __repr__(self):
        return f"Memberships(filename={self.filename}, memberships={self.memberships})\n"
