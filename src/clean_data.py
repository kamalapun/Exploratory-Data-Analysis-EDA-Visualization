# src/clean_data.py
import pandas as pd


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: handle missing values & convert date columns."""
    # Fill missing categorical values with 'Unknown'
    for col in ['director', 'cast', 'country', 'rating']:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')

    # Fill missing dates with a placeholder
    if 'date_added' in df.columns:
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Fill missing durations with 'Unknown'
    if 'duration' in df.columns:
        df['duration'] = df['duration'].fillna('Unknown')

    return df
