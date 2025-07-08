"""
Data Profile
"""
import json
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

    def to_dict(self):
        return {
            "column_name": self.column_name,
            "column_classification": self.column_classification,
            "cardinality": self.cardinality,
            "uniqueness_ratio": self.uniqueness_ratio,
            "missing_values": self.missing_values,
            "missing_percentage": self.missing_percentage,
            "is_binary": self.is_binary,
            "is_time_series": self.is_time_series,
            "potential_role": self.potential_role,
            "statistics": self.statistics,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), default=str, indent=4)


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

    def to_dict(self):
        return {
            "num_columns": self.num_columns,
            "num_rows": self.num_rows,
            "column_profiles": [cp.to_dict() for cp in self.column_profiles],
            "column_classifications": self.column_classifications,
            "any_binary_columns": self.any_binary_columns,
            "any_time_series": self.any_time_series,
            "inter_column_relationships": self.inter_column_relationships,
            "semantic_hints": self.semantic_hints,
            "sample_records": self.sample_records,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), default=str, indent=4)
