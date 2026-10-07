import json
import os

FILENAME = "inventory.json"

def load_inventory():
    """Load the inventory.json file if it exists, otherwise return an empty list."""
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []