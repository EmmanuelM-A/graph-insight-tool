from abc import ABC, abstractmethod
import pandas as pd


class DataLoader(ABC):
    """
    Abstract base class for data loaders.
    This class defines the interface for loading data from various sources.
    """
    @abstractmethod
    def load_data(self, source: str) -> tuple[pd.DataFrame | None, str]:
        """
        Load data from the specified source.

        :param source: The source from which to load data (e.g., file path, URL).
        :return: A dictionary containing the loaded data.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def __str__(self):
        """
        String representation of the DataLoader.
        :return: A string indicating the type of data loader.
        """
        return f"{self.__class__.__name__} DataLoader"


class CSVDataLoader(DataLoader):
    """
    Concrete implementation of the DataLoader for CSV files.
    """
    def load_data(self, source: str) -> tuple[pd.DataFrame | None, str]:
        try:
            df = pd.read_csv(source)
            return df, "CSV file loaded successfully."
        except Exception as e:
            return None, f"Failed to load CSV file: {str(e)}"


class ExcelDataLoader(DataLoader):
    """
    Concrete implementation of the DataLoader for Excel files.
    """
    def load_data(self, source: str) -> tuple[pd.DataFrame | None, str]:
        try:
            df = pd.read_excel(source)
            return df, "Excel file loaded successfully."
        except Exception as e:
            return None, f"Failed to load Excel file: {str(e)}"
