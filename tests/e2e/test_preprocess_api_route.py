"""Test for the preprocess API route."""

import requests

PREPROCESS_URL = "http://127.0.0.1:5000/api/preprocess"


class TestPreprocessAPI:
    """Test class for the preprocess API route."""

    def test_preprocess_api_endpoint(self, get_test_file_path):
        """Test the preprocess API endpoint with a valid file upload."""
        with open(get_test_file_path, "rb") as f:
            files = {'file': f}
            response = requests.post(PREPROCESS_URL, files=files)
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "preview" in data
