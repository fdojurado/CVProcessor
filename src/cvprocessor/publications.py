import pandas as pd


from cvprocessor import common


class PublicationsData:
    def __init__(self, filename, cv):
        self._filename = filename
        self._cv = cv
        self._authors = None
        self._title = None
        self._year = None
        self._source = None
        self._volume = None
        self._issue = None
        self._artno = None
        self._page_start = None
        self._page_end = None
        self._doi = None
        self._preprint_doi = None
        self._document_type = None
        self._code = None
        self._slides = None
        self._abstract = None
        self._keywords = None
        self._jcr = None
        self._license = None
        self._copyright = None
        self._load_publications()

    @property
    def filename(self):
        return self._filename

    @property
    def cv(self):
        return self._cv

    @property
    def authors(self):
        return self._authors

    @property
    def title(self):
        return self._title

    @property
    def year(self):
        return self._year

    @property
    def source(self):
        return self._source

    @property
    def volume(self):
        return self._volume

    @property
    def issue(self):
        return self._issue

    @property
    def artno(self):
        return self._artno

    @property
    def page_start(self):
        return self._page_start

    @property
    def page_end(self):
        return self._page_end

    @property
    def doi(self):
        return self._doi

    @property
    def preprint_doi(self):
        return self._preprint_doi

    @property
    def document_type(self):
        return self._document_type

    @property
    def code(self):
        return self._code

    @property
    def slides(self):
        return self._slides

    @property
    def abstract(self):
        return self._abstract

    @property
    def keywords(self):
        return self._keywords

    @property
    def jcr(self):
        return self._jcr

    @property
    def license(self):
        return self._license

    @property
    def copyright(self):
        return self._copyright

    def load_authors(self):
        authors_list = self.filename["Authors"].split(",")
        authors = []
        for author in authors_list:
            if "(" in author:
                # Author with specific affiliation
                author_tuple = author.split("(")[1].split(")")[0]
                author_tuple_list = author_tuple.split(";")
                author_id = author_tuple_list[0]
                author_affiliation = author_tuple_list[1:]
            else:
                author_id = author
                author_affiliation = None

            if isinstance(author_affiliation, list):
                for affiliation in author_affiliation:
                    author = self.cv.authors.get_author(
                        int(author_id), int(affiliation))
                    if author is None:
                        raise ValueError(
                            f"Author with ID {author_id} and affiliation {affiliation} not found")
                    authors.append(author)
            else:
                author = self.cv.authors.get_author(int(author_id))
                if author is None:
                    raise ValueError(
                        f"Author with ID {author_id} not found")
                authors.append(author)
        return authors

    def process_year_data(self):
        if len(self.year.split()) == 1:
            self._year = 'Jan ' + self.year
        else:
            self._year = self.year
        self._year = pd.to_datetime(self.year, format="%b %Y")

    def _load_publications(self):
        self._authors = self.load_authors()
        self._title = self.filename["Title"]
        self._year = self.filename["Year"]
        self.process_year_data()
        self._source = self.filename["Source"]
        self._volume = self.filename["Volume"]
        self._issue = self.filename["Issue"]
        self._artno = self.filename["Art. No."]
        self._page_start = self.filename["Page start"]
        self._page_end = self.filename["Page end"]
        self._doi = self.filename["DOI"]
        self._preprint_doi = self.filename["Preprint DOI"]
        self._document_type = self.filename["Document Type"]
        self._code = self.cv.software.get_software(
            int(self.filename["Code"])) if not common.check_nan(self.filename["Code"]) else None
        self._slides = self.filename["Slides"]
        self._abstract = self.filename["Abstract"]
        self._keywords = self.filename["Keywords"]
        self._jcr = self.filename["JCR"]
        self._license = self.filename["License"]
        self._copyright = self.filename["Copyright"]

    def build_apa_citation(self):
        citation = ""
        authors = [author.alias_short for author in self.authors]
        unique_authors = [authors[i] for i in range(
            len(authors)) if authors[i] not in authors[:i]]
        citation += ', '.join(unique_authors)
        if not common.check_nan(self.year):
            citation += f" ({self.year.year}). "
        if not common.check_nan(self.title):
            citation += f"{self.title}. "
        if not common.check_nan(self.source):
            citation += f"{self.source}"
        if not common.check_nan(self.volume):
            citation += f", {int(self.volume)}"
        if not common.check_nan(self.issue):
            citation += f"({int(self.issue)})"
        if not common.check_nan(self.artno):
            citation += f"{self.artno}"
        if not common.check_nan(self.page_start):
            citation += f", pp. {int(self.page_start)}"
        if not common.check_nan(self.page_end):
            citation += f"-{int(self.page_end)}"
        if not common.check_nan(self.doi):
            citation += f", doi: {self.doi}"
        citation += "."
        return citation

    def __str__(self) -> str:
        string = f"Title: {self.title}\n"
        string += f"Authors: {self.authors}\n"
        string += f"Year: {self.year}\n"
        string += f"Source: {self.source}\n"
        string += f"Volume: {self.volume}\n"
        string += f"Issue: {self.issue}\n"
        string += f"Art. No.: {self.artno}\n"
        string += f"Page start: {self.page_start}\n"
        string += f"Page end: {self.page_end}\n"
        string += f"DOI: {self.doi}\n"
        string += f"Preprint DOI: {self.preprint_doi}\n"
        string += f"Document Type: {self.document_type}\n"
        string += f"Code: {self.code.name if self.code else None}\n"
        string += f"Slides: {self.slides}\n"
        string += f"Abstract: {self.abstract}\n"
        string += f"Keywords: {self.keywords}\n"
        string += f"JCR: {self.jcr}\n"
        string += f"License: {self.license}\n"
        string += f"Copyright: {self.copyright}\n\n"
        return string

    def __repr__(self) -> str:
        repr = f"PublicationsData(authors={self.authors}, title={self.title}, year={self.year}, source={self.source}, volume={self.volume}, issue={self.issue}, artno={self.artno}, page_start={self.page_start}, page_end={self.page_end}, doi={self.doi}, preprint_doi={self.preprint_doi}, document_type={self.document_type}, code={self.code}, slides={self.slides}, abstract={self.abstract}, keywords={self.keywords}, jcr={self.jcr}, license={self.license}, copyright={self.copyright})"
        return repr


