from tokenize import Name


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
        print("Insert Name of the person")
        name = input("Name: ")
        print("Insert phone number of the person")
        phone = input("Number: ")
        numbers[name] = phone
        print("Phone number of {} is inserted into the phonebook".format(name))
    elif menu_choice == 3:
        print("Whom to delete from phonebook :")
        name = input("")
        if name in numbers:
            del numbers[name]
            print("{} is deleted from the phonebook".format(name))
        else:
            print(name, "'s phone number couldn't find")
    elif menu_choice == 1:
        print("Find the phone number of : ")
        name = input("")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "'s phone number couldn't find")
    elif menu_choice != 4:
        print_menu()
if menu_choice == 4:
    print("Exiting Phonebook")