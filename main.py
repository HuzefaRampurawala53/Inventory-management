
items = []

def add_items():
    name = input("Enter item to add: ").strip().lower()

    while True:
        try:
            quantity = int(input("Enter the Quantity: ").strip())
            size = int(input("Enter the Size: ").strip())
            break
        except ValueError:
            print("Please enter valid whole numbers for quantity and size.")

    item_type = input("Enter type (cpvc/upvc) or n if none : ").strip().lower()
    if item_type == "n" or item_type == "":
        item_type = "None"
    elif item_type == "c":
        item_type = "CPVC"
    elif item_type == "u":
        item_type = "UPVC"
    else:
        pass 
         

    items.append({'name': name, 'quantity': quantity, 'size': size, 'type': item_type})

def show_items():
    if not items:
        print("No items are available")
        return

    print(f"{'Name':<15} {'Quantity':<10} {'Size':<10} {'Type':<10}")
    print("-" * 50)
    for item in items:
        print(f"{item['name']:<15} {item['quantity']:<10} {item['size']:<10} {item['type']:<10}")

def delete_items():
    if not items:
        print("No items are available to delete.")
        return

    print("Current items:")
    print(f"{'#':<5} {'Name':<15} {'Quantity':<10} {'Size':<10} {'Type':<10}")
    print("-" * 60)
    for i, item in enumerate(items, start=1):
        print(f"{i:<5} {item['name']:<15} {item['quantity']:<10} {item['size']:<10} {item['type']:<10}")

    while True:
        try:
            choice = int(input("Enter the number of the item to delete: ").strip())
            if 1 <= choice <= len(items):
                deleted_item = items.pop(choice - 1)
                print(f"Deleted item: {deleted_item['name']}")
                break
            else:
                print(f"Please enter a number between 1 and {len(items)}.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("---INVENTORY MANAGEMENT SYSTEM---")
        choice = input("Enter choice:\n1. Add items\n2. Display the inventory items\n3. Delete items\n4. Exit\n: ").strip()
        if choice == "1":
            add_items()
        elif choice == "2":
            show_items()
        elif choice == "3":
            delete_items()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Please choose 1, 2, 3 or 4.\n")

if __name__ == "__main__":
    main()




