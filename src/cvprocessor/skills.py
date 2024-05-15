"""
This module contains the classes to handle the skills data.
"""
import pandas as pd


class SkillData:
    """
    The SkillData class is used to store the skill data.

    Attributes:
    type (str): The type of the skill.
    skill (str): The skill.
    level (str): The level of the skill.
    """

    def __init__(self):
        self.type = None
        self.skill = None
        self.level = None

    def get_type(self):
        """
        Get the type of the skill.
        """
        return self.type

    def get_skill(self):
        """
        Get the skill.
        """
        return self.skill

    def get_level(self):
        """
        Get the level of the skill.
        """
        return self.level

    def load(self, filename):
        """
        Load the skill data.
        """
        self.type = filename["Type"]
        self.skill = filename["Skill"]
        self.level = filename["Level"]

    def __str__(self) -> str:
        string = f"Type: {self.type}\n"
        string += f"Skill: {self.skill}\n"
        string += f"Level: {self.level}\n"
        return string

    def __repr__(self) -> str:
        string = (
            f"SkillData("
            f"type={self.type}, "
            f"skill={self.skill}, "
            f"level={self.level})"
        )
        return string


class Skills:
    """
    The Skills class is used to store the skills data.

    Attributes:
    skills (list): The list of skills.

    Methods:
    get_skill_types_ordered(): Get the skill types in order.
    get_num_skills_except_type(): Get the number of skills except for the given type.
    get_num_skills_by_type(): Get the number of skills by the given type.
    get_skill_type(): Get the skills by the given type.
    load(): Load the skills data.
    """

    def __init__(self):
        self.skills = []

    def get_skill_types_ordered(self):
        """
        Get the skill types in order.
        """
        skill_type = []
        for skill in self.skills:
            if skill.type not in skill_type:
                skill_type.append(skill.type)
        return skill_type

    def get_num_skills_except_type(self, skill_type):
        """
        Get the number of skills except for the given type.
        """
        return len([skill for skill in self.skills if skill.type != skill_type])

    def get_num_skills_by_type(self, skill_type):
        """
        Get the number of skills by the given type.
        """
        return len(self.get_skill_type(skill_type))

    def get_skill_type(self, skill_type: str):
        """
        Get the skills by the given type.
        """
        return [skill for skill in self.skills if skill.type == skill_type]

    def load(self, filename):
        """
        Load the skills data.
        """
        skills_pd = pd.read_excel(filename, sheet_name="Skills")
        for _, row in skills_pd.iterrows():
            skill_data = SkillData()
            skill_data.load(row)
            self.skills.append(skill_data)

    def __str__(self):
        string = ""
        for skill in self.skills:
            string += str(skill) + "\n"
        return string

    def __repr__(self):
        string = f"Skills(skills={repr(list(self.skills))})"
        return string

    def __iter__(self):
        return iter(self.skills)
