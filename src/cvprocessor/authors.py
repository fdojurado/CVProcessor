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

    def __init__(self, filename):
        self.filename = filename
        self.email = None
        self.telephone = None
        self.website = None
        self.address = None
        self.location = None
        self._load_contact_info()

    def _load_contact_info(self):
        self.email = self.filename["Email"]
        self.telephone = self.filename["Telephone"]
        self.website = self.filename["Website"]
        self.address = self.filename["Address"]
        self.location = self.filename["Location"]

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

    def __init__(self, filename):
        self.filename = filename
        self.linkedin = None
        self.github = None
        self.google_scholar = None
        self.orcid = None
        self.researchgate = None
        self._load_research_info()

    def _load_research_info(self):
        self.linkedin = self.filename["LinkedIn"]
        self.github = self.filename["GitHub"]
        self.google_scholar = self.filename["Google Scholar"]
        self.orcid = self.filename["ORCID"]
        self.researchgate = self.filename["ResearchGate"]

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

    def __init__(self, filename):
        self.name = None
        self.lastname = None
        self.alias_long = None
        self.alias_short = None
        self.job_title = None
        self.fingerprint = None
        self.public_key = None
        self._load_personal_info(filename)

    def _load_personal_info(self, filename):
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
    """

    def __init__(self, filename, affiliation):
        """
        Constructs all the necessary attributes for the author object.

        :param filename: The name of the file
        :type filename: str
        :param affiliation: The affiliation of the author
        :type affiliation: Affiliation
        """
        self._filename = filename
        self._id = None
        self._affiliation = affiliation
        self._personal_info = PersonalInfo(filename)
        self._contact_info = ContactInfo(filename)
        self._research_info = ResearchInfo(filename)
        self._load_authors()

    @property
    def filename(self):
        """
        Gets the filename of the author.

        :return: The filename of the author
        :rtype: str
        """
        return self._filename

    @property
    def id(self):
        """
        Gets the ID of the author.

        :return: The ID of the author
        :rtype: str
        """
        return self._id

    @property
    def affiliation(self):
        """
        Gets the affiliation of the author.

        :return: The affiliation of the author
        :rtype: Affiliation
        """
        return self._affiliation

    @property
    def personal_info(self):
        """
        Gets the personal information of the author.

        :return: The personal information of the author
        :rtype: PersonalInfo
        """
        return self._personal_info

    @property
    def contact_info(self):
        """
        Gets the contact information of the author.

        :return: The contact information of the author
        :rtype: ContactInfo
        """
        return self._contact_info

    @property
    def research_info(self):
        """
        Gets the research information of the author.

        :return: The research information of the author
        :rtype: ResearchInfo
        """
        return self._research_info

    def _load_authors(self):
        self._id = int(self.filename["id"])

    def __str__(self):
        string = f"id: {self.id}\n"
        string += f"Affiliation: \n{self.affiliation}\n"
        string += f"Personal Info: \n{self.personal_info}\n"
        string += f"Contact Info: \n{self.contact_info}\n"
        string += f"Research Info: \n{self.research_info}\n"
        return string

    def __repr__(self):
        string = (
            f"Author("
            f"id={self.id}, "
            f"affiliation={repr(self.affiliation)}, "
            f"personal_info={repr(self.personal_info)}, "
            f"contact_info={repr(self.contact_info)}, "
            f"research_info={repr(self.research_info)})"
        )
        return string


class Authors:
    """
    A class to represent a list of authors.
    """

    def __init__(self, filename, cv):
        """
        Constructs all the necessary attributes for the authors object.

        :param filename: The name of the file
        :type filename: str
        :param cv: The CV object
        :type cv: CV
        """
        self._filename = filename
        self._cv = cv
        self._authors = self._load_authors()

    @property
    def filename(self):
        """
        Gets the filename of the authors.

        :return: The filename of the authors
        :rtype: str
        """
        return self._filename

    @property
    def cv(self):
        """
        Gets the CV of the authors.

        :return: The CV of the authors
        :rtype: CV
        """
        return self._cv

    @property
    def authors(self):
        """
        Gets the authors.

        :return: The authors
        :rtype: list
        """
        return self._authors

    def get_author(self, author_id, affiliation_id=None):
        """
        Gets the author.

        :param author_id: The ID of the author
        :type author_id: int
        :param affiliation_id: The ID of the affiliation
        :type affiliation_id: int
        :return: The author
        :rtype: Author
        """
        if isinstance(author_id, str):
            author_id = int(author_id)
        if affiliation_id is None:
            for author in self.authors:
                if author.id == author_id:
                    return author
            return None
        for author in self.authors:
            if author.id == author_id and \
                self.cv.institutes.get_institute(int(affiliation_id)).id == \
                    author.affiliation.id:
                return author
        return None

    def _load_authors(self):
        authors_df = pd.read_excel(self.filename, sheet_name="Authors")
        authors = []
        for _, row in authors_df.iterrows():
            if isinstance(row["Affiliations"], str) and\
                    ("," in row["Affiliations"] or ";" in row["Affiliations"]):
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
        string = (
            f"Authors("
            f"filename={self.filename}, "
            f"authors={self.authors})\n"
        )
        return string
