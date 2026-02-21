import pandas as pd

 
# 1️⃣ Extract Part
 
def extract(path):
    """
    Load raw dataset from CSV.
    """
    print("Extracting raw data from:", path)
    df = pd.read_csv(path)
    print("Data loaded. Rows:", len(df))
    return df

 
# 2️⃣ Transform Part
 
def transform(df):
    """
    Clean and transform the dataset.
    """
    print("Transforming data...")

    # Convert 'date' to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Drop rows with missing weekly_sales
    df = df.dropna(subset=["weekly_sales"])

    # Optional: reset index
    df = df.reset_index(drop=True)

    print("Transformation complete. Rows after cleaning:", len(df))
    return df
 
# 3️⃣ Load Part
 
def load(df, output_path):
    """
    Save the cleaned/transformed data as CSV.
    """
    print("Loading (saving) data to:", output_path)
    df.to_csv(output_path, index=False)
    print("Data saved successfully!")

 
# Main pipeline
 
if __name__ == "__main__":
    raw_path = "../data/fact_sales_saved.csv"   # adjust path if needed
    clean_path = "../data/fact_sales_clean.csv"

    # ETL steps
    df_raw = extract(raw_path)
    df_clean = transform(df_raw)
    load(df_clean, clean_path)