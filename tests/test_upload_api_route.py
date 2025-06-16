import requests

# URL of your Flask server route
url = "http://127.0.0.1:5000/api/upload"  # Change if your port or route is different

# File to upload (ensure this file exists)
files = {
    'file': open("tests/test_data_files/test-data-0.csv", 'rb')  # Path to a sample test file
}

try:
    # Send POST request to the upload API
    response = requests.post(url, files=files)

    # Print status and response
    print("Status Code: ", response.status_code)
    print("Response JSON: ", response.json())

except Exception as e:
    print("Error making request: ", e)