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

    def print(self):
        print(f"Short summary: {self.short_summary}")
        print(f"Long summary: {self.long_summary}")
        print(f"Job title: {self.job_title}")
        print(f"Tagline: {self.tagline}")
        print("\n")
