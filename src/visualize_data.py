# src/visualize_data.py
import matplotlib

matplotlib.use('TkAgg')  # or 'Qt5Agg' if Tk is unavailable
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")


def save_plot(fig, filename):
    os.makedirs("images", exist_ok=True)
    fig.savefig(os.path.join("images", filename), bbox_inches='tight')
    plt.close(fig)


def plot_content_type(df):
    print("Plots debug to /images folder.")
    print(df['type'].value_counts())
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x='type', palette='viridis', ax=ax)
    ax.set_title('Count of Movies vs TV Shows')
    save_plot(fig, "content_type_count.png")


def plot_top_countries(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    top_countries = df['country'].value_counts().head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index, ax=ax, palette='mako')
    ax.set_title('Top 10 Countries by Content Count')
    save_plot(fig, "top_countries.png")


def plot_release_year_distribution(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df['release_year'], bins=20, kde=False, ax=ax, color='teal')
    ax.set_title('Content Release Year Distribution')
    save_plot(fig, "release_year_distribution.png")
