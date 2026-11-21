# E-commerce sales dashboard
# Uses only numpy and pandas (no charts). Results are printed and saved in the output folder.

import os
import numpy as np
import pandas as pd

pd.options.display.float_format = "{:,.2f}".format

# the csv can be inside the data folder or next to this file (useful in google colab)
file_path = "data/ecommerce_data.csv"
if not os.path.exists(file_path):
    file_path = "ecommerce_data.csv"

df = pd.read_csv(file_path)
df["order_date"] = pd.to_datetime(df["order_date"])

# remove repeated orders and rows with missing values
df = df.drop_duplicates(subset="order_id")
df = df.dropna()

# money earned from each order after the discount
df["revenue"] = df["price"] * df["quantity"] * (1 - df["discount"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)

# returned and cancelled orders are not real sales, so only delivered ones are counted
sales = df[df["status"] == "Delivered"]

os.makedirs("output", exist_ok=True)
report = []


def show(text=""):
    print(text)
    report.append(str(text))


# ---------- key numbers ----------
kpi = pd.Series({
    "Total orders": len(df),
    "Delivered orders": len(sales),
    "Total revenue": sales["revenue"].sum(),
    "Average order value": sales["revenue"].mean(),
    "Unique customers": sales["customer_id"].nunique(),
    "Units sold": sales["quantity"].sum(),
    "Return rate (%)": np.mean(df["status"] == "Returned") * 100,
    "Cancel rate (%)": np.mean(df["status"] == "Cancelled") * 100,
})

show("KEY NUMBERS")
for name, value in kpi.items():
    if float(value).is_integer():
        show(f"{name:<22}{value:>14,.0f}")
    else:
        show(f"{name:<22}{value:>14,.2f}")

# ---------- monthly revenue ----------
monthly = sales.groupby("month")["revenue"].sum().to_frame()
monthly["growth (%)"] = monthly["revenue"].pct_change() * 100

show("\nMONTHLY REVENUE")
show(monthly.to_string())

# ---------- category and region ----------
by_category = sales.groupby("category")["revenue"].sum().sort_values(ascending=False)
by_region = sales.groupby("region")["revenue"].sum().sort_values(ascending=False)

show("\nREVENUE BY CATEGORY")
show(by_category.to_string())

show("\nREVENUE BY REGION")
show(by_region.to_string())

# ---------- best products and customers ----------
top_products = sales.groupby("product_name")["revenue"].sum().nlargest(5)
top_customers = sales.groupby("customer_id")["revenue"].sum().nlargest(5)

show("\nTOP 5 PRODUCTS")
show(top_products.to_string())

show("\nTOP 5 CUSTOMERS")
show(top_customers.to_string())

# ---------- quick summary ----------
show("\nQUICK SUMMARY")
show(f"Best month      : {monthly['revenue'].idxmax()}")
show(f"Weakest month   : {monthly['revenue'].idxmin()}")
show(f"Top category    : {by_category.index[0]}")
show(f"Lowest category : {by_category.index[-1]}")
show(f"Top region      : {by_region.index[0]}")

# ---------- save everything ----------
kpi.to_csv("output/kpi_summary.csv", header=["value"])
monthly.to_csv("output/monthly_revenue.csv")
by_category.to_csv("output/category_revenue.csv")
by_region.to_csv("output/region_revenue.csv")
top_products.to_csv("output/top_products.csv")
top_customers.to_csv("output/top_customers.csv")

with open("output/dashboard_output.txt", "w") as f:
    f.write("\n".join(report))

print("\nFiles saved in the output folder.")
