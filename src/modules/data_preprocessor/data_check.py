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
    """

    def check_data(self, data: pd.DataFrame) -> bool:
        pass
