"""
Database configuration for FoodExpress.

⚠  IMPORTANT: edit DB_PASSWORD below to match the MySQL root password
   that YOU set during the MySQL Installer setup on this machine.
"""

DB_CONFIG = {
    "host":     "localhost",
    "port":     3306,
    "user":     "root",
    "password": "abc123",  # <-- EDIT ME
    "database": "food_ordering_db",
    "charset":  "utf8mb4",
    "use_pure": True,
    "autocommit": False,
}

# Flask app config
SECRET_KEY = "change-this-to-something-random-for-production"
DEBUG = True
PORT = 5000
