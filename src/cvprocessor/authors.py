import pandas as pd


class AuthorsData:
    def __init__(self, filename, affiliation):
        self._filename = filename
        self._id = None
        self._name = None
        self._lastname = None
        self._alias_long = None
        self._alias_short = None
        self._job_title = None
        self._website = None
        self._affiliation = affiliation
        self._fingerprint = None
        self._public_key = None
        self._email = None
        self._linkedin = None
        self._github = None
        self._google_scholar = None
        self._orcid = None
        self._researchgate = None
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
    def affiliation(self):
        return self._affiliation

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
    def researchgate(self):
        return self._researchgate

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
        self._id = int(self.filename["id"])
        self._name = self.filename["Name"]
        self._lastname = self.filename["Lastname"]
        self._alias_long = self.filename["Alias Long"]
        self._alias_short = self.filename["Alias Short"]
        self._job_title = self.filename["Job Title"]
        self._website = self.filename["Website"]
        self._fingerprint = self.filename["Fingerprint"]
        self._public_key = self.filename["Public Key"]
        self._email = self.filename["Email"]
        self._linkedin = self.filename["LinkedIn"]
        self._github = self.filename["GitHub"]
        self._google_scholar = self.filename["Google Scholar"]
        self._orcid = self.filename["ORCID"]
        self._researchgate = self.filename["ResearchGate"]
        self._address = self.filename["Address"]
        self._location = self.filename["Location"]
        self._telephone = self.filename["Telephone"]

    def __str__(self):
        string = f"id: {self.id}\n"
        string += f"Name: {self.name}\n"
        string += f"Lastname: {self.lastname}\n"
        string += f"Alias Long: {self.alias_long}\n"
        string += f"Alias Short: {self.alias_short}\n"
        string += f"Job Title: {self.job_title}\n"
        string += f"Website: {self.website}\n"
        string += f"Fingerprint: {self.fingerprint}\n"
        string += f"Public Key: {self.public_key}\n"
        string += f"Email: {self.email}\n"
        string += f"LinkedIn: {self.linkedin}\n"
        string += f"GitHub: {self.github}\n"
        string += f"Google Scholar: {self.google_scholar}\n"
        string += f"ORCID: {self.orcid}\n"
        string += f"ResearchGate: {self.researchgate}\n"
        string += f"Address: {self.address}\n"
        string += f"Location: {self.location}\n"
        string += f"Telephone: {self.telephone}\n"
        string += f"Affiliation: {self.affiliation.name}\n\n"
        return string

    def __repr__(self):
        repr = f"Author(id={self.id}, name={self.name}, lastname={self.lastname}, alias_long={self.alias_long}, alias_short={self.alias_short}, job_title={self.job_title}, website={self.website}, fingerprint={self.fingerprint}, public_key={self.public_key}, email={self.email}, linkedin={self.linkedin}, github={self.github}, google_scholar={self.google_scholar}, orcid={self.orcid}, researchgate={self.researchgate}, address={self.address}, location={self.location}, telephone={self.telephone}, affiliation={self.affiliation})\n"
        return repr


class Authors:
    def __init__(self, filename, cv):
        self._filename = filename
        self._cv = cv
        self._authors = self._load_authors()

    @property
    def filename(self):
        return self._filename

    @property
    def cv(self):
        return self._cv

    @property
    def authors(self):
        return self._authors

    def get_author(self, author_id, affiliation_id=None):
        if isinstance(author_id, str):
            author_id = int(author_id)
        if affiliation_id is None:
            for author in self.authors:
                if author.id == author_id:
                    return author
            return None
        for author in self.authors:
            if author.id == author_id and self.cv.institutes.get_institute(int(affiliation_id)).id == author.affiliation.id:
                return author
        return None

    def _load_authors(self):
        authors_df = pd.read_excel(self.filename, sheet_name="Authors")
        authors = []
        for index, row in authors_df.iterrows():
            if isinstance(row["Affiliations"], str) and ("," in row["Affiliations"] or ";" in row["Affiliations"]):
                affiliations = row["Affiliations"].split(",")
                for affiliation in affiliations:
                    affiliation = self.cv.institutes.get_institute(
                        int(affiliation))
                    author = AuthorsData(row, affiliation)
                    authors.append(author)
            else:
                affiliation = self.cv.institutes.get_institute(
                    int(row["Affiliations"]))
                author = AuthorsData(row, affiliation)
                authors.append(author)
        return authors

    def __str__(self):
        string = ""
        for author in self.authors:
            string += str(author)
        return string

    def __repr__(self):
        repr = f"Authors(filename={self.filename}, cv={self.cv}, authors={self.authors})\n"
        return repr