class Publications():
    def __init__(self, filename, cv):
        self._filename = filename
        self._cv = cv
        self._publications = self._load_publications()
        # Sort publications by type then year
        self._publications.sort(key=lambda x: (
            x.document_type, x.year), reverse=True)

    @property
    def filename(self):
        return self._filename

    @property
    def cv(self):
        return self._cv

    @property
    def publications(self):
        return self._publications

    def get_publications_count(self):
        return len(self.publications)

    def get_unique_sources(self):
        sources = set()
        for publication in self.publications:
            sources.add(publication.source)
        return len(sources)

    def get_document_types(self):
        document_types = set()
        for publication in self.publications:
            document_types.add(publication.document_type)
        return document_types

    def get_document_types_ordered(self):
        document_types = []
        for publication in self.publications:
            if publication.document_type not in document_types:
                document_types.append(publication.document_type)
        return document_types

    def get_num_publications_by_document_type(self, document_type):
        count = 0
        for publication in self.publications:
            if publication.document_type == document_type:
                count += 1
        return count

    def get_num_publications_by_author(self, author_id):
        count = 0
        for publication in self.publications:
            for author in publication.authors:
                if author.id == author_id:
                    count += 1
                    break
        return count

    def get_publications_year_range(self):
        years = []
        for publication in self.publications:
            years.append(publication.year.year)
        return min(years), max(years)

    def _load_publications(self):
        publications_df = pd.read_excel(
            self.filename, sheet_name="Publications")
        return [PublicationsData(row, self.cv) for index, row in publications_df.iterrows()]

    def __str__(self):
        string = ""
        for publication in self.publications:
            string += str(publication)
        return string

    def __repr__(self):
        repr = f"Publications(filename={self.filename}, cv={self.cv}, publications={self.publications})\n"
        return repr
