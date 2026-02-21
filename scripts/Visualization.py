import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

 
# 1 Load Data
 
def load_data(path):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df

 
# 2 Holiday vs Non-Holiday Plot
 
def plot_holiday_sales(df, output_folder="../plots"):
    holiday_sales = df.groupby("is_holiday")["weekly_sales"].sum()

    plt.figure(figsize=(6,4))
    holiday_sales.plot(kind="bar", color=["skyblue","salmon"])
    plt.title("Holiday vs Non-Holiday Sales")
    plt.ylabel("Revenue")
    plt.xticks([0,1], ["Non-Holiday","Holiday"], rotation=0)
    plt.tight_layout()

    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(os.path.join(output_folder, "holiday_vs_nonholiday_sales.png"))
    plt.close()
    print("Saved plot: holiday_vs_nonholiday_sales.png")

 
# 3 Weekly Revenue Trend
 
def plot_weekly_trend(df, output_folder="../plots"):
    weekly_revenue = df.groupby("date")["weekly_sales"].sum()

    plt.figure(figsize=(10,5))
    weekly_revenue.plot(color="green")
    plt.title("Weekly Revenue Trend")
    plt.ylabel("Revenue")
    plt.xlabel("Week")
    plt.tight_layout()

    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(os.path.join(output_folder, "weekly_sales_trend.png"))
    plt.close()
    print("Saved plot: weekly_sales_trend.png")

 
# 4 Top Stores Revenue Trend
 
def plot_top_stores(df, top_n=5, output_folder="../plots"):
    store_sales = df.groupby("store_id")["weekly_sales"].sum().sort_values(ascending=False)
    top_stores = store_sales.head(top_n).index.tolist()

    plt.figure(figsize=(12,6))
    for store in top_stores:
        store_df = df[df["store_id"] == store].set_index("date")["weekly_sales"]
        store_df.plot(label=f"Store {store}")

    plt.title(f"Top {top_n} Stores Weekly Sales Trend")
    plt.ylabel("Revenue")
    plt.xlabel("Week")
    plt.legend()
    plt.tight_layout()

    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(os.path.join(output_folder, f"top_{top_n}_stores_trend.png"))
    plt.close()
    print(f"Saved plot: top_{top_n}_stores_trend.png")

 
# 5 Store-Department Heatmap
 
def plot_store_dept_heatmap(df, output_folder="../plots"):
    pivot_table = df.pivot_table(
        index="store_id",
        columns="dept_id",
        values="weekly_sales",
        aggfunc="sum",
        fill_value=0
    )

    plt.figure(figsize=(14,10))
    sns.heatmap(pivot_table, cmap="YlGnBu")
    plt.title("Sales Heatmap: Store vs Department")
    plt.xlabel("Department")
    plt.ylabel("Store")
    plt.tight_layout()

    os.makedirs(output_folder, exist_ok=True)
    plt.savefig(os.path.join(output_folder, "store_dept_sales_heatmap.png"))
    plt.close()
    print("Saved plot: store_dept_sales_heatmap.png")

# Main Execution
 
if __name__ == "__main__":
    path = "../data/fact_sales_clean.csv"
    df = load_data(path)

    plot_holiday_sales(df)
    plot_weekly_trend(df)
    plot_top_stores(df, top_n=5)
    plot_store_dept_heatmap(df)

    print("\nAll plots generated successfully.")