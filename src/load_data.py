import os

import pandas as pd


# Load dataset
def load_dataset(file_name):
    """Load dataset from data folder"""
    path = os.path.join("data", file_name)
    print("Loading from:", os.path.abspath(path))  # <-- DEBUG
    return pd.read_csv(path)
