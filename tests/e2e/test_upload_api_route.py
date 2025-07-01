"""The test suite for the upload request endpoint"""

import requests

UPLOAD_URL = "http://127.0.0.1:5000/api/upload"


class TestUploadAPI:
    """Upload test class"""
    def test_upload_endpoint(self, get_test_file_path):
        """Function Description HERE!"""

        with open(get_test_file_path, "rb") as f:
            files = {'file': f}
            response = requests.post(UPLOAD_URL, files=files)

            print(response)

        assert response.status_code == 200

        data = response.json()
        print(data)
        assert "message" in data
        assert "data" in data
        assert "preview" in data["data"]
