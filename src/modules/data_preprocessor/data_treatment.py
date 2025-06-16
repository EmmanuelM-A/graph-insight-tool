from abc import ABC, abstractmethod
import pandas as pd

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
    """

    def treat_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass


class MissingValueTreatment(DataTreatment):
    """
    Concrete implementation of the DataTreatment for missing value treatment.
    """

    def treat_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass


class OutlierTreatment(DataTreatment):
    """
    Concrete implementation of the DataTreatment for outlier treatment.
    """

    def treat_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass


class DuplicateTreatment(DataTreatment):
    """
    Concrete implementation of the DataTreatment for duplicate treatment.
    """

    def treat_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Remove duplicate rows from the DataFrame.

        :param data: The DataFrame to treat.
        :return: A DataFrame with duplicates removed.
        """
        return data.drop_duplicates()