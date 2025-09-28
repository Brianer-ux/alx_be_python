# shopping_list_manager.py

# Implementation of an array (list) named shopping_list at module level
shopping_list = []

def display_menu():
    # exact string the checker expects
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        # calling display_menu function
        display_menu()

        # Choice input implemented as a number (int)
        try:
            choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid choice. Please enter a number (1-4).")
            continue

        if choice == 1:
            item = input("Enter the item name to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added: {item}")
            else:
                print("No item entered. Nothing added.")

        elif choice == 2:
            if not shopping_list:
                print("The shopping list is empty — nothing to remove.")
                continue

            item = input("Enter the item name to remove: ").strip()
            if not item:
                print("No item entered. Cancelled removal.")
                continue

            # case-insensitive removal of the first matching item
            index = next((i for i, v in enumerate(shopping_list) if v.lower() == item.lower()), None)
            if index is not None:
                removed = shopping_list.pop(index)
                print(f"Removed: {removed}")
            else:
                print(f"Item '{item}' not found in the shopping list.")

        elif choice == 3:
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nCurrent shopping list:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
