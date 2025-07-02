import pytest

@pytest.fixture
def get_sample_data():
    """Returns sample data."""
    return {"a": [1, 2, 3], "b": [4, 5, 6]}
