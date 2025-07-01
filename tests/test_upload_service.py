"""Test suite for the upload service"""

import io
from unittest.mock import patch

import pytest

from src.controllers.upload_controller import process_upload_request
from src.exceptions import api_exceptions as ae
from src.modules.data_uploader.upload_handler import get_loader


class TestUploadService:
    """Unit tests for the test service"""

    @patch("src.controllers.upload_controller.UploadFile")
    async def test_upload_failure_no_file_selected(
            self,
            mock_upload_file
    ) -> None:
        """
        Should raise a bad request exception if no file was provided.
        """

        # Simulate no file provided
        mock_upload_file.filename = ""

        with pytest.raises(ae.BadRequestException) as exc_info:
            await pytest.run(process_upload_request(file=mock_upload_file))

        assert exc_info.value.status_code == 400
        assert isinstance(exc_info.value, ae.BadRequestException)
        assert "No file selected" in str(exc_info.value.detail)

    @patch("src.controllers.upload_controller.UploadFile")
    async def test_upload_failure_invalid_file_format(
            self,
            mock_upload_file
    ) -> None:
        """
        Should raise a bad request exception if file is in the wrong format.
        """

        mock_upload_file.filename = "file.unsupported"

        with pytest.raises(ae.BadRequestException) as exc_info:
            await process_upload_request(file=mock_upload_file)

        assert exc_info.value.status_code == 400
        assert isinstance(exc_info.value, ae.BadRequestException)
        assert "Invalid file format" in str(exc_info.value.detail)

    @patch("src.controllers.upload_controller.handle_upload")
    @patch("src.controllers.upload_controller.UploadFile")
    async def test_upload_failure_read_data_failure(
            self,
            mock_upload_file,
            mock_handle_upload
    ) -> None:
        """
        Should return an upload exception if something goes wrong during the
        file read.
        """

        # Simulate valid file
        mock_upload_file.filename = "file.csv"
        mock_upload_file.file = io.BytesIO(b"some,data\n1,2")

        # Simulate handle_upload raising an exception
        mock_handle_upload.side_effect = Exception("Read error")

        with pytest.raises(ae.UploadException) as exc_info:
            await process_upload_request(file=mock_upload_file)

        assert "Read error" in str(exc_info.value.detail)

    @patch("src.controllers.upload_controller.handle_upload")
    @patch("src.controllers.upload_controller.UploadFile")
    async def test_upload_failure_handle_upload_failure(
            self,
            mock_upload_file,
            mock_handle_upload
    ) -> None:
        """
        Should return something if the handle_upload fails during operation.
        """

        # Simulate valid file
        mock_upload_file.filename = "file.csv"
        mock_upload_file.file = io.BytesIO(b"some,data\n1,2")

        # Simulate handle_upload returning (None, "error message")
        mock_handle_upload.return_value = (None, "No data found")

        with pytest.raises(ae.BadRequestException) as exc_info:
            await process_upload_request(file=mock_upload_file)

        assert "No data found" in str(exc_info.value.detail)

    @patch("src.controllers.upload_controller.handle_upload")
    @patch("src.controllers.upload_controller.UploadFile")
    async def test_upload_failure_no_data_exists(
            self,
            mock_upload_file,
            mock_handle_upload
    ) -> None:
        """
        Should raise a bad request exception if the read file contains no
        data.
        :return:
        """

        # Simulate valid file
        mock_upload_file.filename = "file.csv"
        mock_upload_file.file = io.BytesIO(b"some,data\n1,2")

        # Simulate handle_upload returning (None, "No data")
        mock_handle_upload.return_value = (None, "No data")

        with pytest.raises(ae.BadRequestException) as exc_info:
            await process_upload_request(file=mock_upload_file)

        assert "No data" in str(exc_info.value.detail)

    async def test_upload_success_handle_upload_success(
            self,
            mock_upload_file,
            mock_handle_upload
    ) -> None:
        """
        Should return the correct metadata.
        :return:
        """

        # Simulate valid file
        mock_upload_file.filename = "file.csv"
        mock_upload_file.file = io.BytesIO(b"some,data\n1,2")

        # Simulate handle_upload returning (data, message)
        mock_data = {"a": [1, 2]}
        mock_handle_upload.return_value = (mock_data, "Loaded")
        result = await process_upload_request(file=mock_upload_file)

        assert result["message"].startswith(
            "The file 'file.csv' has been uploaded")
        assert result["data"] == mock_data

    async def test_get_loader_success_get_csv_loader(self) -> None:
        """
        Should return the CSV data loader.
        :return:
        """

        loader = get_loader("file.csv")
        assert loader.__name__ == "CSVDataLoader"

    async def test_get_loader_success_get_excel_loader(self) -> None:
        """
        Should return the Excel data loader.
        :return:
        """

        loader = get_loader("file.xlsx")
        assert loader.__name__ == "ExcelDataLoader"

    async def test_get_loader_failure_unsupported_loader(self) -> None:
        """
        Should raise a ValueError if the no loader for the file is found.
        :return:
        """

        with pytest.raises(ValueError):
            get_loader("file.txt")
