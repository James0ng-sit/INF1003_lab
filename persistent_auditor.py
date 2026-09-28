MAX_INVENTORY = 500
TAX_RATE = 0.1  # 10% tax rate

print("Smart Inventory Auditor")


def calculate_tax(amount):
    return amount * TAX_RATE


def process_delivery(current_total, new_value):
    return current_total + new_value


def get_valid_input(prompt):
    """Returns (value, invalid_count). value is None if the user quits."""
    invalid = 0
    while True:
        user_input = input(prompt)
        if user_input.lower() == "quit":
            return None, invalid
        if user_input.startswith("-") and user_input[1:].isdigit():
                    print("Error input. Stock quantity cannot be negative.")
                    invalid += 1
                    continue
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid stock quantity (number only).")
            invalid += 1
            continue
    
        return int(user_input), invalid

def load_inventory():
    """Returns (inventory, history). Starts empty if the file is missing or invalid."""
    try:
        with open("inventory.txt", "r") as file:
            inventory = int(file.readline().strip())
            line = file.readline().strip()
            history = [int(x) for x in line.split(",")] if line else []
            if inventory < 0 or inventory > MAX_INVENTORY:
                print("Inventory file contains invalid data. Resetting inventory to 0.")
                return 0, []
            return inventory, history
    except FileNotFoundError:
        print("Inventory file not found. Starting with 0 inventory.")
        return 0, []
    except ValueError:
        print("Inventory file contains invalid data. Resetting inventory to 0.")
        return 0, []

    
def generate_audit_report(inventory, total_units, failed_entries, total_tax):
    print("\n=====Audit report======")
    print("Current inventory:", inventory)
    print("Total delivered units:", total_units)
    print("Failed/Rejected entries:", failed_entries)
    print(f"Total tax collected: {total_tax:.2f}")


def save_inventory(inventory, history):
    with open("inventory.txt", "w") as file:
        file.write(f"{inventory}\n")
        file.write(",".join(map(str, history)))

def main():
    inventory, history = load_inventory()
    total_units = 0
    total_failed_entries = 0
    delivery_count = 0
    total_tax = 0.0

    while True:
        result, invalid = get_valid_input("Enter stock quantity to add (or type 'quit' to exit): ")
        total_failed_entries += invalid

        if result is None:
            generate_audit_report(inventory, total_units, total_failed_entries, total_tax)
            save_inventory(inventory, history)
            print("Exiting the program.")
            break


        if result > MAX_INVENTORY:
            print("Error input. Stock quantity cannot exceed 500.")
            total_failed_entries += 1
            continue

        if inventory + result > MAX_INVENTORY:
            print("Overflow error. Cannot add stock quantity. Current inventory:", inventory)
            total_failed_entries += 1
            continue

        inventory += result
        history.append(result)
        total_units = process_delivery(total_units, result)
        tax = calculate_tax(result)
        total_tax += tax
        delivery_count += 1
        print(f"Accepted {result} units. Tax on this delivery: {tax:.2f}. Current inventory: {inventory}")



try:
    main()
except KeyboardInterrupt:
    print("\nProgram interrupted.")