# Introduction class that receives information given a pandas dataframe
import pandas as pd


class Intro:
    def __init__(self, filename):
        self._filename = filename
        self._short_summary = None
        self._long_summary = None
        self._job_title = None
        self._tagline = None
        self._intro = self._get_intro()
        self.load_intro()

    @property
    def intro(self):
        return self._intro

    @property
    def filename(self):
        return self._filename

    @property
    def short_summary(self):
        return self._short_summary

    @property
    def long_summary(self):
        return self._long_summary

    @property
    def job_title(self):
        return self._job_title

    @property
    def tagline(self):
        return self._tagline

    def _get_intro(self):
        return pd.read_excel(self.filename, sheet_name="Intro")

    def load_intro(self):
        self._short_summary = self.intro["Short summary"].values[0]
        self._long_summary = self.intro["Welcome"].values[0]
        # self._job_title = self.intro["Jobtitle"].values[0]
        self._tagline = self.intro["Tagline"].values[0]

    def __str__(self) -> str:
        string = f"Short summary: {self.short_summary}\n"
        string += f"Long summary: {self.long_summary}\n"
        string += f"Job title: {self.job_title}\n"
        string += f"Tagline: {self.tagline}\n\n"
        return string

    def __repr__(self) -> str:
        repr = f"Intro(filename={self.filename}, short_summary={self.short_summary}, long_summary={self.long_summary}, job_title={self.job_title}, tagline={self.tagline})"
        return repr
