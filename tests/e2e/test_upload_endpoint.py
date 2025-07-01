"""The test suite for the upload request endpoint"""

import requests

UPLOAD_URL = "http://127.0.0.1:5000/api/upload/"

TEST_FILE_PATH = "tests/test_data_files/test-data-0.csv"


class TestUploadAPI:
    """Upload test class"""
    def test_upload_api_endpoint(self):
        """Should return the correct data"""

        with open(TEST_FILE_PATH, "rb") as f:
            files = {'file': f}
            response = requests.post(UPLOAD_URL, files=files)

        assert response.status_code == 200

        data = response.json()

        assert "message" in data
        assert data["message"] == "The file has been uploaded successfully!"
        assert "data" in data
