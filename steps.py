days = ["Sunday","Monday","Tuesday","Wedesnesday","Thursday","Friday","Saturday"] #list of days
steps = [] #Storage lists for user input
total = 0

for day in days:
    stepinput = int(input(f"Please enter how many steps you took on {day}: ")) #Get user input from each variable in the list
    steps.append([day,stepinput])
    total = total + stepinput

for i in steps: #Look through steps list and give the user each of their daily inputs
    print(f"You took {i[1]} steps on {i[0]}")

average = round(total / len(steps))

print(f"Total Steps: {total}")
print(f"Average steps: {average}")