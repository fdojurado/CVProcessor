"""
This module contains the classes and methods to process the publications data from the CV file.
"""
import pandas as pd

from cvprocessor.links.links import Links
from cvprocessor.date.date import Dates


class Source:
    """
    A class to represent the source of a publication.

    Attributes:
    volume (str): The volume of the publication.
    issue (str): The issue of the publication.
    artno (str): The article number of the publication.
    """

    def __init__(self):
        self.volume = str()
        self.issue = str()
        self.artno = str()
        self.venue = str()

    def get_volume(self):
        """
        Get the volume of the publication.
        """
        return self.volume

    def get_issue(self):
        """
        Get the issue of the publication.
        """
        return self.issue

    def get_artno(self):
        """
        Get the article number of the publication.
        """
        return self.artno

    def get_venue(self):
        """
        Get the venue of the publication.
        """
        return self.venue

    def load(self, filename):
        """
        Load the publication journal information from the file.
        """
        self.volume = filename["Volume"]
        self.issue = filename["Issue"]
        self.artno = filename["Art. No."]
        self.venue = filename["Source"]

    def __repr__(self):
        string = (
            f"Source("
            f"volume={self.volume}, "
            f"issue={self.issue}, "
            f"artno={self.artno}, "
            f"venue={self.venue})"
        )
        return string


class Pages:
    """
    A class to represent the page information of a publication.

    Attributes:
    page_start (str): The starting page of the publication.
    page_end (str): The ending page of the publication.
    """

    def __init__(self):
        self.page_start = str()
        self.page_end = str()

    def get_page_start(self):
        """
        Get the starting page of the publication.
        """
        return self.page_start

    def get_page_end(self):
        """
        Get the ending page of the publication.
        """
        return self.page_end

    def load(self, filename):
        """
        Load the publication page information from the file.
        """
        self.page_start = filename["Page start"]
        self.page_end = filename["Page end"]

    def __repr__(self):
        string = (
            f"Pages("
            f"page_start={self.page_start}, "
            f"page_end={self.page_end})"
        )
        return string

    def __str__(self):
        string = f"Page start: {self.page_start}\n"
        string += f"Page end: {self.page_end}\n"
        return string


class Details:
    """
    A class to represent the details of a publication.

    Attributes:
    basic_info (PublicationBasicInfo): The basic information of the publication.
    journal_info (Source): The journal information of the publication.
    page_info (Pages): The page information of the publication.
    type (str): The document type of the publication.
    """

    def __init__(self):
        self.title = str()
        self.dates = Dates()
        self.venue = Source()
        self.pages = Pages()
        self.type = str()
        self.abstract = str()
        self.keywords = str()

    def get_title(self):
        """
        Get the title of the publication.
        """
        return self.title

    def get_type(self):
        """
        Get the document type of the publication.
        """
        return self.type

    def get_abstract(self):
        """
        Get the abstract of the publication.
        """
        return self.abstract

    def get_keywords(self):
        """
        Get the keywords of the publication.
        """
        return self.keywords

    def load(self, filename):
        """
        Load the publication details from the file.
        """
        self.title = filename["Title"]
        self.dates.load(filename)
        self.venue.load(filename)
        self.pages.load(filename)
        self.type = filename["Document Type"]
        self.abstract = filename["Abstract"]
        self.keywords = filename["Keywords"]

    def __repr__(self):
        string = (
            f"Details("
            f"title={self.title}, "
            f"dates={repr(self.dates)}, "
            f"source={repr(self.venue)}, "
            f"pages={repr(self.pages)}, "
            f"type={self.type}, "
            f"abstract={self.abstract}, "
            f"keywords={self.keywords})"
        )
        return string


class Rights:
    """
    A class to represent the rights of a publication.

    Attributes:
    license (str): The license of the publication.
    copyright (str): The copyright of the publication.
    """

    def __init__(self):
        self.license = str()
        self.copyright = str()

    def get_license(self):
        """
        Get the license of the publication.
        """
        return self.license

    def get_copyright(self):
        """
        Get the copyright of the publication.
        """
        return self.copyright

    def load(self, filename):
        """
        Load the publication rights from the file.
        """
        self.license = filename["License"]
        self.copyright = filename["Copyright"]

    def __repr__(self):
        string = (
            f"Rights("
            f"license={self.license}, "
            f"copyright={self.copyright})"
        )
        return string


class AuthorIDAffiliationIDs:
    """
    A class to represent the author ID and affiliation IDs.

    Attributes:
    author_id (int): The author ID.
    affiliation_ids (list): The list of affiliation IDs.
    """

    def __init__(self):
        self.author_id = int()
        self.affiliation_ids = []

    def get_author_id(self):
        """
        Get the author ID.
        """
        return self.author_id

    def get_affiliation_ids(self):
        """
        Get the affiliation IDs.
        """
        return self.affiliation_ids

    def add_affiliation_id(self, affiliation_id):
        """
        Add an affiliation ID.
        """
        self.affiliation_ids.append(affiliation_id)

    def __repr__(self):
        string = (
            f"AuthorIDAffiliationIDs("
            f"author_id={self.author_id}, "
            f"affiliation_ids={list(map(str, self.affiliation_ids))})"
        )
        return string

    def __str__(self):
        string = f"Author ID: {self.author_id}\n"
        string += f"Affiliation IDs: {repr(list(map(repr, self.affiliation_ids)))}\n"
        return string


