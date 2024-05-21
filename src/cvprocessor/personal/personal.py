"""
The personal module contains the Personal class.
"""


class Personal:
    """
    A class to represent the personal information of an institute/authors.

    Attributes:
    Name (str): The name of the institute/author.
    Lastname (str): The lastname of the author.
    PreferredName (str): The preferred name of the author.
    Alias (str): The alias of the author.
    """

    def __init__(self):
        self.name = str()
        self.lastname = str()
        self.preferredname = str()
        self.alias = str()

    def get_name(self):
        """
        Get the name of the institute/author.
        """
        return self.name

    def get_lastname(self):
        """
        Get the lastname of the author.
        """
        return self.lastname

    def get_preferred_name(self):
        """
        Get the preferred name of the author.
        """
        return self.preferredname

    def get_alias(self):
        """
        Get the alias of the author.
        """
        return self.alias

    def load(self, df):
        """
        Load the institute/author information.
        """
        self.name = df["Name"]
        self.lastname = df["Lastname"]
        self.preferredname = df["Preferred Name"]
        self.alias = df["Alias"]

    def __repr__(self):
        string = (
            f"Personal("
            f"name={self.name}, "
            f"lastname={self.lastname}, "
            f"preferredName={self.preferredname}, "
            f"alias={self.alias})"
        )
        return string
