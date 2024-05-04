# This is the main entry point of the program. It imports the necessary modules and calls the functions to create the content of the website.
import pandas as pd
import sys

# Import classes from other modules such as news, publications, research, quarto_variables, and public_key
from intro import Intro
from education import Education
from publications import Publications
from authors import Authors
from software import Software
from institutes import Institutes


class CV:
    def __init__(self, filename):
        self._filename = filename
        self._education = Education(self.filename)
        self._institutes = Institutes(self.filename)
        self._software = Software(self.filename)
        self._intro = Intro(self.filename)
        self._authors = Authors(self.filename, self)
        self._publications = Publications(self.filename, self)

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
    def publications(self):
        return self._publications


if __name__ == "__main__":
    cv = CV("cv.xlsx")
    cv.intro.print()
    cv.education.print()
    cv.institutes.print()
    cv.authors.print()
    cv.software.print()
    cv.publications.print()
    sys.exit(0)
