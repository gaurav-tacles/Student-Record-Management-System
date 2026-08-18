



print("="*50)
print("\tSTUDENT RECORD MANAGEMENT SYSTEM")
print("="*50)
while(True):
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter Your choice [1-7]  : ")
    if(choice == ""):
        print("Choice cannot be blank")
    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a number.")
        continue

    if (choice <0):
        print("Number must be grater than 0")
    elif (choice == 0):
        print("Invalid choice please enter between 1-7")
    elif (choice == 1):
        print("Add")
    elif (choice == 2):
        print("View")
    elif (choice == 3):
        print("Search")
    elif (choice == 4):
        print("Update")
    elif (choice == 5):
        print("Delete")
    elif (choice == 6):
        print("Genterate")
    elif (choice == 7):
        print("Exiting program...")
        break
    else:
        print("Please enter a correct number between 1-7.")
