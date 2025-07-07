"""
Base class which defines a standard profile class.
"""

from abc import ABC

class Profile(ABC):
    """
    Represents a standard profile class hold data about the specified subject.
    """

    def to_json(self):
        """
        Converts the data profile into a json readable format.
        """

    def to_dict(self):
        """
        Convert the input data into a dictionary.
        """
