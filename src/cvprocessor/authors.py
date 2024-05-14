"""
    Authors module.

    This module contains the classes to represent the authors of the CV.

    Classes:
    AuthorsData: A class to represent an author.
    Authors: A class to represent a list of authors.
"""
import pandas as pd


class ContactInfo:
    """
    A class to represent the contact information of an author.
    """

    def __init__(self):
        self.email = str()
        self.telephone = str()
        self.website = str()
        self.address = str()
        self.location = str()

    def load(self, filename):
        """
        Loads the contact information of the author.
        """
        self.email = filename["Email"]
        self.telephone = filename["Telephone"]
        self.website = filename["Website"]
        self.address = filename["Address"]
        self.location = filename["Location"]

    def __repr__(self):
        string = (
            f"ContactInfo("
            f"email={self.email}, "
            f"telephone={self.telephone}, "
            f"website={self.website}, "
            f"address={self.address}, "
            f"location={self.location})"
        )
        return string

    def __str__(self):
        string = f"Email: {self.email}\n"
        string += f"Telephone: {self.telephone}\n"
        string += f"Website: {self.website}\n"
        string += f"Address: {self.address}\n"
        string += f"Location: {self.location}\n"
        return string


class ResearchInfo:
    """
    A class to represent the research information of an author.
    """

    def __init__(self):
        self.linkedin = str()
        self.github = str()
        self.google_scholar = str()
        self.orcid = str()
        self.researchgate = str()

    def load(self, filename):
        """
        Loads the research information of the author.
        """
        self.linkedin = filename["LinkedIn"]
        self.github = filename["GitHub"]
        self.google_scholar = filename["Google Scholar"]
        self.orcid = filename["ORCID"]
        self.researchgate = filename["ResearchGate"]

    def __repr__(self):
        string = (
            f"ResearchInfo("
            f"linkedin={self.linkedin}, "
            f"github={self.github}, "
            f"google_scholar={self.google_scholar}, "
            f"orcid={self.orcid}, "
            f"researchgate={self.researchgate})"
        )
        return string

    def __str__(self):
        string = f"LinkedIn: {self.linkedin}\n"
        string += f"GitHub: {self.github}\n"
        string += f"Google Scholar: {self.google_scholar}\n"
        string += f"ORCID: {self.orcid}\n"
        string += f"ResearchGate: {self.researchgate}\n"
        return string


class PersonalInfo:
    """
    A class to represent the personal information of an author.
    """

    def __init__(self):
        self.name = str()
        self.lastname = str()
        self.alias_long = str()
        self.alias_short = str()
        self.job_title = str()
        self.fingerprint = str()
        self.public_key = str()

    def load(self, filename):
        """
        Loads the personal information of the author.
        """
        self.name = filename["Name"]
        self.lastname = filename["Lastname"]
        self.alias_long = filename["Alias Long"]
        self.alias_short = filename["Alias Short"]
        self.job_title = filename["Job Title"]
        self.fingerprint = filename["Fingerprint"]
        self.public_key = filename["Public Key"]

    def __repr__(self):
        string = (
            f"AuthorPersonalInfo("
            f"name={self.name}, "
            f"lastname={self.lastname}, "
            f"alias_long={self.alias_long}, "
            f"alias_short={self.alias_short}, "
            f"job_title={self.job_title}, "
            f"fingerprint={self.fingerprint}, "
            f"public_key={self.public_key})"
        )
        return string

    def __str__(self):
        string = f"Name: {self.name}\n"
        string += f"Lastname: {self.lastname}\n"
        string += f"Alias Long: {self.alias_long}\n"
        string += f"Alias Short: {self.alias_short}\n"
        string += f"Job Title: {self.job_title}\n"
        string += f"Fingerprint: {self.fingerprint}\n"
        string += f"Public Key: {self.public_key}\n"
        return string


class AuthorsData:
    """
    A class to represent an author.

    Attributes:
    id (int): The ID of the author.
    affiliations (list): The affiliations of the author.
    personal_info (PersonalInfo): The personal information of the author.
    contact_info (ContactInfo): The contact information of the author.
    research_info (ResearchInfo): The research information of the author.

    Methods:
    load(filename): Loads the author data from the file.
    __str__(): Returns a string representation of the author.
    __repr__(): Returns a string representation of the author.
    """

    def __init__(self):
        self.id = int()
        self.affiliations = []
        self.personal_info = PersonalInfo()
        self.contact_info = ContactInfo()
        self.research_info = ResearchInfo()

    def load(self, filename):
        """
        Loads the author data from the file.
        """
        self.id = filename["id"]
        if isinstance(filename["Affiliations"], str) and\
                ("," in filename["Affiliations"] or ";" in filename["Affiliations"]):
            affiliations = filename["Affiliations"].split(",")
            for affiliation in affiliations:
                self.affiliations.append(int(affiliation))
        else:
            self.affiliations.append(int(filename["Affiliations"]))
        self.personal_info.load(filename)
        self.contact_info.load(filename)
        self.research_info.load(filename)

    def __str__(self):
        string = f"id: {self.id}\n"
        string += f"Affiliation: {self.affiliations}\n"
        string += str(self.personal_info)
        string += str(self.contact_info)
        string += str(self.research_info)
        return string

    def __repr__(self):
        string = (
            f"Author("
            f"id={self.id}, "
            f"affiliation={repr(self.affiliations)}, "
            f"personal_info={repr(self.personal_info)}, "
            f"contact_info={repr(self.contact_info)}, "
            f"research_info={repr(self.research_info)})"
        )
        return string


class Authors:
    """
    A class to represent a list of authors.

    Attributes:
    authors (list): The list of authors.

    Methods:
    get_author(author_id, affiliation_id): Gets the author.
    load(filename): Loads the authors from the file.
    __str__(): Returns a string representation of the authors.
    __repr__(): Returns a string representation of the authors.
    """

    def __init__(self):
        self.authors = []

    def get_author(self, author_id, affiliation_id=None):
        """
        Gets the author by ID and affiliation ID.
        """
        if isinstance(author_id, str):
            author_id = int(author_id)
        if affiliation_id is None:
            for author in self.authors:
                if author.id == author_id:
                    return author
            return None
        for author in self.authors:
            if author.id == author_id and affiliation_id in author.affiliations:
                return author
        return None

    def load(self, filename):
        """
        Loads the authors from the file.
        """
        authors_df = pd.read_excel(filename, sheet_name="Authors")
        for _, row in authors_df.iterrows():
            self.authors.append(AuthorsData())
            self.authors[-1].load(row)

    def __str__(self):
        string = ""
        for author in self.authors:
            string += str(author) + "\n"
        return string

    def __repr__(self):
        string = (
            f"Authors("
            f"authors={repr(self.authors)})"
        )
        return string
