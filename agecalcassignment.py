print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlease input your age.")

age = int(input()) #Get user input age

print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou are {age}:\n")
if age >= 16: print(f"You are old enough to drive at {age}, legal age: 16") #If I'm 16, I can drive. If am younger than 16, I am not old enough to drive.
else: print(f"You are not old enough to drive at {age}, legal age: 16")

if age >= 18: print(f"You are old enough to vote at {age}, legal age: 18")
else: print(f"You are not old enough to vote at {age}, legal age: 18")

if age >= 21: print(f"You are old enough to purchase alcohol at {age}, legal age: 21")
else: print(f"You are not old enough to purchase alcohol at {age}, legal age: 21")

if age >= 55: print(f"You are old enough for the senior discount at various locations at {age}.")
else: print(f"You are generally not old enough to the senior discount at {age}.")
    
if age >= 99 and age < 116: print(f"\nSidenote: If you are over {age} years of age, you are probably dead. If you aren't then congratulations on your good life choices.")
if age >= 116: print(f"\nSidenote: If you are over {age} years of age then you are older than the oldest recorded human to ever live and are a probably an eldrich entity, in which case you probably are not subject to human laws.")