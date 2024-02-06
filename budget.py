#Total Budget to calculate
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter your budget")
budget = int(input())

#Input costs
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter much you spend on rent")
housingcost = int(input())
housingcostp = int(housingcost / budget * 100) #Calculate the percentage of the input choice to the budget

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter how much you spend on utilities")
utilcost = int(input())
utilcostp = int(utilcost / budget * 100)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter how much you spend on groceries")
grocost = int(input())
grocostp = int(grocost / budget * 100)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter how much you spend on transportation")
transcost = int(input())
transcostp = int(transcost / budget * 100)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter how much you spend on health care")
healthcost = int(input())
healthcostp = int(healthcost / budget * 100)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter how much you spend on personal care")
personcost = int(input())
personcostp = int(personcost / budget * 100)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease enter how much you spend on clothing")
clothcost = int(input())
clothcostp = int(clothcost / budget * 100)

total = int((housingcost + utilcost + grocost + transcost + healthcost + personcost + clothcost) / budget * 100) # Get the total percentage put together

#Give the user a rundown of their choices.
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(f"your total budget was {budget}")
print(f"{housingcostp} percent of which was spent on rent.", end='\n')
print(f"{utilcostp} percent of which was spent on utilities.", end='\n')
print(f"{grocostp} percent of which was spent on groceries.", end='\n')
print(f"{transcostp} percent of which was spent on transportation.", end='\n')
print(f"{healthcostp} percent of which was spent on healthcare.", end='\n')
print(f"{personcostp} percent of which was spent on personal care.", end='\n')
print(f"{clothcostp} percent of which was spent on clothing.", end='\n')

if total <= 100: #If percentage of budget exceeds 100%, go into debt.
    print(f"\nYou spent {total} percent of your total budget.", end='\n')
else:
    debt = (housingcost + utilcost + grocost + transcost + healthcost + personcost + clothcost) - budget #Everything spent minus budget
    print(f"\nYou spent 100 percent of your overall budget and are now {debt} dollars in debt.")
