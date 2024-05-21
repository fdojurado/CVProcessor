"""
Links class is used to store the links of the online presence of the user.
"""

import pandas as pd

link_types = {
    "website": "Website",
    "linkedin": "LinkedIn",
    "preprint": "Preprint",
    "pdf": "PDF",
    "code": "Code",
    "github": "GitHub",
    "twitter": "Twitter",
    "facebook": "Facebook",
    "instagram": "Instagram",
    "youtube": "YouTube",
    "slideshare": "SlideShare",
    "medium": "Medium",
    "researchgate": "ResearchGate",
    "google_scholar": "Google Scholar",
    "orcid": "ORCID",
    "publons": "Publons",
    "figshare": "Figshare",
    "zenodo": "Zenodo",
    "arxiv": "arXiv",
    "osf": "OSF",
    "dataverse": "Dataverse",
    "mendeley": "Mendeley",
    "scopus": "Scopus",
    "researcherid": "ResearcherID",
    "academia": "Academia",
    "impactstory": "Impactstory",
    "loop": "Loop",
    "researchmap": "ResearchMap",
    "slides": "Slides",
    "thesis_link": "Thesis Link",
    "course_link": "Course Link",
    "doi": "DOI",
    "journal": "Journal",
    "conference": "Conference",
}


class Link:
    """
    Links class is used to store the links of the online presence of the user.
    Can be used to store the links of the user's website, LinkedIn profile,
    preprints, etc.
    """

    def __init__(self):
        """
        Initialize the Links class.
        """
        self.type = str()
        self.url = str()

    def get_type(self):
        """
        Get the type of the link.
        """
        return self.type

    def get_url(self):
        """
        Get the URL of the link.
        """
        return self.url

    def __repr__(self):
        return f"Link(type={self.type}, url={self.url})"


class Links:
    """
    Links class is used to store an array of links of the online presence of the user.
    """

    def __init__(self):
        """
        Initialize the Links class.
        """
        self.links: list[Link] = []

    def add_link(self, link: Link):
        """
        Add a link to the list of links.
        """
        self.links.append(link)

    def load(self, df: pd.DataFrame):
        """
        Add links to the list of links.
        """
        for link_type in link_types.values():
            if link_type not in df:
                continue
            if pd.isna(df[link_type]):
                continue
            link = Link()
            link.type = link_type
            link.url = str(df[link_type])
            self.add_link(link)

    def get_links(self):
        """
        Get the list of links.
        """
        return self.links

    def get_link(self, link_type: str):
        """
        Get the link by type.
        """
        for link in self:
            if link.get_type() == link_type:
                return link
        return None

    def __iter__(self):
        return iter(self.links)

    def __repr__(self):
        string = f"links({[repr(link) for link in self.links]})"
        return string
