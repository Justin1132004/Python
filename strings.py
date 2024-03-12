def main():

    user_input = input("Enter a character: ") #Get user inputted character

    while len(user_input) != 1: #If user inputs more than one character or none at all, repeat the prompt and loop until they input one character.
        print("Please enter exactly one character")
        user_input = input("Enter a character: ")

    ascii_value = ord(user_input) #Get the ascii value for the user inputted character

    print(f"The ascii value of {user_input} is {ascii_value}")






main()
