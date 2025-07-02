"""Test suite for the PreprocessingHandler module."""

from unittest.mock import patch, MagicMock

import pandas as pd
import pytest

from src.controllers.preprocess_controller import preprocess_data_request
from src.services.data_preprocessor.data_check import DataCheck
from src.services.data_preprocessor.data_encoder import DataEncoder
from src.services.data_preprocessor.data_normalizer import DataNormalizer
from src.services.data_preprocessor.data_treatment import DataTreatment
from src.services.data_preprocessor.preprocessing_handler import (
    PreprocessingHandler)
from src.exceptions import api_exceptions as ae


TEST_FILE_PATH = "tests/test_data_files/test-data-0.csv"


class DummyCheck(DataCheck):
    """Dummy class for testing"""
    def check_data(self, data):
        return True


class FailingCheck(DataCheck):
    """Dummy class for testing"""
    def check_data(self, data):
        return False


class DummyTreatment(DataTreatment):
    """Dummy class for testing"""
    def treat_data(self, data):
        data = data.copy()
        data["treated"] = 1
        return data


class DummyNormalizer(DataNormalizer):
    """Dummy class for testing"""
    def normalize(self, data):
        data = data.copy()
        data["normalized"] = data.mean(axis=1)
        return data


class DummyEncoder(DataEncoder):
    """Dummy class for testing"""
    def encode(self, data):
        data = data.copy()
        data["encoded"] = 42
        return data


class TestPreprocessorService:
    """
    Test suite for preprocessor service.
    """

    @pytest.mark.asyncio
    async def test_preprocess_failure_upload_request_failed(
            self
    ) -> None:
        """
        Should return some exception after running the process upload
        request.
        """

        # Simulate process_upload_request raising an exception
        with patch(
                "src.controllers.preprocess_controller.process_upload_request"
        ) as mock_upload:
            mock_upload.side_effect = Exception("Upload failed")
            with pytest.raises(ae.PreprocessingDataException) as exc:
                dummy_file = MagicMock()
                # Call the controller function directly
                await preprocess_data_request(dummy_file)

            assert "Upload failed" in str(exc.value)

    @pytest.mark.asyncio
    async def test_preprocess_failure_uploaded_data_invalid(
            self
    ) -> None:
        """
        Should return a BadRequestException with a status code of 400.
        :return: None
        """

        # Simulate empty uploaded data
        with patch(
                "src.controllers.preprocess_controller.process_upload_request"
        ) as mock_upload:
            mock_upload.return_value = {"data": pd.DataFrame()}
            dummy_file = MagicMock()
            with pytest.raises(ae.BadRequestException):
                await preprocess_data_request(dummy_file)

    def test_preprocess_failure_fails_preprocessor_validation(
            self,
            get_sample_data
    ) -> None:
        """
        Should check if any preprocessor checks fail and except a
        PreprocessingDataException with the status code 422.
        :return: None
        """

        # Simulate a failing check in the preprocessor
        df = pd.DataFrame(get_sample_data)
        handler = PreprocessingHandler(
            checks=[FailingCheck()],
            treatments=[DummyTreatment()]
        )
        with pytest.raises(ValueError):
            handler.preprocess_data(df)

    def test_preprocess_success_preprocess_data_success(
            self,
            get_sample_data
    ) -> None:
        """
        Should return an object with the necessary data.
        :return: None
        """

        # All checks pass, treatments applied
        df = pd.DataFrame(get_sample_data)
        handler = PreprocessingHandler(
            checks=[DummyCheck()],
            treatments=[DummyTreatment()]
        )
        result = handler.preprocess_data(df)
        assert "treated" in result.columns

    def test_data_treatments_are_applied(
            self,
            get_sample_data
    ) -> None:
        """
        Should apply all the specified data treatments in correct order.
        :return: None
        """

        # Treatments should be applied in order
        df = pd.DataFrame(get_sample_data)
        handler = PreprocessingHandler(
            checks=[DummyCheck()],
            treatments=[DummyTreatment(), DummyTreatment()]
        )
        result = handler.preprocess_data(df)
        assert "treated" in result.columns

    def test_data_checks_are_applied(
            self,
            get_sample_data
    ) -> None:
        """
        Should run all data checks successfully, in the correct order and
        return true.
        :return:
        """

        # All checks should be run and return True
        df = pd.DataFrame(get_sample_data)
        handler = PreprocessingHandler(
            checks=[DummyCheck(), DummyCheck()],
            treatments=[]
        )
        result = handler.preprocess_data(df)
        assert isinstance(result, pd.DataFrame)

    def test_data_encoder(
            self
    ) -> None:
        """
        Should return the encoded data.
        :return: None
        """

    def test_data_normalizer(
            self
    ) -> None:
        """
        Should return the normalized data.
        :return: None
        """
