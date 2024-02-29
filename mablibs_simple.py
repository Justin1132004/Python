def madlibs(person, animal, size, color, noun):
    #My madlibs
    print(f"{person} had a {size} {animal} ")
    print(f"Whose fleece was {color} as {noun}")

def get_info():
    person = input("Please enter the name of a person:  ")
    size = input("Please enter a size:  ")
    animal = input("Please enter an animal:  ")
    color = input("Please enter a color:  ")
    noun = input("Please enter a noun:  ")
    return person, size, animal, color, noun

def main():
    person, size, animal, color, noun = get_info()

    madlibs(person,size,animal,color,noun)

main()