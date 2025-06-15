from abc import ABC, abstractmethod
import pandas as pd

class DataLoader(ABC):
    """
    Abstract base class for data loaders.
    This class defines the interface for loading data from various sources.
    """
    @abstractmethod
    def load_data(self, source: str) -> pd.DataFrame:
        """
        Load data from the specified source.

        :param source: The source from which to load data (e.g., file path, URL).
        :return: A dictionary containing the loaded data.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class CSVDataLoader(DataLoader):
    """
    Concrete implementation of the DataLoader for CSV files.
    """
    def load_data(self, source: str) -> pd.DataFrame:
        pass


class ExcelDataLoader(DataLoader):
    """
    Concrete implementation of the DataLoader for Excel files.
    """
    def load_data(self, source: str) -> pd.DataFrame:
        pass
