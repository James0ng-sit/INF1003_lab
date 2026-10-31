import json
import os
from Product import Product
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

FILENAME = "inventory.json"

def load_inventory():
    inventory = Inventory()
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            data = json.load(file)
        for item in data:
            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"],
                    item["history"]
                )
            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"],
                    item["history"] 
                )
            inventory.add_product(product)
    return inventory

def save_inventory(inventory):
    with open(FILENAME, "w") as file:
        json.dump(inventory.to_list(), file, indent=4)
    print("Inventory saved successfully to", FILENAME)


def get_number(prompt, number_type):
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


def main():
    inventory = load_inventory()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Product ID: ").strip()
            name = input("Product name: ").strip()
            if inventory.search_product(name) is not None:
                print("That product already exists. Use Update Stock instead.")
            else:
                price = get_number("Price: ", float)
                stock = get_number("Starting stock: ", int)
                inventory.add_product(Product(product_id, name, price, stock))
                print(f"Added {name}.")

        elif choice == "3":
            name = input("Product name: ").strip()
            product = inventory.search_product(name)
            if product is None:
                print("Product not found.")
            else:
                change = get_number("Change in stock (e.g. 10 or -3): ", int)
                product.update_stock(change)

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
            save_choice = input("Save before exiting? (y/n): ").strip().lower()
            if save_choice == "y":
                save_inventory(inventory)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

print("===== PHYSICAL PRODUCTS =====")
guitar =  PhysicalProduct ("G001", "Guitar", 50, 10, 5)
guitar.display_information()
print(guitar.get_fulfilment_info())
print(f"Guitar Shipping Cost: ${guitar.calculate_shipping_cost():.2f}")
print() #use to make space 

drum = PhysicalProduct ("G002", "Drum", 100, 10, 10)
drum.display_information()
print(guitar.get_fulfilment_info())
print(f"Drum Shipping Cost: ${drum.calculate_shipping_cost():.2f}")

print("\n===== DIGITAL PRODUCTS =====")
Mac_OS =  DigitalProduct ("D001", "Mac OS", 100, 100, 4500)
Mac_OS.display_information()
print(Mac_OS.get_fulfilment_info())
print(f"Mac OS Download Cost: ${Mac_OS.calculate_download_cost():.2f}")

if __name__ == "__main__":
    main()
    pass