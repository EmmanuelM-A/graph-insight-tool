"""Test for the preprocess API route."""

import requests

PREPROCESS_URL = "http://127.0.0.1:5000/api/preprocess"
TEST_FILE_PATH = "tests/test_data_files/test-data-0.csv"


class TestPreprocessAPI:
    """Test class for the preprocess API route."""

    def test_preprocess_api_endpoint(self):
        """Test the preprocess API endpoint with a valid file upload."""
        with open(TEST_FILE_PATH, "rb") as f:
            files = {'file': f}
            response = requests.post(PREPROCESS_URL, files=files)
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert "message" in data
