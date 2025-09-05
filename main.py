import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.clean_data import clean_dataset
from src.load_data import load_dataset
from src.visualize_data import plot_content_type, plot_release_year_distribution, plot_top_countries

DATA_PATH = os.path.join("data", "netflix_titles.csv")
df = pd.read_csv(DATA_PATH)
# print(df.head())
print("Initial dataset shape:", df.shape)
print(df.info())
print(df.describe())

# Step 2: Clean dataset
df = clean_dataset(df)
print("Cleaned dataset shape:", df.shape)

# Step 3: Visualizations
plot_content_type(df)
plot_top_countries(df)
plot_release_year_distribution(df)
print("Plots saved to /images folder.")
