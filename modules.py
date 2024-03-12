def main():

    import math
    import random


    user_input = int(input("Please enter a number: "))

    randomnum = random.randrange(0,100)
    
    inputdif = abs(user_input - randomnum)

    inputdif = int(input("Please enter exact number: ")) #Just take my inputs now for debugging purposes

    while inputdif <= 5 and inputdif < 15:
        print("Very Hot")
        user_input = int(input("Please enter a number: "))
        inputdif = user_input
    while inputdif > 5 and inputdif <= 15:
        print("Hot")
        user_input = int(input("Please enter a number: "))
        inputdif = user_input
    while inputdif > 15 and inputdif <= 25:
        print("Cool")
        user_input = int(input("Please enter a number: "))
        inputdif = user_input
    while inputdif > 25:
        print("Cold")
        user_input = int(input("Please enter a number: "))
        inputdif = user_input






main()