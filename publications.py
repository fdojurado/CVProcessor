import pandas as pd

from authors import Authors
from software import Software


class PublicationsData:
    def __init__(self, filename):
        self._filename = filename
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

    def _load_publications(self):
        authors_list = self.filename["Authors"].split(",")
        self._authors = authors_list
        self._title = self.filename["Title"]
        self._year = self.filename["Year"]
        self._source = self.filename["Source"]
        self._volume = self.filename["Volume"]
        self._issue = self.filename["Issue"]
        self._artno = self.filename["Art. No."]
        self._page_start = self.filename["Page start"]
        self._page_end = self.filename["Page end"]
        self._doi = self.filename["DOI"]
        self._preprint_doi = self.filename["Preprint DOI"]
        self._document_type = self.filename["Document Type"]
        self._code = self.filename["Code"]
        self._slides = self.filename["Slides"]
        self._abstract = self.filename["Abstract"]
        self._keywords = self.filename["Keywords"]
        self._jcr = self.filename["JCR"]
        self._license = self.filename["License"]
        self._copyright = self.filename["Copyright"]

    def print(self):
        # self.authors.print()
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Source: {self.source}")
        print(f"Volume: {self.volume}")
        print(f"Issue: {self.issue}")
        print(f"Art. No.: {self.artno}")
        print(f"Page start: {self.page_start}")
        print(f"Page end: {self.page_end}")
        print(f"DOI: {self.doi}")
        print(f"Preprint DOI: {self.preprint_doi}")
        print(f"Document Type: {self.document_type}")
        print(f"Code: {self.code}")
        print(f"Slides: {self.slides}")
        print(f"Abstract: {self.abstract}")
        print(f"Keywords: {self.keywords}")
        print(f"JCR: {self.jcr}")
        print(f"License: {self.license}")
        print(f"Copyright: {self.copyright}")


class Publications():
    def __init__(self, filename):
        self._filename = filename
        self._publications = self._load_publications()
        # Sort publications by type then year
        self._publications.sort(key=lambda x: (
            x.document_type, x.year), reverse=True)

    @property
    def filename(self):
        return self._filename

    @property
    def publications(self):
        return self._publications

    def _load_publications(self):
        publications_df = pd.read_excel(
            self.filename, sheet_name="Publications")
        return [PublicationsData(row) for index, row in publications_df.iterrows()]

    def print(self):
        for publication in self.publications:
            publication.print()
