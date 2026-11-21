E-commerce Sales Dashboard

A small project that analyses e-commerce orders using Python, NumPy and Pandas. There are no charts. The results are shown as tables and saved as files.

What it tells you
Total orders, revenue, average order value and number of customers
Return rate and cancel rate
Revenue for every month, and how much it grew or dropped
Which categories and regions earn the most
Top 5 products and top 5 customers
Folder structure
ecommerce-dashboard/
├── data/
│   └── ecommerce_data.csv      # the dataset (2,000 orders)
├── output/                     # results created by the code
│   ├── dashboard_output.txt
│   ├── kpi_summary.csv
│   ├── monthly_revenue.csv
│   ├── category_revenue.csv
│   ├── region_revenue.csv
│   ├── top_products.csv
│   └── top_customers.csv
├── dashboard.py                # the code
├── requirements.txt
└── README.md
About the dataset

Each row is one order. Columns:

Column	Meaning
order_id	unique order number
order_date	date of the order (2025)
customer_id	who bought
region	North, South, East or West
product_name	name of the product
category	Electronics, Fashion, Home, Beauty or Books
price	price of one item
quantity	items bought
discount	discount given (0 to 0.20)
status	Delivered, Returned or Cancelled

Revenue is calculated as price x quantity x (1 - discount). Only Delivered orders are counted as sales.

How to run

On your computer

bash
pip install -r requirements.txt
python dashboard.py

On Google Colab

Open a new notebook and upload dashboard.py and ecommerce_data.csv (folder icon on the left).
Run this in a cell:
python
%run dashboard.py
Main findings
Total revenue from delivered orders is about 1.04 million
December 2025 was the best month and November 2025 the weakest
Home and Beauty bring in more than half of the revenue, Fashion earns the least
All four regions earn almost the same amount
Tools used

Python, NumPy, Pandas
