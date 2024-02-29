def factorial(n): #Gets the factorial of a specified number(n)
    print
    if n == 1 or n == 0: #If n is 0 or 1, return 1. Else multiply n by the function of itself minus 1.
        return 1
    else:
        return n * factorial(n-1)

def main(): #Runs the code to get the user input and run it through the factorial function.
    fact = int(input("Please enter the number you will be finding factorials of: ")) #Get user input for which number to get factorials from
    print(f"The factorial of {fact} is {factorial(fact)}") #Use the factorial function to get the factorial of the number

main()