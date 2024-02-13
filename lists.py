print("Please input five names:") #User inputs five names below prompt
name1 = input()
name2 = input()
name3 = input()
name4 = input()
name5 = input()

nameslist = [name1,name2,name3,name4,name5]
swapped = True

for i in range (0,len(nameslist)): #Cycle through inputs and put them all in lower case
    nameslist[i] = nameslist[i].lower()

while swapped:
    swapped = False 
    for i in range(len(nameslist) - 1):
        if nameslist[i] < nameslist[i + 1]:
            swapped = True #Check if variable is swapped, if variable is swapped then change list with swapped variables until they are all swapped.
            nameslist[i], nameslist[i + 1] = nameslist[i + 1], nameslist[i]

print(nameslist)

nameslist.reverse() #Reverse next print order

print(nameslist)