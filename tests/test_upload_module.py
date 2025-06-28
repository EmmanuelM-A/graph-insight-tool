import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.modules.data_uploader.upload_handler import handle_upload, get_loader


class TestUploadModule:
    @patch("src.modules.data_uploader.upload_handler.get_loader")
    def test_handle_upload_success(self, mock_get_loader, get_sample_data):
        # Mock DataLoader
        mock_loader_instance = MagicMock()
        mock_loader_instance.load_data.return_value = (pd.DataFrame(get_sample_data), "Loaded")
        mock_get_loader.return_value = lambda: mock_loader_instance

        data, msg = handle_upload("test.csv")
        assert isinstance(data, pd.DataFrame)
        assert msg == "Loaded"


    @patch("src.modules.data_uploader.upload_handler.get_loader")
    def test_handle_upload_failure(self, mock_get_loader):
        # Simulate loader raising an exception
        mock_loader_instance = MagicMock()
        mock_loader_instance.load_data.side_effect = Exception("Read error")
        mock_get_loader.return_value = lambda: mock_loader_instance

        data, msg = handle_upload("test.csv")
        assert data is None
        assert "Read error" in msg


    def test_get_loader_csv(self):
        loader = get_loader("file.csv")
        assert loader.__name__ == "CSVDataLoader"


    def test_get_loader_excel(self):
        loader = get_loader("file.xlsx")
        assert loader.__name__ == "ExcelDataLoader"


    def test_get_loader_unsupported(self):
        with pytest.raises(ValueError):
            get_loader("file.txt")
