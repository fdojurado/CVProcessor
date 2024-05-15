"""
This module contains the classes and methods to process the publications data from the CV file.
"""
import pandas as pd


from cvprocessor import common


class PublicationBasicInfo:
    """
    A class to represent the basic information of a publication.
    """

    def __init__(self):
        self.title = str()
        self.year: pd.Timestamp = pd.Timestamp("NaT")
        self.source = str()

    def get_date(self):
        """
        Get the date of the publication.
        """
        return self.year.date()

    def process_year_data(self, year):
        """
        Process the year data.
        """
        if len(year.split()) == 1:
            year = 'Jan ' + year
        self.year = pd.to_datetime(year, format="%b %Y")

    def load(self, filename):
        """
        Load the publication basic information from the file.
        """
        self.title = filename["Title"]
        self.process_year_data(filename["Year"])
        self.source = filename["Source"]

    def __repr__(self):
        string = (
            f"PublicationBasicInfo("
            f"title={self.title}, "
            f"year={self.year}, "
            f"source={self.source})"
        )
        return string

    def __str__(self):
        string = f"Title: {self.title}\n"
        string += f"Year: {self.year}\n"
        string += f"Source: {self.source}\n"
        return string


class PublicationJournalInfo:
    """
    A class to represent the journal information of a publication.

    Attributes:
    volume (str): The volume of the publication.
    issue (str): The issue of the publication.
    artno (str): The article number of the publication.
    """

    def __init__(self):
        self.volume = str()
        self.issue = str()
        self.artno = str()

    def load(self, filename):
        """
        Load the publication journal information from the file.
        """
        self.volume = filename["Volume"]
        self.issue = filename["Issue"]
        self.artno = filename["Art. No."]

    def __repr__(self):
        string = (
            f"PublicationJournalInfo("
            f"volume={self.volume}, "
            f"issue={self.issue}, "
            f"artno={self.artno})"
        )
        return string

    def __str__(self):
        string = f"Volume: {self.volume}\n"
        string += f"Issue: {self.issue}\n"
        string += f"Art. No.: {self.artno}\n"
        return string


class PublicationPageInfo:
    """
    A class to represent the page information of a publication.

    Attributes:
    page_start (str): The starting page of the publication.
    page_end (str): The ending page of the publication.
    """

    def __init__(self):
        self.page_start = str()
        self.page_end = str()

    def load(self, filename):
        """
        Load the publication page information from the file.
        """
        self.page_start = filename["Page start"]
        self.page_end = filename["Page end"]

    def __repr__(self):
        string = (
            f"PublicationPageInfo("
            f"page_start={self.page_start}, "
            f"page_end={self.page_end})"
        )
        return string

    def __str__(self):
        string = f"Page start: {self.page_start}\n"
        string += f"Page end: {self.page_end}\n"
        return string


class PublicationDetails:
    """
    A class to represent the details of a publication.

    Attributes:
    basic_info (PublicationBasicInfo): The basic information of the publication.
    journal_info (PublicationJournalInfo): The journal information of the publication.
    page_info (PublicationPageInfo): The page information of the publication.
    document_type (str): The document type of the publication.
    """

    def __init__(self):
        self.basic_info = PublicationBasicInfo()
        self.journal_info = PublicationJournalInfo()
        self.page_info = PublicationPageInfo()
        self.document_type = str()

    def load(self, filename):
        """
        Load the publication details from the file.
        """
        self.basic_info.load(filename)
        self.journal_info.load(filename)
        self.page_info.load(filename)
        self.document_type = filename["Document Type"]

    def __repr__(self):
        string = (
            f"PublicationDetails("
            f"basic_info={self.basic_info}, "
            f"journal_info={self.journal_info}, "
            f"page_info={self.page_info})"
        )
        return string

    def __str__(self):
        string = str(self.basic_info)
        string += str(self.journal_info)
        string += str(self.page_info)
        return string


