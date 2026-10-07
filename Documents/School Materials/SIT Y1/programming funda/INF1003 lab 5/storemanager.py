import json
import os

FILENAME = "inventory.json"

def load_inventory():
    """Load the inventory.json file if it exists, otherwise return an empty list."""
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

def save_inventory(inventory):
    """Save the inventory to the inventory.json file."""
    with open(FILENAME, 'w') as file:
        json.dump(inventory, file, indent=4)
        print("Inventory saved successfully to", FILENAME)

def search_product(inventory, name):
    """Return the product dictionary that matches the name, or None."""
    for product in inventory:
        if product["name"].lower() == name.lower():
            return product
    return None


def add_product(inventory, name, price, stock):
    """Add a new product (a dictionary) to the inventory list."""
    if search_product(inventory, name) is not None:
        print("That product already exists. Use Update Stock instead.")
        return
    product = {
        "name": name,
        "price": price,
        "stock": stock,
        "history": [stock],  # every stock change is recorded here
    }
    inventory.append(product)
    print(f"Added {name}.")


def update_stock(inventory, name, change):
    """Change stock by a number. Positive = restock, negative = sale/removal."""
    product = search_product(inventory, name)
    if product is None:
        print("Product not found.")
        return
    if product["stock"] + change < 0:
        print("Not enough stock. Current stock is", product["stock"])
        return
    product["stock"] += change
    product["history"].append(change)  # keep the transaction, not just the total
    print(f"{name} stock is now {product['stock']}.")


def display_all(inventory):
    """Print every product with its price, stock, and transaction history."""
    if len(inventory) == 0:
        print("Inventory is empty.")
        return
    print(f"{'Name':<15}{'Price':>10}{'Stock':>8}   History")
    print("-" * 55)
    for product in inventory:
        print(f"{product['name']:<15}{product['price']:>10.2f}{product['stock']:>8}   {product['history']}")

def add_product(inventory, name, price, stock):
    """Add a new product (a dictionary) to the inventory list."""
    if search_product(inventory, name) is not None:
        print("That product already exists. Use Update Stock instead.")
        return
    product = {
        "name": name,
        "price": price,
        "stock": stock,
        "history": [stock],  # every stock change is recorded here
    }
    inventory.append(product)
    print(f"Added {name}.")


def update_stock(inventory, name, change):
    """Change stock by a number. Positive = restock, negative = sale/removal."""
    product = search_product(inventory, name)
    if product is None:
        print("Product not found.")
        return
    if product["stock"] + change < 0:
        print("Not enough stock. Current stock is", product["stock"])
        return
    product["stock"] += change
    product["history"].append(change)  # keep the transaction, not just the total
    print(f"{name} stock is now {product['stock']}.")


def display_all(inventory):
    """Print every product with its price, stock, and transaction history."""
    if len(inventory) == 0:
        print("Inventory is empty.")
        return
    print(f"{'Name':<15}{'Price':>10}{'Stock':>8}   History")
    print("-" * 55)
    for product in inventory:
        print(f"{product['name']:<15}{product['price']:>10.2f}{product['stock']:>8}   {product['history']}")


def get_number(prompt, number_type):
    """Keep asking until the user types a valid number."""
    while True:
        try:
            return number_type(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def show_menu():
    print("\n===== INVENTORY MENU =====")
    print("1. Display all products")
    print("2. Add product")
    print("3. Update stock")
    print("4. Search product")
    print("5. Save")
    print("6. Exit")