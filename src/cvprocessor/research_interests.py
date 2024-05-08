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
        research_interests_pd = pd.read_excel(
            self.filename, sheet_name="Research_Interests")
        self._research_interests = research_interests_pd["Interests"].values[0]
        keywords = research_interests_pd["Keywords"]
        for keyword in keywords:
            self._keywords.append(keyword)

    def __str__(self):
        string = f"Research Interests: {self.research_interests}\n"
        string += f"Keywords: {self.keywords}\n\n"
        return string

    def __repr__(self):
        repr = f"ResearchInterests(filename={self.filename}, research_interests={self.research_interests}, keywords={self.keywords})"
        return repr