class PublicationResources:
    """
    A class to represent the resources of a publication.

    Attributes:
    code (str): The code of the publication.
    slides (str): The slides of the publication.
    abstract (str): The abstract of the publication.
    keywords (str): The keywords of the publication.
    doi (str): The DOI of the publication.
    preprint_doi (str): The preprint DOI of the publication.
    """

    def __init__(self):
        self.code = str()
        self.slides = str()
        self.abstract = str()
        self.keywords = str()
        self.doi = str()
        self.preprint_doi = str()

    def load(self, filename):
        """
        Load the publication resources from the file.
        """
        self.code = filename["Code"]
        self.slides = filename["Slides"]
        self.abstract = filename["Abstract"]
        self.keywords = filename["Keywords"]
        self.doi = filename["DOI"]
        self.preprint_doi = filename["Preprint DOI"]

    def __repr__(self):
        string = (
            f"PublicationResources("
            f"code={self.code}, "
            f"slides={self.slides}, "
            f"abstract={self.abstract}, "
            f"keywords={self.keywords}, "
            f"doi={self.doi}, "
            f"preprint_doi={self.preprint_doi})"
        )
        return string

    def __str__(self):
        string = f"Code: {self.code}\n"
        string += f"Slides: {self.slides}\n"
        string += f"Abstract: {self.abstract}\n"
        string += f"Keywords: {self.keywords}\n"
        string += f"DOI: {self.doi}\n"
        string += f"Preprint DOI: {self.preprint_doi}\n"
        return string


