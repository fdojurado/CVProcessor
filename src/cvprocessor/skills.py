import pandas as pd


class SkillData:
    def __init__(self, filename):
        self._filename = filename
        self._type = None
        self._skill = None
        self._level = None
        self._load_skills()

    @property
    def filename(self):
        return self._filename

    @property
    def type(self):
        return self._type

    @property
    def skill(self):
        return self._skill

    @property
    def level(self):
        return self._level

    def _load_skills(self):
        self._type = self.filename["Type"]
        self._skill = self.filename["Skill"]
        self._level = self.filename["Level"]

    def __str__(self) -> str:
        string = f"Type: {self.type}\n"
        string += f"Skill: {self.skill}\n"
        string += f"Level: {self.level}\n\n"
        return string

    def __repr__(self) -> str:
        repr = f"SkillData(type={self.type}, skill={self.skill}, level={self.level})"
        return repr


class Skills:
    def __init__(self, filename):
        self._filename = filename
        self._skills = self._load_skills()
        self._skills = sorted(self.skills, key=lambda x: (x.type, x.skill))

    @property
    def filename(self):
        return self._filename

    @property
    def skills(self):
        return self._skills

    def get_skill_types_ordered(self):
        skill_type = []
        for skill in self.skills:
            if skill.type not in skill_type:
                skill_type.append(skill.type)
        return skill_type

    def get_num_skills_except_type(self, skill_type):
        return len([skill for skill in self.skills if skill.type != skill_type])

    def get_num_skills_by_type(self, skill_type):
        return len(self.get_skill_type(skill_type))

    def get_skill_type(self, skill_type: str):
        return [skill for skill in self.skills if skill.type == skill_type]

    def _load_skills(self):
        skills_pd = pd.read_excel(self.filename, sheet_name="Skills")
        return [SkillData(skill) for _, skill in skills_pd.iterrows()]

    def __str__(self):
        string = ""
        for skill in self.skills:
            string += str(skill)
        return string

    def __repr__(self):
        repr = f"Skills(filename={self.filename}, skills={self.skills})"
        return repr
