count = 99
while count > 1:
    print(f"{count} bottles of beer on the wall")
    print(f"{count} bottles of beer")
    print("Take one down, pass it around")
    count -= 1
    if count == 1: print("1 bottle of beer\n\n")
    else: print(f"{count} bottles of beer\n\n")

if count == 1:
    print(f"{count} bottle of beer on the wall")
    print(f"{count} bottle of beer")
    print("Take it down, pass it around")
    print("No bottles of beer on the wall!")