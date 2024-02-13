#Input grade percentage
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter a grade of 0-100")
grade = int(input())

if grade < 0 or grade > 100: #If the grade input is in this range, return an error.
    print("Invalid grade range")
elif grade >= 90: #If grade is 90-100, give an A
    print("The inputted grade is an A")
elif grade >= 80: #If grade is 80-89, give a B
    print("The inputted grade is a B")
elif grade >= 70: #If grade is 70-79, give a B
    print("The inputted grade is a C")
elif grade >= 60: #If grade is 60-69, give a D
    print("The inputted grade is a D")
elif grade < 60: #If grade is below 60, give an F
    print("The inputted grade is an F")