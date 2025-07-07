"""
Data Profile
"""
from dataclasses import dataclass

from src.services.extractor.profiler.profile import Profile


@dataclass
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
