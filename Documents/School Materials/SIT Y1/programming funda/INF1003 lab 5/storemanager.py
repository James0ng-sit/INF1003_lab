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

def search_item(inventory, item_name):
    """Return the prodcut from the dictionary if it exists, otherwise return None."""
    for product in inventory:
        if product['name'].lower() == item_name.lower():
            return product
    return None
