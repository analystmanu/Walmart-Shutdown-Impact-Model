import pandas as pd
 
# 1️⃣ Load Data
 
def load_data(path):
    """
    Load the cleaned fact_sales dataset.
    """
    print("Loading cleaned data from:", path)
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    print("Data loaded. Rows:", len(df))
    return df

 
# 2️⃣ Compute Total Revenue
 
def compute_total_revenue(df):
    """
    Calculate total revenue across all stores and weeks.
    """
    total_revenue = df["weekly_sales"].sum()
    print("\nTotal Revenue: ${:,.2f}".format(total_revenue))
    return total_revenue

 
# 3️⃣ Holiday Analysis
 
def holiday_analysis(df, total_revenue):
    """
    Compare revenue during holidays vs non-holidays and calculate percentages.
    Saves the result as CSV.
    """
    holiday_sales = df.groupby("is_holiday")["weekly_sales"].sum()
    holiday_pct = (holiday_sales / total_revenue) * 100

    result = pd.DataFrame({
        "revenue": holiday_sales,
        "percentage": holiday_pct
    })

    print("\nHoliday vs Non-Holiday Revenue:")
    print(result)

    result.to_csv("../data/holiday_revenue_percentage.csv")
    print("Saved holiday analysis to CSV.")

 
# 4️⃣ Store Revenue Rankings
 
def store_rankings(df):
    """
    Rank stores by total revenue.
    Saves rankings as CSV.
    """
    sales_per_store = (
        df.groupby("store_id")["weekly_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    sales_per_store.to_csv("../data/sales_per_store.csv")
    print("\nTop Stores by Revenue:")
    print(sales_per_store.head(10))
    return sales_per_store

 
# 5️⃣ Department Revenue Rankings
 
def department_rankings(df):
    """
    Rank departments by total revenue.
    Saves rankings as CSV.
    """
    sales_per_dept = (
        df.groupby("dept_id")["weekly_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    sales_per_dept.to_csv("../data/sales_per_dept.csv")
    print("\nTop Departments by Revenue:")
    print(sales_per_dept.head(10))
    return sales_per_dept

 
# 6️⃣ Shutdown Simulation
 
def shutdown_simulation(df, total_revenue, top_stores):
    """
    Simulate revenue loss if top 5 stores were shut down.
    Saves results to CSV.
    """
    shutdown_stores = top_stores.head(5).index.tolist()

    shutdown_loss = df[df["store_id"].isin(shutdown_stores)]["weekly_sales"].sum()
    shutdown_pct = (shutdown_loss / total_revenue) * 100

    summary = pd.DataFrame({
        "shutdown_loss": [shutdown_loss],
        "loss_pct": [shutdown_pct]
    })

    summary.to_csv("../data/shutdown_total_revenue_loss_summary.csv")
    print("\nShutdown Simulation (Top 5 Stores):")
    print(summary)

 
# 7️⃣ Individual Store Shutdown
 
def individual_store_shutdown(df, store_id, total_revenue):
    """
    Calculate revenue loss for a single store.
    Saves results to CSV.
    """
    store_loss = df[df["store_id"] == store_id]["weekly_sales"].sum()
    store_pct = (store_loss / total_revenue) * 100

    result = pd.DataFrame({
        "store_id": [store_id],
        "shutdown_loss": [store_loss],
        "loss_pct": [store_pct]
    })

    result.to_csv(f"../data/shutdown_revenue_loss_store_{store_id}.csv")
    print(f"\nShutdown Simulation for Store {store_id}:")
    print(result)

 
# Main pipeline
 
if __name__ == "__main__":
    path = "../data/fact_sales_clean.csv"

    df = load_data(path)
    total_revenue = compute_total_revenue(df)

    # Holiday analysis
    holiday_analysis(df, total_revenue)

    # Store & department rankings
    top_stores = store_rankings(df)
    top_departments = department_rankings(df)

    # Shutdown simulations
    shutdown_simulation(df, total_revenue, top_stores)
    individual_store_shutdown(df, store_id=1, total_revenue=total_revenue)