class PublicationsData:
    """
    A class to represent the data of a publication.

    Attributes:
    authors_ids (list): The list of author IDs and affiliation IDs.
    details (Details): The details of the publication.
    resources (Social): The resources of the publication.
    rights (Rights): The rights of the publication.

    Methods:
    load: Load the publication data from the file.
    build_apa_citation: Build the APA citation.
    """

    def __init__(self):
        self.auth_id_aff_id = []
        self.details = Details()
        self.links = Links()
        self.rights = Rights()

    def get_auth_id_aff_id(self):
        """
        Get the author IDs and affiliation IDs.
        """
        return self.auth_id_aff_id

    def load(self, filename):
        """
        Load the publication data from the file.
        """
        authors_list = filename["Authors"].split(",")
        authors = []
        for author in authors_list:
            if "(" in author:
                author_tuple = author.split("(")[1].split(")")[0]
                author_tuple_list = author_tuple.split(";")
                author_id = author_tuple_list[0]
                author_affiliation = author_tuple_list[1:]
            else:
                author_id = author
                author_affiliation = None
            authors.append(AuthorIDAffiliationIDs())
            authors[-1].author_id = int(author_id)
            if author_affiliation is not None:
                for affiliation in author_affiliation:
                    authors[-1].add_affiliation_id(int(affiliation))
        self.auth_id_aff_id = authors
        self.details.load(filename)
        self.links.load(filename)
        self.rights.load(filename)

    def get_apa_citation(self) -> str:
        """
        Build the APA citation.
        """
        citation = ""
        start_date = self.details.dates.get_start()
        if pd.notna(start_date):
            citation += f"({int(start_date.year)}). "
        if pd.notna(self.details.get_title()):
            citation += f"{self.details.get_title()}. "
        if pd.notna(self.details.venue.get_venue()):
            citation += f"{self.details.venue.get_venue()}"
        if pd.notna(self.details.venue.get_volume()):
            citation += f", {int(self.details.venue.get_volume())}"
        if pd.notna(self.details.venue.get_issue()):
            citation += f"({int(self.details.venue.get_issue())})"
        if pd.notna(self.details.venue.get_artno()):
            citation += f"{self.details.venue.get_artno()}"
        if pd.notna(self.details.pages.get_page_start()):
            citation += f", pp. {int(self.details.pages.get_page_start())}"
        if pd.notna(self.details.pages.get_page_end()):
            citation += f"-{int(self.details.pages.get_page_end())}"
        doi = self.links.get_link("DOI")
        if doi is not None:
            citation += f", doi: {doi.get_url()}"
        citation += "."
        return citation

    def __repr__(self) -> str:
        string = (
            f"PublicationsData("
            f"authors={repr(self.auth_id_aff_id)}, "
            f"details={repr(self.details)}, "
            f"links={repr(self.links)}, "
            f"rights={repr(self.rights)})"
        )
        return string


class Publications():
    """
    A class to represent the publications of an author.

    Attributes:
    publications (list): The list of publications.

    Methods:
    get_publications_count: Gets the number of publications.
    get_unique_sources: Gets the number of unique sources.
    get_types: Gets the document types.
    get_types_ordered: Gets the document types ordered.
    get_num_publications_by_type: Gets the number of publications by document type.
    get_num_publications_by_author: Gets the number of publications by author.
    get_publications_date_range: Gets the date range of the publications.
    """

    def __init__(self):
        self.publications = []

    def get_publications_count(self):
        """
        Gets the number of publications.
        """
        return len(self.publications)

    def get_publications_by_index(self, index):
        """
        Gets the publication by index.
        """
        return self.publications[index]

    def get_unique_sources(self):
        """
        Gets the number of unique sources.
        """
        sources = set()
        for publication in self.publications:
            sources.add(publication.details.venue.get_venue())
        return len(sources)

    def get_types(self):
        """
        Gets the document types.
        """
        types = set()
        for publication in self:
            types.add(publication.details.type)
        return types

    def get_publication_by_title(self, title):
        """
        Get the publication by the title.
        """
        for publication in self:
            if publication.details.get_title() == title:
                return publication
        return None

    def get_types_ordered(self):
        """
        Gets the document types ordered.
        """
        types = []
        for publication in self.publications:
            if publication.details.type not in types:
                types.append(publication.details.type)
        return types

    def get_num_publications_by_type(self, type):
        """
        Gets the number of publications by document type.
        """
        count = 0
        for publication in self.publications:
            if publication.details.type == type:
                count += 1
        return count

    def get_num_publications_by_author(self, author_id):
        """
        Gets the number of publications by author.
        """
        count = 0
        for publication in self:
            for auth_id_aff_id in publication.get_auth_id_aff_id():
                if auth_id_aff_id.get_author_id() == author_id:
                    count += 1
        return count

    def get_publications_date_range(self):
        """
        Gets the date range of the publications.
        """
        dates = []
        for publication in self.publications:
            dates.append(publication.details.dates.get_start())
        return min(dates), max(dates)

    def load(self, filename):
        """
        Load the publications data from the file.
        """
        publications_df = pd.read_excel(
            filename, sheet_name="Publications")
        for _, row in publications_df.iterrows():
            self.publications.append(PublicationsData())
            self.publications[-1].load(row)
        self.publications = sorted(
            self.publications, key=lambda x: (
                x.details.dates.get_start(), x.details.get_title()), reverse=True
        )

    def __repr__(self):
        string = (
            f"Publications("
            f"publications={list(map(repr, self.publications))}"
        )
        return string

    def __iter__(self):
        return iter(self.publications)
