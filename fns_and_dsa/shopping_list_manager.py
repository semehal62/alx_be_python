def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item_add = input("Enter the item to add: ")
            shoppint_list.append(item_add)
        
        elif choice == '2':
            item_remove = input( "Enter the item to removed: ")
            shopping_list.remove( item_removed)       
        elif choice == '3':
            print(shoping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
