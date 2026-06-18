import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
products = pd.read_csv(r"C:\Users\ranja\OneDrive\Desktop\ranjani\realtime projects\SupplyChainIQ – Inventory & Supply Chain Analytics Platform\supplychain dataset\products.csv")
inventory = pd.read_csv(r"C:\Users\ranja\OneDrive\Desktop\ranjani\realtime projects\SupplyChainIQ – Inventory & Supply Chain Analytics Platform\supplychain dataset\inventory.csv")
orders = pd.read_csv(r"C:\Users\ranja\OneDrive\Desktop\ranjani\realtime projects\SupplyChainIQ – Inventory & Supply Chain Analytics Platform\supplychain dataset\orders.csv")
suppliers = pd.read_csv(r"C:\Users\ranja\OneDrive\Desktop\ranjani\realtime projects\SupplyChainIQ – Inventory & Supply Chain Analytics Platform\supplychain dataset\suppliers.csv")
deliveries = pd.read_csv(r"C:\Users\ranja\OneDrive\Desktop\ranjani\realtime projects\SupplyChainIQ – Inventory & Supply Chain Analytics Platform\supplychain dataset\deliveries.csv")
warehouses = pd.read_csv(r"C:\Users\ranja\OneDrive\Desktop\ranjani\realtime projects\SupplyChainIQ – Inventory & Supply Chain Analytics Platform\supplychain dataset\warehouses.csv")

#explore data
print(products.head())
print(inventory.head())
print(orders.head())
print(products.info())
print(inventory.info())
print(products.shape)
print(inventory.shape)

#top selling products
print("---Top Selling Products---")
top_products = (
    orders.groupby('ProductID')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products.plot(kind='bar')
plt.title("Top Selling Products")
plt.show()

#warehouse inventory
print("---Warehouse Inventory---")
warehouse_stock = (
    inventory.groupby('WarehouseID')['Stock']
    .sum()
)

warehouse_stock.plot(kind='bar')
plt.title("Inventory by Warehouse")
plt.show()

#stockout products
print("---Out-of-Stock Products---")
# Merge inventory and products data
stockout_details = inventory.merge(
    products,
    on='ProductID',
    how='inner'
)
# Filter out-of-stock products
stockout_details = stockout_details[
    stockout_details['Stock'] == 0
]
# Display results
print("Out-of-Stock Products:")
print(
    stockout_details[
        ['ProductID', 'ProductName', 'WarehouseID', 'Stock']
    ]
)
# Count total stockouts
print(
    "\nTotal Out-of-Stock Records:",
    stockout_details.shape[0]
)

#Supplier Delays
print("---Supplier Delays---")
# Convert date columns to datetime
deliveries['ExpectedDate'] = pd.to_datetime(deliveries['ExpectedDate'])
deliveries['DeliveryDate'] = pd.to_datetime(deliveries['DeliveryDate'])
# Calculate delay in days
deliveries['DelayDays'] = (
    deliveries['DeliveryDate'] - deliveries['ExpectedDate']
).dt.days
# Average delay by supplier
avg_delay = (
    deliveries.groupby('SupplierID')['DelayDays']
    .mean()
    .reset_index()
    .sort_values(by='DelayDays', ascending=False)
)
print(avg_delay)

#Category Performance
print("---Category Performance---")
sales_category = orders.merge(
    products,
    on='ProductID'
)
sales_category.groupby('Category')['Quantity'].sum()
sales_category.groupby('Category')['Quantity'].sum().plot(kind='bar')
plt.title("Sales by Category")
plt.show()

