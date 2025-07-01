"""Test suite for the PreprocessingHandler module."""

import pytest
import pandas as pd
from src.services.data_preprocessor.data_normalizer import DataNormalizer
from src.services.data_preprocessor.preprocessing_handler import PreprocessingHandler
from src.services.data_preprocessor.data_check import DataCheck
from src.services.data_preprocessor.data_treatment import DataTreatment
from src.services.data_preprocessor.data_encoder import DataEncoder

class DummyCheck(DataCheck):
    def check_data(self, data):
        return True

class FailingCheck(DataCheck):
    def check_data(self, data):
        return False

class DummyTreatment(DataTreatment):
    def treat_data(self, data):
        data = data.copy()
        data["treated"] = 1
        return data

class DummyNormalizer(DataNormalizer):
    def normalize(self, data):
        data = data.copy()
        data["normalized"] = data.mean(axis=1)
        return data

class DummyEncoder(DataEncoder):
    def encode(self, data):
        data = data.copy()
        data["encoded"] = 42
        return data

class TestPreprocessorModule:
    def test_preprocess_success(self, get_sample_data):
        df = pd.DataFrame(get_sample_data)
        handler = PreprocessingHandler(
            checks=[DummyCheck()],
            treatments=[DummyTreatment()],
        )
        result = handler.preprocess_data(df)
        assert "treated" in result.columns

    def test_preprocess_fails_validation(self, get_sample_data):
        df = pd.DataFrame(get_sample_data)
        handler = PreprocessingHandler(
            checks=[FailingCheck()],
            treatments=[DummyTreatment()]
        )
        with pytest.raises(ValueError):
            handler.preprocess_data(df)

    def test_treatments_are_applied(self, get_sample_data):
        df = pd.DataFrame(get_sample_data)
        handler = PreprocessingHandler(
            checks=[DummyCheck()],
            treatments=[DummyTreatment(), DummyTreatment()]
        )
        result = handler.preprocess_data(df)
        # Should only add 'treated' column once, as DummyTreatment overwrites it
        assert "treated" in result.columns
