import os
import pytest
import logging
from modules.data_loader import data_loader

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s -> %(message)s",
    handlers=[
        logging.FileHandler("test_logs/test_data_loader.log", mode='w'),  # Log to file
        #logging.StreamHandler()  # Log to console
    ]
)

# Path to the directory containing test files
TEST_FILES_DIR = 'test_data_files'

# TODO LOOK INTO LOGGING MECHANISM AND FIGURE OUT WHY LOGGING DOES NOT WORK

@pytest.mark.parametrize("filename", os.listdir(TEST_FILES_DIR))
def test_data_loader_file(filename):
    filepath = os.path.join(TEST_FILES_DIR, filename)

    data, msg = data_loader(filepath)

    if data is not None:
        logging.info(f"File: {filename} - Successfully loaded!")
        assert data is not None
        print(f"File: {filename} - Successfully loaded!")
    else:
        logging.error(f"File: {filename} - Error: {msg}")
        assert data is None
        print(f"File: {filename} - Error: {msg}")
