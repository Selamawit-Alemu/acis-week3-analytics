import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set a consistent style for plots
sns.set_theme(style="whitegrid")

def load_data(filepath):
    """
    Loads data from the given filepath, handles pipe delimiters,
    and converts key columns to appropriate data types.
    """
    print(f"Attempting to load data from: {filepath}")
    df = pd.read_csv(filepath, delimiter="|")

    # Handle the DtypeWarning columns ('CapitalOutstanding' and 'CrossBorder')
    # Convert 'CapitalOutstanding' to numeric, coercing errors to NaN.
    df['CapitalOutstanding'] = pd.to_numeric(df['CapitalOutstanding'], errors='coerce')

    # Convert 'CrossBorder' to a nullable boolean type.
    # Replace common "False" representations and then convert to numeric before boolean for robustness.
    df['CrossBorder'] = df['CrossBorder'].replace({'False': False, 'false': False, '0': False, '': pd.NA})
    df['CrossBorder'] = pd.to_numeric(df['CrossBorder'], errors='coerce').astype('boolean')

    # Convert date columns to datetime objects for proper time-series analysis.
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    df['VehicleIntroDate'] = pd.to_datetime(df['VehicleIntroDate'])

    # Ensure 'TotalPremium' and 'TotalClaims' are numeric, handling potential non-numeric entries.
    df['TotalPremium'] = pd.to_numeric(df['TotalPremium'], errors='coerce')
    df['TotalClaims'] = pd.to_numeric(df['TotalClaims'], errors='coerce')

    print("Data loaded and preprocessed successfully!")
    return df

def describe_variables(df, cols):
    """
    Returns descriptive statistics for the specified numeric columns.
    """
    print(f"\n--- Descriptive Statistics for {', '.join(cols)} ---")
    stats = df[cols].agg(['count', 'min', 'max', 'mean', 'median', 'std', 'skew', 'kurt'])
    print(stats)
    print("\n" + "="*50 + "\n")
    return stats # Return stats for potential further use

def plot_distribution(df, col, save_dir='plots'):
    """
    Plots and saves histogram + KDE plot for a given column,
    and displays the plot.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"Created directory: {save_dir}")

    # --- TEMPORARY DEBUGGING PRINTS ---
    print(f"\n--- Debugging plot_distribution for '{col}' ---")
    print(f"Column '{col}' head:\n{df[col].head()}")
    print(f"Column '{col}' isnull().sum(): {df[col].isnull().sum()}")
    print(f"Column '{col}' describe():\n{df[col].describe()}")
    if df[col].dropna().empty:
        print(f"WARNING: After dropping NaNs, '{col}' is empty. Plot will be blank.")
    print(f"--------------------------------------------------")
    # --- END TEMPORARY DEBUGGING PRINTS ---

    plt.figure(figsize=(10, 4))
    sns.histplot(df[col].dropna(), bins=50, kde=True, color='skyblue')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency / Density')
    plt.tight_layout()

    plot_save_path = os.path.join(save_dir, f'{col}_distribution.png')
    plt.savefig(plot_save_path)
    print(f"Plot saved to: {plot_save_path}")

    plt.show()
    plt.close()

# ... (main function remains the same) ...
def main():
    """
    Main function to run the EDA process.
    """
    # Define the relative path to your data file
    # This assumes your notebook/script is one level up from 'data' and 'scripts'
    data_path = '../data/MachineLearningRating_v3.txt'
    
    df = load_data(data_path)

    print("\n📊 Starting Exploratory Data Analysis:\n")

    # Describe financial variables
    describe_variables(df, ['TotalPremium', 'TotalClaims'])

    # Generate and display distribution plots
    print("\n📈 Generating distribution plots for TotalPremium and TotalClaims...")
    plot_distribution(df, 'TotalPremium')
    plot_distribution(df, 'TotalClaims')
    print("✅ All plots generated and saved in the 'plots/' folder, and should be displayed above.")

if __name__ == "__main__":
    main()