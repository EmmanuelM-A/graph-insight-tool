"""import pandas as pd
import re


def analyze(df):
    column_info = {}

    for col in df.columns:
        col_data = df[col]
        col_lower = col.lower()
        unique_vals = col_data.nunique()
        total_vals = len(col_data)
        unique_ratio = unique_vals / total_vals

        # Heuristic flags
        is_id_like = (
                unique_ratio > 0.9 and
                (re.search(r'\bid\b', col_lower) or col_lower.endswith('_id') or col_lower == 'id')
        )

        is_email = col_lower in ['email', 'email_address']
        is_ip = 'ip' in col_lower and 'address' in col_lower
        is_name = col_lower in ['first_name', 'last_name', 'firstname', 'lastname', 'first', 'last', 'family_name',
                                'surname']
        is_text_heavy = col_data.map(lambda x: isinstance(x, str) and len(x) > 30).mean() > 0.5

        if is_id_like:
            column_info[col] = 'id'
        elif is_email or is_ip or is_name:
            column_info[col] = 'pii'
        elif pd.api.types.is_numeric_dtype(col_data):
            column_info[col] = 'numerical'
        elif pd.api.types.is_datetime64_any_dtype(col_data):
            column_info[col] = 'datetime'
        elif col_data.dtype == 'object':
            try:
                parsed = pd.to_datetime(col_data, errors='raise', utc=True)
                df[col] = parsed
                column_info[col] = 'datetime'
            except ValueError:
                # TODO LOOK INTO THIS - MOST LABELS SHOULD BE CATEGORICAL
                if unique_vals <= 50 and col_data.map(lambda x: isinstance(x, str) and len(x) < 25).mean() > 0.8:
                    column_info[col] = 'categorical'
                elif is_text_heavy:
                    column_info[col] = 'text'
                else:
                    column_info[col] = 'other'
        else:
            column_info[col] = 'other'

    return column_info
"""
