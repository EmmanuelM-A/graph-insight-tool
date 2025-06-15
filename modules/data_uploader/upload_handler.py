import pandas as pd

from data_loader import DataLoader, CSVDataLoader, ExcelDataLoader

class UploadHandler:
    """
    Handles file uploads and data loading.
    """

    def __init__(self):
        self.data = None
        self.message = ""

    def handle_upload(self, filepath: str) -> pd.DataFrame:
        pass

    def _get_loader(self, filepath: str) -> DataLoader:
        pass
