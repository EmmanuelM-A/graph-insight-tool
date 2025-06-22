import pandas as pd
from presidio_structured import PandasAnalysisBuilder

def check_sensitivity(data: pd.DataFrame) -> bool:
    """
    Check if the data does not contain any sensitive information.

    :param data: DataFrame to check.
    :return: True if data contains sensitive information, False otherwise.
    """

    # Generate a tabular analysis which describes PII entities in the DataFrame.
    tabular_analysis = PandasAnalysisBuilder().generate_analysis(data)

    if tabular_analysis:
        return True
    else:
        return False
