
items = [
    "pipe",
    "sink",
]
def delete_items():
    for i,item in enumerate(items,start=1):
        print(f"{i:<5} {item['name']:<15} {item['quantity']:<10} {item['size']:<10} {item['type']:<10}")
        delete_choice = int(input("Enter the number you want to delete: "))
        if 1<= delete_choice <= len(items):
            items.pop(delete_choice - 1)
        else:
            print("Invalid...")
delete_items()
print(items)



