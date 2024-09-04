"""
This module contains the classes and methods to process the presentations data from the CV.
"""

import pandas as pd
from cvprocessor.date.date import Date
from cvprocessor.links.links import Link


class Presentation:
    """
    The Presentation class is used to store the presentation data.

    Attributes:
    date (Date): The date of the presentation.
    title (str): The title of the presentation.
    institution_id (int): The institution id of the presentation.
    event (str): The event of the presentation.
    slides (str): The slides of the presentation.
    """

    def __init__(self):
        self.date = Date()
        self.title = str()
        self.institution_id = int()
        self.event = str()
        self.slides = Link()

    def get_title(self):
        """
        Get the title of this presentation.
        """
        return self.title

    def get_institution_id(self):
        """
        Get the institution id of this presentation.
        """
        return self.institution_id

    def get_event(self):
        """
        Get the event of this presentation.
        """
        return self.event

    def get_slides(self):
        """
        Get the slides of this presentation.
        """
        return self.slides

    def load(self, filename):
        """
        Load the presentation data from the given filename.
        """
        self.title = filename["Title"]
        self.date.start = self.date.format_date(filename["Date"])
        self.institution_id = filename["Institution id"]
        self.event = filename["Event"]
        self.slides.type = "Slides"
        self.slides.url = filename["Slides"]

    def __str__(self):
        string = f"Title: {self.title}\n"
        string += f"Date: {self.date.get_range()}\n"
        string += f"Institution id: {self.institution_id}\n"
        string += f"Event: {self.event}\n"
        string += f"Slides: {self.slides}\n"
        return string

    def __repr__(self):
        string = (
            f"Presentation("
            f"title={self.title}, "
            f"date={repr(self.date)}, "
            f"institution_id={self.institution_id}, "
            f"event={self.event}, "
            f"slides={self.slides})\n")
        return string


class Presentations:
    """
    The Presentations class is used to store all the presentation data.

    Attributes:
    presentations (list): The list of Presentation objects.
    """

    def __init__(self):
        self.presentations = []

    def get_presentations(self):
        """
        Get the list of Presentation objects.
        """
        return self.presentations

    def get_presentations_ordered(self):
        """
        Get the presentations ordered by date.
        """
        return sorted(self.presentations, key=lambda x: x.date.get_start(), reverse=True)

    def load(self, filename):
        """
        Load the presentation data from the given filename.
        """
        presentations_df = pd.read_excel(
            filename, sheet_name="Presentations")
        for _, row in presentations_df.iterrows():
            self.presentations.append(Presentation())
            self.presentations[-1].load(row)
        self.presentations.sort(key=lambda x: x.date.get_start(), reverse=True)

    def __repr__(self):
        string = (
            f"Presentations("
            f"presentations={list(map(repr, self.presentations))})"
        )
        return string

    def __iter__(self):
        return iter(self.presentations)
