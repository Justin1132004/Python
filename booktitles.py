def main():

    booklist = [""] #Empty list to add user input to
    user_input = input("Please input the name of a book: ")
    booklist.append(user_input) #Adds user input to the empty list
    books = 9

    while books > 0: #Loop inputs until books count reaches 0
        user_input = input("Please input the name of a book: ")
        booklist.append(user_input)
        books -= 1

    sortedlist = sorted(booklist) #Sort the book list
    
    for book in sortedlist: #Print each variable in the sorted list
        print(book)
        




main()