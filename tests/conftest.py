import pytest

TEST_FILE_PATH = "tests/test_data_files/test-data-0.csv"

@pytest.fixture
def get_sample_data():
    """
    Fixture to provide sample data for tests.
    """
    return {"a": [1, 2]}


@pytest.fixture
def get_test_file_path():
    return TEST_FILE_PATH
