# Walmart Shutdown Impact Model

End-to-end Data Engineering & Data Analysis project analyzing revenue distribution, shutdown risk, and seasonal demand patterns using Walmart sales data.

## Overview
This project analyzes the **impact of temporary Walmart store shutdowns** on overall revenue. Using historical sales data, simulated shutdowns, and time-series analysis, the project quantifies potential revenue loss and identifies key trends across departments and stores.

The project was developed in **Python** using **GCP Cloud Shell**, leveraging pandas for data processing, matplotlib & seaborn for visualization, and Jupyter notebooks for interactive analysis.

## Problem Statement
Retailers often face temporary closures due to maintenance, holidays, or unexpected events. Understanding the **revenue impact of such shutdowns** is critical for planning, risk assessment, and resource allocation.  

This project answers:

- How much revenue is lost per store during shutdowns?
- Which departments or stores contribute most to total sales?
- How do holidays affect sales patterns?
- How can Walmart plan shutdowns to minimize losses?

---

## Methodology
1. **Data Extraction & Cleaning (ETL)**  
   - Collected weekly sales data for multiple stores and departments  
   - Cleaned missing values and standardized formats  

2. **Data Analysis**  
   - Compared holiday vs non-holiday sales  
   - Calculated store and department revenue rankings  
   - Visualized sales trends with time-series plots and heatmaps  

3. **Simulation**  
   - Simulated shutdown scenarios for individual stores and top 5 stores  
   - Computed total revenue loss under different shutdown durations  

4. **Findings & Insights**  
   - Identified high-revenue stores and departments  
   - Quantified percentage revenue loss due to shutdowns  
   - Recommended strategies to reduce impact  

---

 
---

## Tech Stack
- **Python** (pandas, numpy, matplotlib, seaborn, scikit-learn)  
- **GCP Cloud Shell** (development environment)  
- **Git & GitHub** (version control and portfolio)  

---

## Key Plots & Visualizations
- `sales_heatmap_store_dept.png` — department-level sales heatmap  
- `holiday_vs_nonholiday_sales.png` — comparison of holiday vs non-holiday sales  
- `weekly_sales_trend.png` — time-series of weekly sales per store  
- `store_1_shutdown_simulation.png` — revenue loss simulation for store 1  
- `revenue_loss_top_5_stores.png` — simulated loss for top 5 stores  

*(All plots available in `/plots` folder)*

---

 
