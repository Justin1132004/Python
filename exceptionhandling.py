
# Simple Python program to calculate the square of a number

def square_number():
    try:

        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")

    except ValueError: #If user inputs an invalid character, explain value error.

        print("Value Error: That won't work, you need to put in a valid number.")
        square_number() #Rerun the function
    except:
        print("Something went wrong!")

square_number()
    
