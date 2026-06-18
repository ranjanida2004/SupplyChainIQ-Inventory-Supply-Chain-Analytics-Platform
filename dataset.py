import pandas as pd
import numpy as np
from faker import Faker
from random import randint, choice

fake = Faker()

np.random.seed(42)

# ------------------------
# PRODUCTS
# ------------------------
categories = {
    "Electronics": ["Laptop", "Mouse", "Keyboard", "Monitor", "Tablet"],
    "Accessories": ["Headset", "Webcam", "USB Hub", "Charger", "Power Bank"],
    "Appliances": ["Mixer", "Fan", "Iron", "Kettle", "Vacuum Cleaner"]
}

products = []
product_id = 1001

for category, items in categories.items():
    for item in items:
        products.append([
            f"P{product_id}",
            item,
            category
        ])
        product_id += 1

products_df = pd.DataFrame(
    products,
    columns=["ProductID", "ProductName", "Category"]
)

# ------------------------
# WAREHOUSES
# ------------------------
warehouses = pd.DataFrame({
    "WarehouseID": [f"W{i}" for i in range(1, 6)],
    "Location": [
        "Chennai",
        "Bangalore",
        "Mumbai",
        "Hyderabad",
        "Delhi"
    ]
})

# ------------------------
# SUPPLIERS
# ------------------------
suppliers = []

for i in range(1, 11):
    suppliers.append([
        f"S{i:03}",
        fake.company()
    ])

suppliers_df = pd.DataFrame(
    suppliers,
    columns=["SupplierID", "SupplierName"]
)

# ------------------------
# INVENTORY
# ------------------------
inventory = []

for product in products_df["ProductID"]:
    for warehouse in warehouses["WarehouseID"]:
        inventory.append([
            product,
            warehouse,
            randint(20, 500)
        ])

inventory_df = pd.DataFrame(
    inventory,
    columns=["ProductID", "WarehouseID", "Stock"]
)

# ------------------------
# ORDERS (30,000 rows)
# ------------------------
orders = []

dates = pd.date_range(
    start="2024-01-01",
    end="2025-12-31",
    freq="D"
)

for i in range(1, 30001):

    product = choice(products_df["ProductID"].tolist())

    quantity = np.random.poisson(4)

    if quantity == 0:
        quantity = 1

    orders.append([
        f"O{i:06}",
        product,
        quantity,
        choice(dates)
    ])

orders_df = pd.DataFrame(
    orders,
    columns=[
        "OrderID",
        "ProductID",
        "Quantity",
        "OrderDate"
    ]
)

# ------------------------
# DELIVERIES
# ------------------------
deliveries = []

for i in range(1, 5001):

    supplier = choice(
        suppliers_df["SupplierID"].tolist()
    )

    expected = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    delay = np.random.choice(
        [0, 1, 2, 3, 5, 7],
        p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]
    )

    actual = expected + pd.Timedelta(days=int(delay))

    deliveries.append([
        f"D{i:05}",
        supplier,
        expected,
        actual
    ])

deliveries_df = pd.DataFrame(
    deliveries,
    columns=[
        "DeliveryID",
        "SupplierID",
        "ExpectedDate",
        "DeliveryDate"
    ]
)

# ------------------------
# REALISTIC ISSUES
# ------------------------

# Missing stock values
inventory_df.loc[
    inventory_df.sample(10).index,
    "Stock"
] = np.nan

# Duplicate orders
orders_df = pd.concat([
    orders_df,
    orders_df.sample(50)
])

# ------------------------
# EXPORT CSV FILES
# ------------------------

products_df.to_csv(
    "products.csv",
    index=False
)

warehouses.to_csv(
    "warehouses.csv",
    index=False
)

suppliers_df.to_csv(
    "suppliers.csv",
    index=False
)

inventory_df.to_csv(
    "inventory.csv",
    index=False
)

orders_df.to_csv(
    "orders.csv",
    index=False
)

deliveries_df.to_csv(
    "deliveries.csv",
    index=False
)

print("Dataset generated successfully!")