import pandas as pd


class AuthorsData:
    def __init__(self, filename):
        self._filename = filename
        self._id = None
        self._name = None
        self._lastname = None
        self._alias_long = None
        self._alias_short = None
        self._job_title = None
        self._website = None
        self._affiliations_ids = None
        self._fingerprint = None
        self._public_key = None
        self._email = None
        self._linkedin = None
        self._github = None
        self._google_scholar = None
        self._orcid = None
        self._research_gate = None
        self._address = None
        self._location = None
        self._telephone = None
        self._load_authors()

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
    def lastname(self):
        return self._lastname

    @property
    def alias_long(self):
        return self._alias_long

    @property
    def alias_short(self):
        return self._alias_short

    @property
    def job_title(self):
        return self._job_title

    @property
    def website(self):
        return self._website

    @property
    def affiliation_ids(self):
        return self._affiliations_ids

    @property
    def fingerprint(self):
        return self._fingerprint

    @property
    def public_key(self):
        return self._public_key

    @property
    def email(self):
        return self._email

    @property
    def linkedin(self):
        return self._linkedin

    @property
    def github(self):
        return self._github

    @property
    def google_scholar(self):
        return self._google_scholar

    @property
    def orcid(self):
        return self._orcid

    @property
    def research_gate(self):
        return self._research_gate

    @property
    def address(self):
        return self._address

    @property
    def location(self):
        return self._location

    @property
    def telephone(self):
        return self._telephone

    def _load_authors(self):
        self._id = self.filename["ID"]
        self._name = self.filename["Name"]
        self._lastname = self.filename["Lastname"]
        self._alias_long = self.filename["Alias Long"]
        self._alias_short = self.filename["Alias Short"]
        self._job_title = self.filename["Job Title"]
        self._website = self.filename["Website"]
        # if self.filename["Affiliations"] is a list of ids, then split it
        if isinstance(self.filename["Affiliations"], list):
            self._affiliations_ids = self.filename["Affiliations"].split(",")
        else:
            self._affiliations_ids = self.filename["Affiliations"]
        self._fingerprint = self.filename["Fingerprint"]
        self._public_key = self.filename["Public Key"]
        self._email = self.filename["Email"]
        self._linkedin = self.filename["LinkedIn"]
        self._github = self.filename["GitHub"]
        self._google_scholar = self.filename["Google Scholar"]
        self._orcid = self.filename["ORCID"]
        self._research_gate = self.filename["ResearchGate"]
        self._address = self.filename["Address"]
        self._location = self.filename["Location"]
        self._telephone = self.filename["Telephone"]

    def print(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Lastname: {self.lastname}")
        print(f"Alias Long: {self.alias_long}")
        print(f"Alias Short: {self.alias_short}")
        print(f"Job Title: {self.job_title}")
        print(f"Website: {self.website}")
        print(f"Fingerprint: {self.fingerprint}")
        print(f"Public Key: {self.public_key}")
        print(f"Email: {self.email}")
        print(f"LinkedIn: {self.linkedin}")
        print(f"GitHub: {self.github}")
        print(f"Google Scholar: {self.google_scholar}")
        print(f"ORCID: {self.orcid}")
        print(f"ResearchGate: {self.research_gate}")
        print(f"Address: {self.address}")
        print(f"Location: {self.location}")
        print(f"Telephone: {self.telephone}")
        print("\n")


class Authors:
    def __init__(self, filename,):
        self._filename = filename
        self._authors = self._load_authors()

    @property
    def filename(self):
        return self._filename

    @property
    def authors(self):
        return self._authors

    def get_author(self, author_id):
        for author in self.authors:
            if author.id == author_id:
                return author
        return None

    def _load_authors(self):
        authors_df = pd.read_excel(self.filename, sheet_name="Authors")
        return [AuthorsData(row) for _, row in authors_df.iterrows()]

    def print(self):
        for author in self.authors:
            author.print()
