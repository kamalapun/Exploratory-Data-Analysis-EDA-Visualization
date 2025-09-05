# File: src/load_data.py
### Imports
```
import os
import pandas as pd
```
- os: Provides functions for working with the operating system, like file paths. 
- pandas as pd: Pandas is used for working with data in tables (DataFrames).

### Function: load_dataset(file_name)

This function loads a dataset (CSV file) from the data folder.

- Build the file path :path = os.path.join("data", file_name)
Combines "data" folder name and file_name into one path using os.path.join.
This makes it cross-platform — works on Windows (\) and Mac/Linux (/).
Example:
```
If file_name = "movies.csv",
path becomes "data/movies.csv".
```
- Print full path (for debugging)
```
print("Loading from:", os.path.abspath(path))
```
os.path.abspath(path) gives the absolute path (full path from the root directory).
Helpful to check if the file path is correct when debugging.

- Load the CSV into a DataFrame
```
return pd.read_csv(path)
```
Uses pandas to read the CSV file at path.
Returns a DataFrame — a table-like structure for working with data.

# File: src/clean_data.py

It imports pandas (a library for working with tabular data) and defines a function clean_dataset that cleans a given dataset stored as a pandas DataFrame.
Function: 
```
clean_dataset(df: pd.DataFrame) -> pd.DataFrame
```
This function takes in a DataFrame df and returns a cleaned version of it.
- Fill missing categorical values
```
for col in ['director', 'cast', 'country', 'rating']:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown')
```
Loops over four columns: director, cast, country, and rating.
If the column exists in the dataset, all missing values (NaN) are replaced with 'Unknown'.
This ensures there are no blanks in these categorical fields.

- Convert date column
```
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
```
Checks if date_added exists in the dataset.
Converts it into a datetime object.
If conversion fails (e.g., invalid date string), it replaces the value with NaT (pandas' version of missing datetime).

- Fill missing durations
```
if 'duration' in df.columns:
    df['duration'] = df['duration'].fillna('Unknown')
```
For the duration column, missing values are also replaced with 'Unknown'.
- Return cleaned data
```
return df
```
Finally, the cleaned DataFrame is returned.
# File src/visualize_data
### Imports
```
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg' if Tk is unavailable
import matplotlib.pyplot as plt
import seaborn as sns
import os
```
- matplotlib: Library for creating plots.
- matplotlib.use('TkAgg') specifies the backend (how plots are rendered).
- 'TkAgg' works with Tkinter; 'Qt5Agg' is an alternative.
- matplotlib.pyplot as plt: Provides the plotting interface.
- seaborn as sns: High-level plotting library built on Matplotlib for prettier charts.
- os: For file operations, like creating folders.

sns.set(style="whitegrid"): Sets the default Seaborn style for plots with a white background and grid lines.

### Function: save_plot
```
def save_plot(fig, filename):
    os.makedirs("images", exist_ok=True)
    fig.savefig(os.path.join("images", filename), bbox_inches='tight')
    plt.close(fig)
```
Purpose: Save a plot as an image file.

- os.makedirs("images", exist_ok=True) creates an images folder if it doesn’t exist.
- fig.savefig(...) saves the figure in that folder.
- bbox_inches='tight' trims extra whitespace.
- plt.close(fig) closes the figure to free memory.

### Function: plot_content_type
```
def plot_content_type(df):
    print("Plots debug to /images folder.")
    print(df['type'].value_counts())
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='type', palette='viridis', ax=ax)
    ax.set_title('Count of Movies vs TV Shows')
    save_plot(fig, "content_type_count.png")
```
Prints debug info: counts of each type (Movie, TV Show).
Creates a count plot showing how many movies vs TV shows exist.
Uses viridis color palette.
Calls save_plot to save the figure as "images/content_type_count.png".

### Function: plot_top_countries
```
def plot_top_countries(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    top_countries = df['country'].value_counts().head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index, ax=ax, palette='mako')
    ax.set_title('Top 10 Countries by Content Count')
    save_plot(fig, "top_countries.png")
```

Finds the top 10 countries by content count.
Plots a horizontal bar chart using barplot.
Saves figure as "images/top_countries.png".

### Function: plot_release_year_distribution
```
def plot_release_year_distribution(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df['release_year'], bins=20, kde=False, ax=ax, color='teal')
    ax.set_title('Content Release Year Distribution')
    save_plot(fig, "release_year_distribution.png")
```

Plots a histogram of release years (grouped in 20 bins).

kde=False disables density curve; only shows counts.

Saves figure as "images/release_year_distribution.png".