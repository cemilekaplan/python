def print_menu():
    print('1. Find phone number')
    print('2. Insert a phone number')
    print('3. Delete a person from the phonebook')
    print('4. Terminate')
    
    print()

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 4:
    menu_choice = int(input("Type in a number (1-4): "))
    
    if menu_choice == 2:
        print("Insert Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Delete Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 1:
        print("Find Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 4:
        print_menu()