"""
    CRUD application for creating an address book.
    This will have some problems in it. you may solve the problems 
    for extra credit:
    Does not allow for duplicate names to be properly handled
    Search searches the entire entry not a specific field


    🚨 Avoid project creep!


"""


def main_menu():
    # present menu
    # Check values 
    # return choice
    main()

def check():
    # read file to list
    # if file not there create empty customer list
    # return customer list
    main()

def save():
    # save the file
    main()

def create():
    # create a new entry
    # call the save  function
    main()

def read():
    # will call the search function
    # will display the found record
    main()

def search():
    # called by - read, update, delete
    # returns - record, index
    print("Search")

def update():
    # updates a record
    # uses search function
    main()

def delete():
    # calls search
    # verifies that it is the record to delete
    # deletes the record
    main()



def main():
    choice = main_menu()

main()