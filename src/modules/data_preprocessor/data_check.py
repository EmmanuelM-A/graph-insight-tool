from abc import ABC, abstractmethod
import pandas as pd


class DataCheck(ABC):
    """
    Abstract base class for the data checkers. This class defines the interface for
    checking if data meets the implemented conditions.
    """

    @abstractmethod
    def check_data(self, data: pd.DataFrame) -> bool:
        """
        Check if the data meets the implemented conditions.
        """

        raise NotImplementedError("Subclasses must implement this method.")


class DataSanityCheck(DataCheck):
    """
    Concrete implementation of the DataCheck for checking the sanity of data.
    Ensures the DataFrame is non-empty and has valid rows and columns.
    """

    def check_data(self, data: pd.DataFrame) -> bool:
        """
        Check if the data is valid for further processing.
        :param data: The DataFrame to check.
        :return: True if the data is valid, False otherwise.
        """

        if data is None:
            return False

        if data.empty:
            return False

        if data.shape[0] == 0 or data.shape[1] == 0:
            return False

        if all(data[col].isnull().all() for col in data.columns):
            return False

        return True
