"""
    Authors module.

    This module contains the classes to represent the authors of the CV.

    Classes:
    AuthorsData: A class to represent an author.
    Authors: A class to represent a list of authors.
"""
import pandas as pd


class Contact:
    """
    A class to represent the contact information of an author.
    """

    def __init__(self):
        self.email = str()
        self.telephone = str()
        self.website = str()
        self.address = str()
        self.location = str()

    def get_email(self):
        """
        Returns the email of the author.
        """
        return self.email

    def get_telephone(self):
        """
        Returns the telephone of the author.
        """
        return self.telephone

    def get_website(self):
        """
        Returns the website of the author.
        """
        return self.website

    def get_address(self):
        """
        Returns the address of the author.
        """
        return self.address

    def get_location(self):
        """
        Returns the location of the author.
        """
        return self.location

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
            f"Contact("
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


class Social:
    """
    A class to represent the social profiles of an author.
    """

    def __init__(self):
        self.linkedin = str()
        self.github = str()
        self.google_scholar = str()
        self.orcid = str()
        self.researchgate = str()

    def get_linkedin(self):
        """
        Returns the LinkedIn of the author.
        """
        return self.linkedin

    def get_github(self):
        """
        Returns the GitHub of the author.
        """
        return self.github

    def get_google_scholar(self):
        """
        Returns the Google Scholar of the author.
        """
        return self.google_scholar

    def get_orcid(self):
        """
        Returns the ORCID of the author.
        """
        return self.orcid

    def get_researchgate(self):
        """
        Returns the ResearchGate of the author.
        """
        return self.researchgate

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
            f"Social("
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


class Personal:
    """
    A class to represent the personal information of an author.

    Attributes:
    name (str): The name of the author.
    lastname (str): The lastname of the author.
    alias_long (str): The long alias of the author.
    alias_short (str): The short alias of the author.
    job_title (str): The job title of the author.
    """

    def __init__(self):
        self.name = str()
        self.lastname = str()
        self.alias_long = str()
        self.alias_short = str()
        self.job_title = str()

    def get_name(self):
        """
        Returns the name of the author.
        """
        return self.name

    def get_lastname(self):
        """
        Returns the lastname of the author.
        """
        return self.lastname

    def get_alias_long(self):
        """
        Returns the long alias of the author.
        """
        return self.alias_long

    def get_alias_short(self):
        """
        Returns the short alias of the author.
        """
        return self.alias_short

    def get_job_title(self):
        """
        Returns the job title of the author.
        """
        return self.job_title

    def load(self, filename):
        """
        Loads the personal information of the author.
        """
        self.name = filename["Name"]
        self.lastname = filename["Lastname"]
        self.alias_long = filename["Alias Long"]
        self.alias_short = filename["Alias Short"]
        self.job_title = filename["Job Title"]

    def __repr__(self):
        string = (
            f"Personal("
            f"name={self.name}, "
            f"lastname={self.lastname}, "
            f"alias_long={self.alias_long}, "
            f"alias_short={self.alias_short}, "
            f"job_title={self.job_title})"
        )
        return string


class Security:
    """
    A class to represent the security details of an author.

    Attributes:
    fingerprint (str): The fingerprint of the author.
    public_key (str): The public key of the author.
    """

    def __init__(self):
        self.fingerprint = str()
        self.public_key = str()

    def get_fingerprint(self):
        """
        Returns the fingerprint of the author.
        """
        return self.fingerprint

    def get_public_key(self):
        """
        Returns the public key of the author.
        """
        return self.public_key

    def load(self, filename):
        """
        Loads the security details of the author.
        """
        self.fingerprint = filename["Fingerprint"]
        self.public_key = filename["Public Key"]

    def __repr__(self):
        string = (
            f"Security("
            f"fingerprint={self.fingerprint}, "
            f"public_key={self.public_key})"
        )
        return string


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
        self.affiliation_ids = []
        self.personal = Personal()
        self.contact = Contact()
        self.social = Social()
        self.security = Security()

    def get_id(self):
        """
        Returns the ID of the author.
        """
        return self.id

    def get_affiliation_ids(self):
        """
        Returns the affiliations of the author.
        """
        return self.affiliation_ids

    def load(self, filename):
        """
        Loads the author data from the file.
        """
        self.id = filename["id"]
        if isinstance(filename["Affiliations"], str) and\
                ("," in filename["Affiliations"] or ";" in filename["Affiliations"]):
            affiliations = filename["Affiliations"].split(",")
            for affiliation in affiliations:
                self.affiliation_ids.append(int(affiliation))
        else:
            self.affiliation_ids.append(int(filename["Affiliations"]))
        self.personal.load(filename)
        self.contact.load(filename)
        self.social.load(filename)
        self.security.load(filename)

    def __repr__(self):
        string = (
            f"Author("
            f"id={self.id}, "
            f"affiliation={repr(self.affiliation_ids)}, "
            f"personal={repr(self.personal)}, "
            f"contact={repr(self.contact)}, "
            f"social={repr(self.social)}, "
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
