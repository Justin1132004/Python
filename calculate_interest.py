def calculate_interest(principal, rate, time): #Function to calculate the values
    totalcalc = (principal * rate * time) / 100
    return totalcalc

def main():
    principal_amount = int(input("Enter the principal amount: "))
    interest_rate = int(input("Enter the interest rate as a whole number: "))
    time = int(input("Enter the investment time in years: "))
    
    total = calculate_interest(principal_amount,interest_rate,time) #Use the function to calculate the inputted valuess
    print(f"The simple interest for a principal amount of ${principal_amount:,.2f} at an interest rate of {interest_rate}% over a period of {time} years is: ${total:,.2f}")

main()