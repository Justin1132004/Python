"""""""""""""""""

Crud Application

"""""""""""""""""

def main_menu():
     print("Menu:")
     while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")
    
def check():
    #Read file list, if no file then create one.
    #If list exists then return list
    print("Checking the system...")
    try:
        file = open("customer_directory.txt", "r")
        customer = file.readlines()
        file.close()
    except FileNotFoundError:
        print("List does not exist, creating..")
        customer = []
        return customer
    except Exception as e:
        print(f"Something went horribly wrong: {e}")

def read():
    print("Reading an entry...")

def update():
    print("Updating an entry...")

def delete():
    print("Deleting an entry...")
    
def create():
    #create new entity
    #call save
    try:
        customer = check()
        print("\n Please enter the customer information")
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        entry = {f"{firstname}, {lastname}, {phone}, {email}"}
        customer.append(entry)
        for line in customer:
            print(line)
        save(customer)
    except Exception as e:
        print(f"Something went horribly wrong: {e}")
    main()

def save(output):
    try:
        file = open("customer_directory", "w") #Open to customer_directory
        for line in output: #For every line that is in the customer defined in create() write that line to the file
            file.write(line)
        file.close()
        print("File saved!")
    except Exception as e:
        print(f"Something went horribly wrong: {e}")
    main()

def main():
    choice = main_menu()
    try:
        if choice == 1:
            create()
        elif choice == 2:
            print("a")
        elif choice == 3:
            print("a1")
        elif choice == 4:
            print("a2")
        else:
            print("Thank-a you so much for to playing my game") 
    except Exception as e:
        print(f"Something went wrong: {e}")


main()