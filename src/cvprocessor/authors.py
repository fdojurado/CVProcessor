"""
    Authors module.

    This module contains the classes to represent the authors of the CV.

    Classes:
    AuthorsData: A class to represent an author.
    Authors: A class to represent a list of authors.
"""
import pandas as pd
from cvprocessor.security.security import Security
from cvprocessor.Personal.Personal import Personal
from cvprocessor.contact.contact import Contact
from cvprocessor.links.links import Links


class AuthorsData:
    """
    A class to represent an author.

    Attributes:
    id (int): The ID of the author.
    affiliations (list): The affiliations of the author.
    personal_info (Personal): The personal information of the author.
    contact_info (Contact): The contact information of the author.
    research_info (Social): The research information of the author.

    Methods:
    load(filename): Loads the author data from the file.
    __str__(): Returns a string representation of the author.
    __repr__(): Returns a string representation of the author.
    """

    def __init__(self):
        self.id = int()
        self.job_title = str()
        self.affiliation_ids = []
        self.personal = Personal()
        self.contact = Contact()
        self.links = Links()
        self.security = Security()

    def get_id(self):
        """
        Returns the ID of the author.
        """
        return self.id

    def get_job_title(self):
        """
        Returns the job title of the author.
        """
        return self.job_title

    def get_affiliation_ids(self):
        """
        Returns the affiliations of the author.
        """
        return self.affiliation_ids

    def load(self, df):
        """
        Loads the author data from the file.
        """
        self.id = df["id"]
        self.job_title = df["Job Title"]
        if isinstance(df["Affiliations"], str) and\
                ("," in df["Affiliations"] or ";" in df["Affiliations"]):
            affiliations = df["Affiliations"].split(",")
            for affiliation in affiliations:
                self.affiliation_ids.append(int(affiliation))
        else:
            self.affiliation_ids.append(int(df["Affiliations"]))
        self.personal.load(df)
        self.contact.load(df)
        self.links.load(df)
        self.security.load(df)

    def __repr__(self):
        string = (
            f"AuthorsData("
            f"id={self.id}, "
            f"job_title={self.job_title}, "
            f"affiliation_ids={self.affiliation_ids}, "
            f"personal={repr(self.personal)}, "
            f"contact={repr(self.contact)}, "
            f"links={repr(self.links)}, "
            f"security={repr(self.security)})"
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
                if author.get_id() == author_id:
                    return author
            return None
        for author in self.authors:
            if author.get_id() == author_id and affiliation_id in author.get_affiliation_ids():
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

    def __iter__(self):
        return iter(self.authors)
