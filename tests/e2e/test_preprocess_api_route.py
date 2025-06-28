import requests
import pytest

PREPROCESS_URL = "http://127.0.0.1:5000/api/preprocess"


class TestPreprocessAPI:
    def test_preprocess_success(self, get_test_file_path):
        with open(get_test_file_path, "rb") as f:
            files = {'file': f}
            response = requests.post(PREPROCESS_URL, files=files)
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "preview" in data