import pandas as pd


class ResearchInterests:
    def __init__(self, filename):
        self._filename = filename
        self._interest = None
        self._keywords = []
        self._research_interests = self._get_research_interests()
        self._load_interests()

    @property
    def filename(self):
        return self._filename

    @property
    def interest(self):
        return self._interest

    @property
    def keywords(self):
        return self._keywords

    @property
    def research_interests(self):
        return self._research_interests

    def _get_research_interests(self):
        return pd.read_excel(self.filename, sheet_name="Research_Interests")

    def _load_interests(self):
        self._interest = self.research_interests["Interests"].values[0]
        keywords = self.research_interests["Keywords"]
        for keyword in keywords:
            self._keywords.append(keyword)

    def print(self):
        print(f"Interest: {self._interest}")
        print(f"Keywords: {self._keywords}")
        print("\n")
