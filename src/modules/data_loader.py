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
        is_csv_file = uploaded_data_filepath.endswith('.csv')
        is_xls_or_xlsx_file = uploaded_data_filepath.endswith(('.xls', '.xlsx'))

        if is_csv_file:
            data = pd.read_csv(uploaded_data_filepath)
            msg = "CSV file loaded successfully."
        elif is_xls_or_xlsx_file:
            data = pd.read_excel(uploaded_data_filepath, engine='openpyxl')
            msg = "Excel file loaded successfully."
        else:
            msg = "File format not supported! Please upload a CSV or Excel file."
    except Exception as e:
        msg = f"Error loading file: {str(e)}"

    if data is not None:
        # Strips whitespace from column names and convert to lowercase
        data.columns = data.columns.str.strip()

    return data, msg
