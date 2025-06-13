import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def univariate_analysis(df):
    print("📊 Univariate Analysis:")

    # Numerical columns
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col].dropna(), kde=True, bins=30)
        plt.title(f'Distribution of {col}')
        plt.tight_layout()
        plt.show()

    # Categorical columns
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        plt.figure(figsize=(8, 4))
        top_vals = df[col].value_counts().nlargest(10)
        sns.barplot(x=top_vals.index, y=top_vals.values)
        plt.title(f'Top 10 Frequent Categories in {col}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

def bivariate_analysis(df):
    print("\n🔁 Bivariate Analysis (Correlations & Scatter):")
    # Convert date if not already
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    df['Month'] = df['TransactionMonth'].dt.to_period('M').astype(str)

    monthly = df.groupby(['Month', 'PostalCode']).agg({
        'TotalPremium': 'sum',
        'TotalClaims': 'sum'
    }).reset_index()

    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=monthly, x='TotalPremium', y='TotalClaims', hue='PostalCode')
    plt.title('Monthly Total Premium vs Total Claims by PostalCode')
    plt.tight_layout()
    plt.show()

    corr_cols = ['TotalPremium', 'TotalClaims']
    corr = df[corr_cols].corr()
    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()

def trend_over_geography(df):
    print("\n🗺️ Geographic Trends:")
    geo_summary = df.groupby('Province').agg({
        'TotalPremium': 'mean',
        'CoverType': lambda x: x.mode().iloc[0] if not x.mode().empty else None,
        'make': lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    }).reset_index()

    plt.figure(figsize=(10, 5))
    sns.barplot(data=geo_summary, x='Province', y='TotalPremium')
    plt.title("Average Premium by Province")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='CoverType', hue='Province', order=df['CoverType'].value_counts().index)
    plt.title("Cover Type Distribution by Province")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    top_makes = df['make'].value_counts().nlargest(10).index
    filtered = df[df['make'].isin(top_makes)]
    plt.figure(figsize=(12, 6))
    sns.countplot(data=filtered, x='make', hue='Province')
    plt.title("Top 10 Vehicle Makes by Province")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def outlier_detection(df):
    print("\n🚨 Outlier Detection:")
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[col].dropna())
        plt.title(f'Outlier Detection: {col}')
        plt.tight_layout()
        plt.show()

# Main function
def run_full_eda(df):
    univariate_analysis(df)
    bivariate_analysis(df)
    trend_over_geography(df)
    outlier_detection(df)
