import pandas as pd


class ResearchInterests:
    def __init__(self, filename):
        self._filename = filename
        self._research_interests = None
        self._keywords = []
        self._load_interests()

    @property
    def filename(self):
        return self._filename

    @property
    def keywords(self):
        return self._keywords

    @property
    def research_interests(self):
        return self._research_interests

    def _load_interests(self):
        self._filename = pd.read_excel(
            self.filename, sheet_name="Research_Interests")
        self._research_interests = self.filename["Interests"].values[0]
        keywords = self.filename["Keywords"]
        for keyword in keywords:
            self._keywords.append(keyword)

    def print(self):
        print(f"Research Interests: {self._research_interests}")
        print(f"Keywords: {self._keywords}")
        print("\n")