class PublicationRights:
    """
    A class to represent the rights of a publication.

    Attributes:
    jcr (str): The JCR of the publication.
    license (str): The license of the publication.
    copyright (str): The copyright of the publication.
    """

    def __init__(self):
        self.jcr = str()
        self.license = str()
        self.copyright = str()

    def load(self, filename):
        """
        Load the publication rights from the file.
        """
        self.jcr = filename["JCR"]
        self.license = filename["License"]
        self.copyright = filename["Copyright"]

    def __repr__(self):
        string = (
            f"PublicationRights("
            f"jcr={self.jcr}, "
            f"license={self.license}, "
            f"copyright={self.copyright})"
        )
        return string

    def __str__(self):
        string = f"JCR: {self.jcr}\n"
        string += f"License: {self.license}\n"
        string += f"Copyright: {self.copyright}"
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
    details (PublicationDetails): The details of the publication.
    resources (PublicationResources): The resources of the publication.
    rights (PublicationRights): The rights of the publication.

    Methods:
    load: Load the publication data from the file.
    build_apa_citation: Build the APA citation.
    """

    def __init__(self):
        self.auth_id_aff_id = []
        self.details = PublicationDetails()
        self.resources = PublicationResources()
        self.rights = PublicationRights()

    def get_title(self):
        """
        Get the title of the publication.
        """
        return self.details.basic_info.title

    def get_date(self):
        """
        Get the date of the publication.
        """
        return self.details.basic_info.get_date()

    def get_source(self):
        """
        Get the source of the publication.
        """
        return self.details.basic_info.source

    def get_volume(self):
        """
        Get the volume of the publication.
        """
        return self.details.journal_info.volume

    def get_issue(self):
        """
        Get the issue of the publication.
        """
        return self.details.journal_info.issue

    def get_artno(self):
        """
        Get the article number of the publication.
        """
        return self.details.journal_info.artno

    def get_page_start(self):
        """
        Get the starting page of the publication.
        """
        return self.details.page_info.page_start

    def get_page_end(self):
        """
        Get the ending page of the publication.
        """
        return self.details.page_info.page_end

    def get_document_type(self):
        """
        Get the document type of the publication.
        """
        return self.details.document_type

    def get_code(self):
        """
        Get the code of the publication.
        """
        return self.resources.code

    def get_slides(self):
        """
        Get the slides of the publication.
        """
        return self.resources.slides

    def get_abstract(self):
        """
        Get the abstract of the publication.
        """
        return self.resources.abstract

    def get_keywords(self):
        """
        Get the keywords of the publication.
        """
        return self.resources.keywords

    def get_doi(self):
        """
        Get the DOI of the publication.
        """
        return self.resources.doi

    def get_preprint_doi(self):
        """
        Get the preprint DOI of the publication.
        """
        return self.resources.preprint_doi

    def get_jcr(self):
        """
        Get the JCR of the publication.
        """
        return self.rights.jcr

    def get_license(self):
        """
        Get the license of the publication.
        """
        return self.rights.license

    def get_copyright(self):
        """
        Get the copyright of the publication.
        """
        return self.rights.copyright

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
        self.resources.load(filename)
        self.rights.load(filename)

    def get_apa_citation(self) -> str:
        """
        Build the APA citation.
        """
        citation = ""
        if not common.check_nan(self.details.basic_info.year):
            citation += f" ({self.details.basic_info.year.year}). "
        if not common.check_nan(self.details.basic_info.title):
            citation += f"{self.details.basic_info.title}. "
        if not common.check_nan(self.details.basic_info.source):
            citation += f"{self.details.basic_info.source}"
        if not common.check_nan(self.details.journal_info.volume):
            citation += f", {int(self.details.journal_info.volume)}"
        if not common.check_nan(self.details.journal_info.issue):
            citation += f"({int(self.details.journal_info.issue)})"
        if not common.check_nan(self.details.journal_info.artno):
            citation += f"{self.details.journal_info.artno}"
        if not common.check_nan(self.details.page_info.page_start):
            citation += f", pp. {int(self.details.page_info.page_start)}"
        if not common.check_nan(self.details.page_info.page_end):
            citation += f"-{int(self.details.page_info.page_end)}"
        if not common.check_nan(self.resources.doi):
            citation += f", doi: {self.resources.doi}"
        citation += "."
        return citation

    def __str__(self) -> str:
        string = f"Authors' IDs and Affiliation IDs: {list(map(str, self.auth_id_aff_id))}\n"
        string += str(self.details)
        string += str(self.resources)
        string += str(self.rights)
        return string

    def __repr__(self) -> str:
        string = (
            f"PublicationsData("
            f"authors={repr(self.auth_id_aff_id)}, "
            f"details={repr(self.details)}, "
            f"resources={repr(self.resources)}, "
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
    get_document_types: Gets the document types.
    get_document_types_ordered: Gets the document types ordered.
    get_num_publications_by_document_type: Gets the number of publications by document type.
    get_num_publications_by_author: Gets the number of publications by author.
    get_publications_year_range: Gets the year range of the publications.
    """

    def __init__(self):
        self.publications = []

    def get_publications_count(self):
        """
        Gets the number of publications.
        """
        return len(self.publications)

    def get_unique_sources(self):
        """
        Gets the number of unique sources.
        """
        sources = set()
        for publication in self.publications:
            sources.add(publication.details.basic_info.source)
        return len(sources)

    def get_document_types(self):
        """
        Gets the document types.
        """
        document_types = set()
        for publication in self.publications:
            document_types.add(publication.details.document_type)
        return document_types

    def get_publication_by_title(self, title):
        """
        Get the publication by the title.
        """
        for publication in self.publications:
            if publication.get_title() == title:
                return publication
        return None

    def get_document_types_ordered(self):
        """
        Gets the document types ordered.
        """
        document_types = []
        for publication in self.publications:
            if publication.details.document_type not in document_types:
                document_types.append(publication.details.document_type)
        return document_types

    def get_num_publications_by_document_type(self, document_type):
        """
        Gets the number of publications by document type.
        """
        count = 0
        for publication in self.publications:
            if publication.details.document_type == document_type:
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

    def get_publications_year_range(self):
        """
        Gets the year range of the publications.
        """
        years = []
        for publication in self.publications:
            years.append(publication.details.basic_info.get_date().year)
        return min(years), max(years)

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
                x.details.document_type, x.details.basic_info.year), reverse=True
        )

    def __str__(self):
        string = ""
        for publication in self.publications:
            string += str(publication) + "\n\n"
        return string

    def __repr__(self):
        string = (
            f"Publications("
            f"publications={list(map(repr, self.publications))}"
        )
        return string

    def __iter__(self):
        return iter(self.publications)
