"""
Profiles the data.
"""
import pandas as pd


class DataProfiler:
    """
    Profiles the data.
    """

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def generate_profile(self):
        pass

    def get_scheme_features(self):
        pass

    def get_column_distribution_features(self):
        pass

    def infer_relation(self):
        pass
