inventory = 0
failed_entries = 0
print ("Smart inventory Auditor")

while True:
    User_input = input("Please enter stock quantities or Please enter Quit to exit: ")

    if User_input.lower() == "quit":
        print("=====Audit report======")
        print("Current inventory: ", inventory)
        print("failed entries: ", failed_entries)
        break
    

    elif not User_input.isdigit():
        print("Invalid input. Please enter a valid stock quantity hint: number only.")
        failed_entries += 1
        continue


    quantity = int(User_input)

    if quantity < 0:
        print("Error input. Stock quantity cannot be negative.")
        failed_entries += 1
        continue

    if quantity > 500:
        print("Error input. Stock quantity cannot exceed 500.")
        failed_entries += 1
        continue

    total_stock = inventory + quantity

    if total_stock <= 500:
        inventory = total_stock
        print("Stock quantity updated. Current inventory: ", inventory)

    elif total_stock > 500:
        print("Overflow error. Cannot add stock quantity. Current inventory: ", inventory)
        failed_entries += 1
        break

    if failed_entries >= 4:
        print("Too many failed entries. Exiting the program.")
        break

    if inventory == 500:
        print("Inventory limit reached. Cannot add more stock.")
        print("=====Audit report======")
        print("Current inventory: ", inventory)
        print("failed entries: ", failed_entries)
        break