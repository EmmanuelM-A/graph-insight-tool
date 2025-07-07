"""
Data Profile
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional, List
from abc import ABC


class Profile(ABC):
    """
    Represents a standard profile class hold data about the specified subject.
    """

    def to_json(self):
        """
        Converts the profile into a json readable format.
        """

    def to_dict(self):
        """
        Convert the input data into a dictionary.
        """


@dataclass
class ColumnProfile(Profile):
    """
    Concrete class
    """

    def __init__(self):
        super().__init__()
        self.column_name: str  = ""
        self.column_classification: str = ""
        self.cardinality: int = 0
        self.uniqueness_ratio: float = 0.0
        self.missing_values: int = 0
        self.missing_percentage: float = 0.0
        self.is_binary: bool = False
        self.is_time_series: bool = False
        self.potential_role: List[str] = []
        self.statistics: Optional[Dict[str, Any]] = None

    def to_json(self):
        pass

    def to_dict(self):
        pass


class DataProfile(Profile):
    """
    Represents the metadata of a pandas DataFrame.
    """


    def __init__(self):
        self.num_columns = 0
        self.num_rows = 0
        self.column_profiles = []
        self.column_classifications = []
        self.any_binary_columns = []
        self.any_time_series = []
        self.inter_column_relationships = []
        self.semantic_hints = []
        self.sample_records = []


    def __str__(self):
        pass

    def __len__(self):
        pass

    def to_json(self):
        pass

    def to_dict(self):
        pass
