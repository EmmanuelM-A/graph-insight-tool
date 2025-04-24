import os
import logging
from modules.data_loader import data_loader

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s -> %(message)s",
    handlers=[
        logging.FileHandler("test_data_loader.log"),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

# Path to the directory containing test files
TEST_FILES_DIR = "./test_data_files"


def test_data_loader_file(filename):
    filepath = os.path.join(TEST_FILES_DIR, filename)

    data, msg = data_loader(filepath)

    if data is not None:
        logging.info(f"{filename} - Successfully loaded!")
        return True
    else:
        logging.error(f"{filename} - Error: {msg}")
        return False


if __name__ == "__main__":
    total = 0
    passed = 0

    for file in sorted(os.listdir(TEST_FILES_DIR)):
        filename = os.fsdecode(file)

        if os.path.isfile(os.path.join(TEST_FILES_DIR, filename)):
            total += 1
            if test_data_loader_file(filename):
                passed += 1

    logging.info(f"Test Summary: {passed}/{total} files loaded successfully.")
