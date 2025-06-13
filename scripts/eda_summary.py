import pandas as pd

def summarize_numerical_features(df, columns=None):
    """
    Print descriptive statistics for selected or all numerical columns.
    """
    if columns:
        num_df = df[columns]
    else:
        num_df = df.select_dtypes(include='number')

    print("📊 Descriptive Statistics for Numerical Features:")
    print(num_df.describe().T)
    print("\n🔍 Variability (Standard Deviation):")
    print(num_df.std().sort_values(ascending=False))

def review_data_structure(df):
    """
    Review structure of dataframe: dtypes, nulls, and unique values.
    """
    print("📋 Data Types and Null Counts:")
    print(df.dtypes)
    print("\n❗ Null Value Count:")
    print(df.isnull().sum()[df.isnull().sum() > 0])

    print("\n🔢 Categorical Columns & Unique Values:")
    cat_cols = df.select_dtypes(include='object').columns
    for col in cat_cols:
        unique_vals = df[col].nunique()
        if unique_vals < 20:  # Limit to manageable size
            print(f"{col}: {df[col].unique()}")
        else:
            print(f"{col}: {unique_vals} unique values")
