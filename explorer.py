import pandas as pd

# Load CSV
def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print(f"\nFile loaded: {filepath}")
        return df
    except FileNotFoundError:
        print("File not found. Check your path.")
        return None

# Inspect dataset
def inspect_data(df):
    print("\nShape:", df.shape)

    print("\nColumns & Data Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

# Check missing values
def check_missing(df):
    print("\nMissing Values:")

    missing = df.isnull().sum()
    pct = (missing / len(df) * 100).round(2)

    summary = pd.DataFrame({
        'Count': missing,
        'Percent (%)': pct
    })

    print(summary[summary['Count'] > 0])

# Summary statistics
def summary_stats(df):
    print("\nSummary Statistics (Numeric Columns):")

    print(
        df.describe().T[
            ['mean', '50%', 'std', 'min', 'max']
        ].rename(columns={'50%': 'median'})
    )

# Outlier detection using IQR
def detect_outliers(df):
    print("\nOutlier Detection (IQR Method):")

    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)

        IQR = Q3 - Q1

        outliers = df[
            (df[col] < Q1 - 1.5 * IQR) |
            (df[col] > Q3 + 1.5 * IQR)
        ]

        print(f"{col}: {len(outliers)} outlier(s)")

# Main block
if __name__ == "__main__":

    filepath = "titanic.csv"

    df = load_data(filepath)

    if df is not None:
        inspect_data(df)
        check_missing(df)
        summary_stats(df)
        detect_outliers(df)