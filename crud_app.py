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
        file = open("customer_directory", "r")
        curcustomer = file.readlines()
        file.close()
        return curcustomer
    except FileNotFoundError as e:
        print("List does not exist, creating..")
        curcustomer = []
        return curcustomer
    except Exception as e:
        print(f"Something went horribly wrong: {e}")

def read():
    #Call Search
    print("Reading an entry...")

    found_customer,found_index = search()

    print(f"System Found Customer: {found_customer} at index {found_index}")

def search():
    #Called by read, update, delete
    #Returns record, index
    try:
        customers = check()

        recordtosearchfor = input("Please enter a name or part of a name to look for: ")
        for cust in customers:
            if recordtosearchfor in cust:
                customer_index = customers.index(cust)
                return cust, customer_index
        else:
                print("Entry does not exist")
        
    except Exception as e:
        print(f"Something went horribly wrong searching when searching the entry: {e}")

def update():
    try:
        found_customer,found_index = search() #Call search function to find a customer's information
        customerlist = found_customer.split(", ")
        firstname = customerlist[0]
        lastname = customerlist[1]
        phone = customerlist[2]
        email = customerlist[3]
        print(f"1. First Name: {firstname} \n2. Last Name: {lastname} \n3. Phone Number: {phone} \n4. Email: {email}") #List off the current customer's current entrys
        choice = input("Please enter the number of the entry you want to change: ") #Give user choice on which aspect of the customer's entry to change.
        if choice == "1":
            firstname = input("Please enter new first name: ")
        elif choice == "2":
            lastname = input("Please enter new last name: ")
        elif choice == "3":
            phone = input("Please enter new phone number: ")
        elif choice == "4":
            email = input("Please enter new email: ")
        entry = ("\n" + firstname + ", " + lastname +  ", " + phone +  ", " + email + "\n") #Create new entry based on user input
        print(entry)
        customer = check()
        del customer[found_index]
        customer.append(entry) #Add new entry to direectory
        save(customer)

        print("Updating an entry...")
    except Exception as e:
        print(f"Something went horribly when when updating entry: {e}")


    main()

def delete():
    try:

        found_customer,found_index = search() #Search for entry to delete
        customer = check()
        confirmation = input("Are you sure you want to delete this entry? (y/n)")
        if confirmation == "y":
            del customer[found_index] #Delete found entry if user inputs y
            print("Deleting an entry..")
            save(customer)
        else:
            print("Deletion cancelled..") #Cancel the interaction and return to menu if anything else is inputted



    except Exception as e:
        print("Something went horribly wrong when deleting entry: {e}")

    
    main()
    
def create():
    #create new entity
    #call save
    try:
        customer = check() #Call check function to make sure the customer_directory file exists before a new entry is made.
        print("\n Please enter the customer information")
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        entry = (firstname + ", " + lastname +  ", " + phone +  ", " + email + "\n")
        customer.append(entry) #Append the user inputted entries to the customer list
        for line in customer:
            print(line)
        save(customer)
    except Exception as e:
        print(f"Something went horribly wrong: {e}")
    main()

def save(curcustomer):
    try:
        file = open("customer_directory", "w") #Open to customer_directory
        for line in curcustomer: #For every line that is in the customer defined in create() write that line to the file
            file.write(line)
        file.close()
        print("File saved!")
    except Exception as e:
        print(f"Something went horribly wrong: {e}")
    main()

def main():
    choice = main_menu()
    try: #User chooses from 1-4, exit the program if anything else is given.
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        else:
            print("Exiting Program..") 
    except Exception as e:
        print(f"Something went wrong: {e}")


main()
