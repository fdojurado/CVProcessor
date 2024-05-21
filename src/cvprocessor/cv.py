"""
This module contains the CV class that is used to create a CV object.
The CV object is used to store all the information
"""
import sys

from cvprocessor.intro import Intro
from cvprocessor.education import Educations
from cvprocessor.publications import Publications
from cvprocessor.authors import Authors
from cvprocessor.software import Software
from cvprocessor.institutes import Institutes
from cvprocessor.news import News
from cvprocessor.research_interests import ResearchInterests
from cvprocessor.grants_awards import GrantsAwards
from cvprocessor.teaching import Teaching
from cvprocessor.supervision import Supervision
from cvprocessor.experience import Experience
from cvprocessor.skills import Skills
from cvprocessor.service import Services
from cvprocessor.memberships import Memberships
from cvprocessor.references import References


class AcademicInfo:
    """
    The AcademicInfo class is used to store all the academic information from the CV file.

    :param filename: The filename of the CV file.
    :type filename: str

    :param cv_class: The CV class object.
    :type cv_class: CV
    """

    def __init__(self):
        self.education = Educations()
        self.institutes = Institutes()
        self.research_interests = ResearchInterests()
        self.grants_awards = GrantsAwards()
        self.teaching = Teaching()
        self.supervision = Supervision()
        self.publications = Publications()

    def __str__(self):
        string = f"Education: {self.education}\n"
        string += f"Institutes: {self.institutes}\n"
        string += f"Research Interests: {self.research_interests}\n"
        string += f"Grants & Awards: {self.grants_awards}\n"
        string += f"Teaching: {self.teaching}\n"
        string += f"Supervision: {self.supervision}\n"
        string += f"Publications: {self.publications}\n"
        return string

    def __repr__(self):
        string = (
            f"AcademicInfo("
            f"education={repr(self.education)}, "
            f"institutes={repr(self.institutes)}, "
            f"research_interests={repr(self.research_interests)}, "
            f"grants_awards={repr(self.grants_awards)}, "
            f"teaching={repr(self.teaching)}, "
            f"supervision={repr(self.supervision)}, "
            f"publications={repr(self.publications)})\n")
        return string


class PersonalInfo:
    """
    The PersonalInfo class is used to store all the personal information from the CV file.

    :param filename: The filename of the CV file.
    :type filename: str

    :param cv_class: The CV class object.
    :type cv_class: CV
    """

    def __init__(self):
        self.intro = Intro()
        self.authors = Authors()
        self.references = References()

    def __str__(self):
        string = f"Intro: {self.intro}\n"
        string += f"Authors: {self.authors}\n"
        string += f"References: {self.references}\n"
        return string

    def __repr__(self):
        string = (
            f"PersonalInfo("
            f"intro={repr(self.intro)}, "
            f"authors={repr(self.authors)}, "
            f"references={repr(self.references)})\n")
        return string


class ProfessionalInfo:
    """
    The ProfessionalInfo class is used to store all the professional information from the CV file.

    :param filename: The filename of the CV file.
    :type filename: str

    :param cv_class: The CV class object.
    :type cv_class: CV
    """

    def __init__(self):
        self.experience = Experience()
        self.skills = Skills()
        self.service = Services()
        self.memberships = Memberships()

    def __str__(self):
        string = f"Experience: {self.experience}\n"
        string += f"Skills: {self.skills}\n"
        string += f"Service: {self.service}\n"
        string += f"Memberships: {self.memberships}\n"
        return string

    def __repr__(self):
        string = (
            f"ProfessionalInfo("
            f"experience={repr(self.experience)}, "
            f"skills={repr(self.skills)}, "
            f"service={repr(self.service)}, "
            f"memberships={repr(self.memberships)})\n")
        return string


class CV:
    """
    The CV class is used to create a CV object that stores all the information from the CV file.

    :param filename: The filename of the CV file.
    :type filename: str
    """

    def __init__(self, filename):
        self.professional = ProfessionalInfo()
        self.personal = PersonalInfo()
        self.academic = AcademicInfo()
        self.software = Software()
        self.news = News()
        self._load_cv(filename)

    def get_publications_apa_citation(self, publication_title):
        """
        The get_publications_apa_citation method is used to get the APA citation of the publication.

        :param publication_title: The title of the publication.
        :type publication_title: str
        """
        pub = self.academic.publications.get_publication_by_title(
            publication_title)
        if pub is None:
            return None
        apa = pub.get_apa_citation()
        authors_ids_affiliations_ids = pub.get_auth_id_aff_id()
        authors_ids = []
        for author_id in authors_ids_affiliations_ids:
            authors_ids.append(author_id.get_author_id())
        authors_alias_short = []
        for author_id in authors_ids:
            author = self.personal.authors.get_author(author_id)
            if author is not None:
                authors_alias_short.append(author.personal.get_alias())
        if len(authors_alias_short) > 1:
            authors_alias_short[-1] = "& " + authors_alias_short[-1]
        authors_alias_short = ", ".join(authors_alias_short)
        apa = authors_alias_short + " " + apa
        return apa

    def _load_cv(self, filename):
        """
        The _load_cv method is used to load the CV file.

        :param filename: The filename of the CV file.
        :type filename: str
        """
        self.academic.education.load(filename)
        self.academic.institutes.load(filename)
        self.software.load(filename)
        self.personal.intro.load(filename)
        self.personal.authors.load(filename)
        self.news.load(filename)
        self.academic.publications.load(filename)
        self.academic.research_interests.load(filename)
        self.academic.grants_awards.load(filename)
        self.academic.teaching.load(filename)
        self.academic.supervision.load(filename)
        self.professional.experience.load(filename)
        self.professional.skills.load(filename)
        self.professional.service.load(filename)
        self.professional.memberships.load(filename)
        self.personal.references.load(filename)

    def __str__(self):
        string = f"Academic Info: {self.academic}\n"
        string += f"Personal Info: {self.personal}\n"
        string += f"Professional Info: {self.professional}\n"
        string += f"Software: {self.software}\n"
        string += f"News: {self.news}\n"
        return string

    def __repr__(self):
        string = (
            f"CV("
            f"academic={repr(self.academic)}, "
            f"personal={repr(self.personal)}, "
            f"professional={repr(self.professional)}, "
            f"software={repr(self.software)}, "
            f"news={repr(self.news)})\n")
        return string


if __name__ == "__main__":
    cv = CV("cv.xlsx")
    print(str(cv.academic.education))
    # Get the first publication
    # pub = cv.academic.publications.get_publications_by_index(0)
    # print(f"Publication title: {pub.details.get_title()}")
    # apa = cv.get_publications_apa_citation(pub.details.get_title())
    # print(f"APA Citation: {apa}")
    sys.exit(0)
