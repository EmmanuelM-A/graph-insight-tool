import pandas as pd

class PreprocessingHandler:
    """
    PreprocessingHandler is responsible for managing the preprocessing of data.
    """
    
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data
        self.__data_treatments = []
        self.__data_checks = []
        self.__encoders = []
        self.__normalizers = []

    def preprocess_data(self) -> pd.DataFrame:
        pass