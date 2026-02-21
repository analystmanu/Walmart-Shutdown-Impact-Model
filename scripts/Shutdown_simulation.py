import pandas as pd
import os

 
# 1️⃣ Load Data
 
def load_data(path):
    """
    Load cleaned fact_sales dataset
    """
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df

 
# 2️⃣ Simulate Single Store Shutdown
 
def simulate_store_shutdown(df, store_id, output_folder="../data"):
    """
    Simulate revenue loss if a single store shuts down.
    Saves result to CSV.
    """
    store_sales = df[df["store_id"] == store_id]
    loss = store_sales["weekly_sales"].sum()
    result = pd.DataFrame({
        "store_id": [store_id],
        "shutdown_loss": [loss]
    })

    os.makedirs(output_folder, exist_ok=True)
    result.to_csv(os.path.join(output_folder, f"shutdown_revenue_loss_store_{store_id}.csv"), index=False)
    
    print(f"Store {store_id} Shutdown Loss: ${loss:,.2f}")
    return result

 
# 3️⃣ Simulate Top N Stores Shutdown
 
def simulate_top_stores_shutdown(df, top_n=5, output_folder="../data"):
    """
    Simulate revenue loss if top N stores shut down.
    Saves result to CSV.
    """
    store_sales = df.groupby("store_id")["weekly_sales"].sum().sort_values(ascending=False)
    top_stores = store_sales.head(top_n).index.tolist()

    loss = df[df["store_id"].isin(top_stores)]["weekly_sales"].sum()
    result = pd.DataFrame({
        "top_stores": [top_stores],
        "shutdown_loss": [loss]
    })

    os.makedirs(output_folder, exist_ok=True)
    result.to_csv(os.path.join(output_folder, f"shutdown_revenue_loss_top_{top_n}_stores.csv"), index=False)

    print(f"Top {top_n} Stores Shutdown Loss: ${loss:,.2f}")
    return result

 
# Main Execution
 
if __name__ == "__main__":
    path = "../data/fact_sales_clean.csv"
    df = load_data(path)

    # Single store example
    simulate_store_shutdown(df, store_id=1)

    # Top 5 stores shutdown
    simulate_top_stores_shutdown(df, top_n=5)

    print("\nShutdown simulations completed and saved as CSV.")