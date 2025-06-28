import pandas as pd
from typing_extensions import override

from src.modules.data_preprocessor.data_check import DataCheck
from src.modules.data_preprocessor.data_encoder import DataEncoder
from src.modules.data_preprocessor.data_normalizer import DataNormalizer
from src.modules.data_preprocessor.data_preprocessor import DataPreprocessor
from src.modules.data_preprocessor.data_treatment import DataTreatment


class PreprocessingHandler(DataPreprocessor):
    """
    PreprocessingHandler is responsible for managing the preprocessing of data.
    """

    def __init__(
            self,
            checks: list[DataCheck],
            treatments: list[DataTreatment],
            encoder: DataEncoder = None,
            normalizer: DataNormalizer = None
    ) -> None:
        super().__init__(
            checks=checks,
            treatments=treatments,
            encoder=encoder,
            normalizer=normalizer
        )

    @override
    def run_data_treatments(self, data: pd.DataFrame) -> pd.DataFrame:
        for treatment in self.treatments:
            data = treatment.treat_data(data)
        return data

    @override
    def validate_data(self, data: pd.DataFrame) -> bool:
        return all(check.check_data(data) for check in self.checks)

    @override
    def encode_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

    @override
    def normalize_data(self, data: pd.DataFrame) -> pd.DataFrame:
        pass
