import json
import os
import csv
from CanBeDownloaded import CanBeDownloaded
from CanbeShipped import CanbeShipped
from Product import Product
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
from ProductFactory import ProductFactory

FILENAME = "inventory.json"

def load_inventory() -> Inventory:
    inventory = Inventory()
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            data = json.load(file)
        for item in data:
            supplier_data = item["supplier"]
            supplier = Supplier(
                supplier_data["supplier_id"],
                supplier_data["name"],
                supplier_data["contact_email"]
            )
            if item["type"] == "physical":
                extra = item["weight"]
            else:
                extra = item["download_size"]
            product = ProductFactory.create(
                item["type"],
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"],
                supplier,
                extra,
                item["history"]
            )
            inventory.add_product(product)
    return inventory

def save_inventory(inventory: Inventory) -> None:
    with open(FILENAME, "w") as file:
        json.dump(inventory.to_list(), file, indent=4)
    print("Inventory saved successfully to", FILENAME)


def get_number(prompt:str, number_type) -> int | float:
    while True:
        try:
            return number_type(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

def show_menu() -> None:
    print("\n===== INVENTORY MENU =====")
    print("1. Display all products")
    print("2. Add product")
    print("3. Update stock")
    print("4. Search product")
    print("5. Save")
    print("6. Deliver Order")
    print("7. Exit")
    print("\n===== DELIVERY & DOWNLOAD RATE SUMMARY =====")
    print(f"Shipping rate: ${PhysicalProduct.SHIPPING_RATE:.2f} per kg")
    print(f"Download rate: ${DigitalProduct.DOWNLOAD_RATE:.2f} per MB")


def main() -> None:
    inventory = load_inventory()
    total_shipped_units = 0
    total_shipping_cost = 0
    total_downloaded_units = 0
    total_download_cost = 0

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Product ID: ").strip()
            name = input("Product name: ").strip()
            if inventory.search_product(name) is not None:
                print("That product already exists. Use Update Stock instead.")
            else:
                price = get_positive_float("Price: ")
                stock = get_number("Starting stock: ", int)
                supplier_id = input("Supplier ID: ").strip()
                supplier_name = input("Supplier Name: ").strip()
                supplier_email = input("Supplier Email: ").strip()
                supplier = Supplier(supplier_id, supplier_name, supplier_email)
                product_type = input("Type (physical/digital): ").strip().lower()
                try:
                    if product_type == "physical":
                        weight = get_number("Weight (kg): ", float)
                        inventory.add_product(ProductFactory.create(product_type, product_id, name, price, stock, supplier, weight))
                        print(f"Added {name}")
                    elif product_type == "digital":
                        download_size = get_number("download size (MB): ", float)
                        inventory.add_product(ProductFactory.create(product_type, product_id, name, price, stock, supplier, download_size))
                        print(f"Added {name}")
                    else:
                        print("Invalid type. Product not added")
                except ValueError as error:
                        print(f"Could not add product: {error}")

        elif choice == "4":
            name = input("Product name to search: ").strip()
            product = inventory.search_product(name)
            if product is None:
                print("Product not found.")
            else:
                product.display_information()

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            name = input("Product name: ").strip()
            product = inventory.search_product(name)
            if product is None:
                print("Product not found.")
            else:
                change = get_number("How many units to be delivered (e.g. 10 or 1): ", int)
                if change <= 0:
                    print("Please enter a positive number for delivery.")
                else:
                    if product.update_stock(-change):
                        print(product.get_fulfilment_info())
                        if isinstance(product, CanbeShipped):
                            cost = product.calculate_shipping_cost() * change
                            print(f"Shipping cost for {change} units of {product.get_name()} is ${cost:.2f}.")
                            total_shipped_units += change
                            total_shipping_cost += cost
                        elif isinstance(product, CanBeDownloaded):
                            cost = product.calculate_download_cost() * change
                            print(f"Download cost for {change} units of {product.get_name()} is ${cost:.2f}.")
                            total_downloaded_units += change
                            total_download_cost += cost

        elif choice == "7":
            save_choice = input("Save before exiting? (y/n): ").strip().lower()
            if save_choice == "y":
                save_inventory(inventory)
            print("\n===== DELIVERY SUMMARY =====")
            print(f"Total shipped units: {total_shipped_units}")
            print(f"Total shipping cost: ${total_shipping_cost:.2f}")
            print(f"Total downloaded units: {total_downloaded_units}")
            print(f"Total download cost: ${total_download_cost:.2f}")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    product_type, product_id, name, price, stock = row
                    product = ProductFactory.create(product_type, product_id, name, float(price), int(stock), supplier)
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as error:
                    print(f"Skipped row {row}: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")

if __name__ == "__main__":
    main()