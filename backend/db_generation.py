import sqlite3
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("en_IN")

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# ---------------- DROP TABLES ----------------
tables = ["Product_Reviews", "Inventory_Logs", "Orders", "Customers"]
for t in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {t}")

# ---------------- CREATE TABLES ----------------
cursor.execute("""
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    city TEXT,
    state TEXT,
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date TEXT,
    order_time TEXT,
    status TEXT,
    payment_method TEXT,
    order_channel TEXT,
    total_quantity INTEGER,
    total_amount REAL,
    discount_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)
""")

cursor.execute("""
CREATE TABLE Inventory_Logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    product_category TEXT,
    change_type TEXT,
    quantity_changed INTEGER,
    current_stock INTEGER,
    log_date TEXT,
    related_order_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE Product_Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_name TEXT,
    rating INTEGER,
    review_text TEXT,
    verified_purchase INTEGER,
    sentiment_score REAL,
    review_date TEXT
)
""")

# ---------------- HELPER DATA ----------------
products = {
    "Basmati Rice": "Grocery",
    "Milk Packet": "Grocery",
    "Sugar 1kg": "Grocery",
    "Men T-Shirt": "Clothing",
    "Women Jeans": "Clothing",
    "Kids Jacket": "Clothing",
    "LED Bulb": "Electronics",
    "Power Bank": "Electronics"
}

statuses = ["Placed", "Shipped", "Delivered", "Cancelled"]
payments = ["UPI", "Card", "Cash", "Wallet"]
channels = ["Online", "Store"]
change_types = ["Restock", "Sale", "Damage"]


# ---------------- INSERT CUSTOMERS ----------------
for _ in range(200):
    cursor.execute("""
        INSERT INTO Customers VALUES (NULL,?,?,?,?,?,?)
    """, (
        fake.name(),
        fake.unique.email(),
        fake.phone_number(),
        fake.city(),
        random.choice([
                       "MH", "KA", "DL", "TN", "TS", "GJ", "RJ", "UP", "MP", "WB"]),
        fake.date_this_year().isoformat()
    ))

# ---------------- INSERT ORDERS ----------------
for _ in range(200):
    dt = fake.date_time_this_year()
    qty = random.randint(1, 8)

    cursor.execute("""
        INSERT INTO Orders VALUES (NULL,?,?,?,?,?,?,?,?,?)
    """, (
        random.randint(1, 200),
        dt.date().isoformat(),
        dt.time().isoformat(),
        random.choice(statuses),
        random.choice(payments),
        random.choice(channels),
        qty,
        round(qty * random.uniform(80, 500), 2),
        round(random.choice([0, random.uniform(10, 150)]), 2)
    ))

# ---------------- INSERT INVENTORY LOGS ----------------
stock = 1000
for _ in range(200):
    product = random.choice(list(products.keys()))
    change = random.choice(change_types)
    qty = random.randint(1, 20)

    stock += qty if change != "Sale" else -qty
    stock = max(stock, 0)

    cursor.execute("""
        INSERT INTO Inventory_Logs VALUES (NULL,?,?,?,?,?,?,?)
    """, (
        product,
        products[product],
        change,
        qty,
        stock,
        fake.date_this_year().isoformat(),
        random.randint(1, 200) if change == "Sale" else None
    ))

# ---------------- INSERT REVIEWS ----------------
for _ in range(200):
    rating = random.randint(1, 5)
    sentiment = round((rating - 3) / 2, 2)

    cursor.execute("""
        INSERT INTO Product_Reviews VALUES (NULL,?,?,?,?,?,?,?)
    """, (
        random.randint(1, 200),
        random.choice(list(products.keys())),
        rating,
        fake.sentence(nb_words=10),
        random.choice([0, 1]),
        sentiment,
        fake.date_this_year().isoformat()
    ))

conn.commit()
conn.close()

print("✅ Database created using Faker (200 rows per table)")
