import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def check_missing_values(df):
    """
    Display count and percentage of missing values per column.
    """
    print("🔍 Missing Values Summary:")
    nulls = df.isnull().sum()
    null_pct = (nulls / len(df)) * 100
    missing_data = pd.DataFrame({'MissingValues': nulls, 'Percent': null_pct})
    print(missing_data[missing_data['MissingValues'] > 0].sort_values(by='MissingValues', ascending=False))

def plot_numerical_distributions(df, columns):
    """
    Plot histograms for selected numerical columns.
    """
    print("📊 Histograms for Numerical Features:")
    for col in columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col].dropna(), bins=30, kde=True)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

def plot_categorical_distributions(df, columns):
    """
    Plot bar charts for selected categorical columns.
    """
    print("📊 Bar Charts for Categorical Features:")
    for col in columns:
        plt.figure(figsize=(8, 4))
        df[col].value_counts(dropna=False).plot(kind='bar')
        plt.title(f'Frequency of {col}')
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
