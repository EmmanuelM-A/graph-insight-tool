import pandas as pd


def data_loader(uploaded_data_filepath):
    """
    Loads tabular data from a CSV or Excel file.

    Parameters:
        uploaded_data_filepath (str): Path to the uploaded file.

    Returns:
        tuple:
            - pd.DataFrame or None: The loaded DataFrame or None if failed.
            - str: Message indicating success or failure.
    """

    data = None

    try:
        # Check if the data file is one of the allowed formats, and such read into a pandas DataFrame accordingly
        if uploaded_data_filepath.endswith('.csv'):
            data = pd.read_csv(uploaded_data_filepath)
            msg = "CSV file loaded successfully."
        elif uploaded_data_filepath.endswith(('.xls', '.xlsx')):
            data = pd.read_excel(uploaded_data_filepath)
            msg = "Excel file loaded successfully."
        else:
            msg = "File format not supported! Please upload a CSV or Excel file."
    except Exception as e:
        msg = f"Error loading file: {str(e)}"

    if data is not None:
        # Strip whitespace from column names and convert to lowercase
        data.columns = data.columns.str.strip()

    return data, msg
