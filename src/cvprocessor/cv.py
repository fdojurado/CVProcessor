# This is the main entry point of the program. It imports the necessary modules and calls the functions to create the content of the website.
import pandas as pd
import sys

# Import classes from other modules such as news, publications, research, quarto_variables, and public_key
from cvprocessor.intro import Intro
from cvprocessor.education import Education
from cvprocessor.publications import Publications
from cvprocessor.authors import Authors
from cvprocessor.software import Software
from cvprocessor.institutes import Institutes
from cvprocessor.news import News
from cvprocessor.research_interests import ResearchInterests
from cvprocessor.grants_awards import GrantsAwards
from cvprocessor.teaching import Teaching


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
        self._grants_awards = GrantsAwards(self.filename)
        self._teaching = Teaching(self.filename)

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

    @property
    def grants_awards(self):
        return self._grants_awards

    @property
    def teaching(self):
        return self._teaching

    def print(self):
        print("CV")
        print("Filename:", self.filename)
        self.intro.print()
        self.education.print()
        self.institutes.print()
        self.authors.print()
        self.software.print()
        self.publications.print()
        self.news.print()
        self.research_interests.print()
        self.grants_awards.print()
        self.teaching.print()


if __name__ == "__main__":
    cv = CV("cv.xlsx")
    cv.print()
    sys.exit(0)
