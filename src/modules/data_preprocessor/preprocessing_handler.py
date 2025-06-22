import pandas as pd
from src.modules.data_preprocessor.data_preprocessor import DataPreprocessor


class PreprocessingHandler(DataPreprocessor):
    """
    PreprocessingHandler is responsible for managing the preprocessing of data.
    """
    
    def __init__(self) -> None:
        super().__init__()

    def run_data_treatments(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

    def run_data_checks(self, data: pd.DataFrame) -> bool:
        pass

    def encode_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

    def normalize_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass






