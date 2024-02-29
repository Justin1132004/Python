def main():
    programming_classes={"Intro to Python","Advanced Python","Database Essentials","Web Development Basics","Data Structures in Python","Web Design Fundamentals"}
    for pclass in programming_classes: #Loop through the tuple and print the name of each class
        print(pclass)

    print(f"There are {len(programming_classes)} programming classes in the tuple.") #Get and print how many classes are in the tuple
main()