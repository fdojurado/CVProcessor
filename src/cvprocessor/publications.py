"""
This module contains the classes and methods to process the publications data from the CV file.
"""
import pandas as pd


from cvprocessor import common


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
        self.source = str()

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

    def get_source(self):
        """
        Get the source of the publication.
        """
        return self.source

    def load(self, filename):
        """
        Load the publication journal information from the file.
        """
        self.volume = filename["Volume"]
        self.issue = filename["Issue"]
        self.artno = filename["Art. No."]
        self.source = filename["Source"]

    def __repr__(self):
        string = (
            f"Source("
            f"volume={self.volume}, "
            f"issue={self.issue}, "
            f"artno={self.artno}, "
            f"source={self.source})"
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
    document_type (str): The document type of the publication.
    """

    def __init__(self):
        self.title = str()
        self.year = pd.Timestamp("NaT")
        self.source = Source()
        self.pages = Pages()
        self.document_type = str()
        self.abstract = str()
        self.keywords = str()

    def get_title(self):
        """
        Get the title of the publication.
        """
        return self.title

    def get_year(self):
        """
        Get the year of the publication.
        """
        return self.year

    def get_document_type(self):
        """
        Get the document type of the publication.
        """
        return self.document_type

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
        self.year = filename["Year"]
        if len(self.year.split()) == 1:
            self.year = "Jan "+self.year
        # To datetime month year format
        self.year = pd.to_datetime(self.year, format="%b %Y").date()
        self.source.load(filename)
        self.pages.load(filename)
        self.document_type = filename["Document Type"]
        self.abstract = filename["Abstract"]
        self.keywords = filename["Keywords"]

    def __repr__(self):
        string = (
            f"Details("
            f"title={self.title}, "
            f"year={self.year}, "
            f"source={repr(self.source)}, "
            f"pages={repr(self.pages)}, "
            f"document_type={self.document_type}, "
            f"abstract={self.abstract}, "
            f"keywords={self.keywords})"
        )
        return string


class Social:
    """
    A class to represent the resources of a publication.

    Attributes:
    code (str): The code of the publication.
    slides (str): The slides of the publication.
    doi (str): The DOI of the publication.
    preprint_doi (str): The preprint DOI of the publication.
    """

    def __init__(self):
        self.code = str()
        self.slides = str()
        self.doi = str()
        self.preprint_doi = str()

    def get_code(self):
        """
        Get the code of the publication.
        """
        return self.code

    def get_slides(self):
        """
        Get the slides of the publication.
        """
        return self.slides

    def get_doi(self):
        """
        Get the DOI of the publication.
        """
        return self.doi

    def get_preprint_doi(self):
        """
        Get the preprint DOI of the publication.
        """
        return self.preprint_doi

    def load(self, filename):
        """
        Load the publication resources from the file.
        """
        self.code = filename["Code"]
        self.slides = filename["Slides"]
        self.doi = filename["DOI"]
        self.preprint_doi = filename["Preprint DOI"]

    def __repr__(self):
        string = (
            f"Social("
            f"code={self.code}, "
            f"slides={self.slides}, "
            f"doi={self.doi}, "
            f"preprint_doi={self.preprint_doi})"
        )
        return string

    def __str__(self):
        string = f"Code: {self.code}\n"
        string += f"Slides: {self.slides}\n"
        string += f"DOI: {self.doi}\n"
        string += f"Preprint DOI: {self.preprint_doi}\n"
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

    def __str__(self):
        string = f"License: {self.license}\n"
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
        self.social = Social()
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
        self.social.load(filename)
        self.rights.load(filename)

    def get_apa_citation(self) -> str:
        """
        Build the APA citation.
        """
        citation = ""
        if not common.check_nan(self.details.get_year()):
            citation += f"({self.details.get_year().year}). "
        if not common.check_nan(self.details.get_title()):
            citation += f"{self.details.get_title()}. "
        if not common.check_nan(self.details.source.get_source()):
            citation += f"{self.details.source.get_source()}"
        if not common.check_nan(self.details.source.get_volume()):
            citation += f", {int(self.details.source.get_volume())}"
        if not common.check_nan(self.details.source.get_issue()):
            citation += f"({int(self.details.source.get_issue())})"
        if not common.check_nan(self.details.source.get_artno()):
            citation += f"{self.details.source.get_artno()}"
        if not common.check_nan(self.details.pages.get_page_start()):
            citation += f", pp. {int(self.details.pages.get_page_start())}"
        if not common.check_nan(self.details.pages.get_page_end()):
            citation += f"-{int(self.details.pages.get_page_end())}"
        if not common.check_nan(self.social.get_doi()):
            citation += f", doi: {self.social.get_doi()}"
        citation += "."
        return citation

    def __str__(self) -> str:
        string = f"Authors' IDs and Affiliation IDs: {list(map(str, self.auth_id_aff_id))}\n"
        string += str(self.details)
        string += str(self.social)
        string += str(self.rights)
        return string

    def __repr__(self) -> str:
        string = (
            f"PublicationsData("
            f"authors={repr(self.auth_id_aff_id)}, "
            f"details={repr(self.details)}, "
            f"social={repr(self.social)}, "
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
            sources.add(publication.details.source.get_source())
        return len(sources)

    def get_document_types(self):
        """
        Gets the document types.
        """
        document_types = set()
        for publication in self:
            document_types.add(publication.details.document_type)
        return document_types

    def get_publication_by_title(self, title):
        """
        Get the publication by the title.
        """
        for publication in self:
            if publication.details.get_title() == title:
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
            years.append(publication.details.get_year().year)
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
                x.details.get_year(), x.details.get_title()), reverse=True
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
