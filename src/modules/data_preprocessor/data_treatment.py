from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

class DataTreatment(ABC):
    """
    Abstract base class for data treatment.
    This class defines the interface for treating data.
    """
    @abstractmethod
    def treat_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Treat the data according to the implemented treatment.

        :param data: The DataFrame to treat.
        :return: A treated DataFrame.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class GarbageValueTreatment(DataTreatment):
    """
    Concrete implementation of the DataTreatment for garbage value treatment.

    Removes columns with all nulls, all constant values, or suspicious values like empty strings or 'N/A'.
    """

    def treat_data(self, data: pd.DataFrame) -> pd.DataFrame:
        # Drop columns with all null values
        data = data.dropna(axis=1, how='all')

        # Drop columns where all values are the same (e.g., constant)
        data = data.loc[:, data.apply(pd.Series.nunique) > 1]

        # Strip and replace known garbage strings with NaN
        garbage_strings = ["", " ", "N/A", "n/a", "NULL", "null", "-", "--"]
        data.replace(garbage_strings, np.nan, inplace=True)

        return data


class MissingValueTreatment(DataTreatment):
    """
    Concrete implementation of the DataTreatment for missing value treatment.

    Fills missing values using mean for numeric and mode for categorical columns.
    """

    def treat_data(self, data: pd.DataFrame) -> pd.DataFrame:
        for col in data.columns:
            if data[col].isnull().any():
                if pd.api.types.is_numeric_dtype(data[col]):
                    data[col].fillna(data[col].mean(), inplace=True)
                else:
                    data[col].fillna(data[col].mode()[0], inplace=True)
        return data


class OutlierTreatment(DataTreatment):
    """
    Concrete implementation of the DataTreatment for outlier treatment.

    Removes outliers using the IQR method for numeric columns.
    """

    def treat_data(self, data: pd.DataFrame) -> pd.DataFrame:
        for col in data.select_dtypes(include=['number']).columns:
            Q1 = data[col].quantile(0.25)
            Q3 = data[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]
        return data


class DuplicateTreatment(DataTreatment):
    """
    Concrete implementation of the DataTreatment for duplicate treatment.

    Removes duplicate rows from the dataset.
    """

    def treat_data(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop_duplicates()