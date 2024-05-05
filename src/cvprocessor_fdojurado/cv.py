# This is the main entry point of the program. It imports the necessary modules and calls the functions to create the content of the website.
import pandas as pd
import sys

# Import classes from other modules such as news, publications, research, quarto_variables, and public_key
from cvprocessor_fdojurado.intro import Intro
from cvprocessor_fdojurado.education import Education
from cvprocessor_fdojurado.publications import Publications
from cvprocessor_fdojurado.authors import Authors
from cvprocessor_fdojurado.software import Software
from cvprocessor_fdojurado.institutes import Institutes
from cvprocessor_fdojurado.news import News
from cvprocessor_fdojurado.research_interests import ResearchInterests


class CV:
    def __init__(self, filename):
        self._filename = filename
        self._education = Education(self.filename)
        self._institutes = Institutes(self.filename)
        self._software = Software(self.filename)
        self._intro = Intro(self.filename)
        self._authors = Authors(self.filename, self)
        self._news = News(self.filename)
        self._publications = Publications(self.filename, self)
        self._research_interests = ResearchInterests(self.filename)

    @property
    def filename(self):
        return self._filename

    @property
    def intro(self):
        return self._intro

    @property
    def education(self):
        return self._education

    @property
    def institutes(self):
        return self._institutes

    @property
    def authors(self):
        return self._authors

    @property
    def software(self):
        return self._software

    @property
    def intro(self):
        return self._intro

    @property
    def news(self):
        return self._news

    @property
    def publications(self):
        return self._publications

    @property
    def research_interests(self):
        return self._research_interests


if __name__ == "__main__":
    cv = CV("cv.xlsx")
    cv.intro.print()
    cv.education.print()
    cv.institutes.print()
    cv.authors.print()
    cv.software.print()
    cv.publications.print()
    cv.news.print()
    cv.research_interests.print()
    sys.exit(0)
