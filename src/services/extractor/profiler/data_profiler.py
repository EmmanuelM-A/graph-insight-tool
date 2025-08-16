"""
This module is responsible for generating a full profile of a DataFrame
by extracting schema, distributional, and statistical insights and storing
them in a `DataProfile` and `ColumnProfile` data containers.
"""

from typing import List

import numpy as np
import pandas as pd

from src.services.extractor.profiler.data_profile import (
    DataProfile,
    ColumnProfile
)


class DataProfiler:
    """
    Profiles tabular data and extracts features such as column types,
    statistics, cardinality, null distribution, and inferred relationships.
    Stores results into DataProfile and ColumnProfile objects.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initialize with the DataFrame to be profiled.

        :param data: A pandas DataFrame
        """

        self.data = data.copy()

    def generate_profile(self) -> DataProfile:
        """
        Main method to generate a full data profile.
        :return: DataProfile object populated with profiling information.
        """


        # TODO FIX THIS FILE SO IT PROFILE CONTAINS THE RIGHT INFO
        # TODO LOOK INTO THE DATAPREP.EDA LIBRARY AND FIND OUT HOW IT WORKS

        profile = DataProfile()

        profile.num_rows = self.data.shape[0]

        profile.num_columns = self.data.shape[1]

        profile.sample_records = self.data.head(5).to_dict(orient="records")

        for col in self.data.columns:
            profile.column_profiles.append(self._profile_column(col))

        profile.column_classifications = (
            self._get_column_classification_summary(profile.column_profiles)
        )

        profile.any_binary_columns = \
            [
                col.column_name for col in profile.column_profiles
                if col.is_binary
            ]

        profile.any_time_series = \
            [
                col.column_name for col in profile.column_profiles
                if col.is_time_series
            ]

        profile.inter_column_relationships = self._infer_correlation()

        return profile

    def _profile_column(self, col: str) -> ColumnProfile:
        """
        Extract column-level metadata and statistics.

        :param col: column name
        :return: ColumnProfile object
        """
        s = self.data[col]
        cp = ColumnProfile()

        cp.column_name = col

        cp.column_classification = str(s.dtype)

        cp.cardinality = s.nunique(dropna=True)

        cp.uniqueness_ratio = (
                cp.cardinality / len(s)) if len(s) > 0 else 0.0

        cp.missing_values = s.isna().sum()

        cp.missing_percentage = (
                cp.missing_values / len(s) * 100) if len(s) > 0 else 0.0

        cp.is_binary = cp.cardinality == 2

        cp.is_time_series = pd.api.types.is_datetime64_any_dtype(s)

        cp.potential_role = self._infer_roles(s, cp)

        if pd.api.types.is_numeric_dtype(s):
            cp.statistics = {
                "mean": s.mean(),
                "std": s.std(),
                "min": s.min(),
                "max": s.max(),
                "skewness": s.skew(),
                "kurtosis": s.kurt(),
                "zero_count": int((s == 0).sum())
            }
        else:
            cp.statistics = {}

        return cp

    def _infer_roles(self, s: pd.Series, cp: ColumnProfile) -> List[str]:
        """
        Heuristics to infer potential roles of a column.

        :param s: Column as pandas Series
        :param cp: ColumnProfile object
        :return: List of inferred roles
        """
        roles = []
        if cp.is_time_series:
            roles.append("timestamp")
        elif cp.is_binary:
            roles.append("binary_class")
        elif cp.uniqueness_ratio > 0.9:
            roles.append("identifier")
        elif pd.api.types.is_numeric_dtype(s):
            roles.append("measure")
        else:
            roles.append("dimension")
        return roles

    def _get_column_classification_summary(
            self,
            profiles: List[ColumnProfile]
    ) -> List[tuple]:
        """
        Summarize data type distributions across the DataFrame.
        :param profiles: list of ColumnProfiles
        :return: list of (data_type, count, percentage)
        """

        dtype_counts = {}
        for p in profiles:
            dtype = p.column_classification
            dtype_counts[dtype] = dtype_counts.get(dtype, 0) + 1

        total = sum(dtype_counts.values())

        return [
            (dtype, count, round(count / total * 100, 2))
            for dtype, count in dtype_counts.items()
        ]

    def _infer_correlation(self) -> List[dict]:
        """
        Infer relationships between numeric columns using correlation.
        :return: List of correlation insights
        """

        numeric_df = self.data.select_dtypes(include=np.number)

        if numeric_df.shape[1] < 2:
            return []

        corr = numeric_df.corr()
        results = []
        for i, col1 in enumerate(corr.columns):
            for j, col2 in enumerate(corr.columns):
                if j > i:
                    corr_val = corr.iloc[i, j]
                    if abs(corr_val) > 0.5:
                        results.append({
                            "column_pair": (col1, col2),
                            "correlation": round(corr_val, 3)
                        })

        return results


if __name__ == "__main__":

    SOURCE = "../../../../tests/test_data_files/test-data-0.csv"

    test_data = pd.read_csv(SOURCE)

    profiler = DataProfiler(test_data)

    profiled_data = profiler.generate_profile()

    print(profiled_data.to_json())
