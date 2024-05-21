"""
This module contains the Security class.
"""

class Security:
    """
    A class to represent the security details of an author.

    Attributes:
    fingerprint (str): The fingerprint of the author.
    public_key (str): The public key of the author.
    """

    def __init__(self):
        self.fingerprint = str()
        self.public_key = str()

    def get_fingerprint(self):
        """
        Returns the fingerprint of the author.
        """
        return self.fingerprint

    def get_public_key(self):
        """
        Returns the public key of the author.
        """
        return self.public_key

    def load(self, filename):
        """
        Loads the security details of the author.
        """
        self.fingerprint = filename["Fingerprint"]
        self.public_key = filename["Public Key"]

    def __repr__(self):
        string = (
            f"Security("
            f"fingerprint={self.fingerprint}, "
            f"public_key={self.public_key})"
        )
        return string
