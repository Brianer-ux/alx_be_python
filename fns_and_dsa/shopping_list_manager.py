def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item name to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added: '{item}'")
            else:
                print("No item entered. Nothing added.")

        elif choice == '2':
            if not shopping_list:
                print("The shopping list is empty — nothing to remove.")
                continue

            item = input("Enter the item name to remove: ").strip()
            if not item:
                print("No item entered. Cancelled removal.")
                continue

            # case-insensitive removal, removes the first matching item
            index = next((i for i, v in enumerate(shopping_list) if v.lower() == item.lower()), None)
            if index is not None:
                removed = shopping_list.pop(index)
                print(f"Removed: '{removed}'")
            else:
                print(f"Item '{item}' not found in the shopping list.")

        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nCurrent shopping list:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
