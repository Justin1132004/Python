print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnter an integer")

userint1 = int(input("")) #User inputs first integer

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEnter another integer")

userint2 = int(input("")) #Second integer

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

if userint1 > 0 and userint2 > 0:
    print("\n\nBoth numbers are positive")
elif userint1 == 0 or userint2 == 0:
    print("\nOne or both numbers are zero")
else:
    print("\nOne or both numbers are negative")

if userint1 > userint2:
    print(f"\n{userint1} is greater than {userint2}")
elif userint1 == userint2:
    print("\nBoth inputs are the same")
else:
    print(f"\n{userint2} is greater than {userint1}")

if userint1 % 2 == 0:
    print(f"\n{userint1} is an even number")
else:
    print(f"\n{userint1} is an odd number")

if userint2 % 2 == 0:
    print(f"\n{userint2} is an even number")
else:
    print(f"\n{userint2} is an odd number")