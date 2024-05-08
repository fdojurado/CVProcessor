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
from cvprocessor.supervision import Supervision


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
        self._supervision = Supervision(self.filename, self)

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

    @property
    def supervision(self):
        return self._supervision

    def __str__(self):
        string = f"Education: {self.education}\n"
        string += f"Institutes: {self.institutes}\n"
        string += f"Software: {self.software}\n"
        string += f"Intro: {self.intro}\n"
        string += f"Authors: {self.authors}\n"
        string += f"News: {self.news}\n"
        string += f"Publications: {self.publications}\n"
        string += f"Research Interests: {self.research_interests}\n"
        string += f"Grants and Awards: {self.grants_awards}\n"
        string += f"Teaching: {self.teaching}\n"
        string += f"Supervision: {self.supervision}\n"
        return string

    def __repr__(self):
        repr = f"CV(filename={self.filename}, education={self.education}, institutes={self.institutes}, software={self.software}, intro={self.intro}, authors={self.authors}, news={self.news}, publications={self.publications}, research_interests={self.research_interests}, grants_awards={self.grants_awards}, teaching={self.teaching}, supervision={self.supervision})"
        return repr


if __name__ == "__main__":
    cv = CV("cv.xlsx")
    print(repr(cv.supervision))
    sys.exit(0)
