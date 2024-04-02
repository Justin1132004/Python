
class Person: #Class definition for person
    def __init__(self,name,address,age,phonenumber): #Instance variables for class
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phonenumber = phonenumber

    def get_info(self): #Function to input information
            return f"name: {self.__name} address: {self.__address} age: {self.__age} phone number: {self.__phonenumber}"

def main():

    person1 = Person("Bill", "680 Fake Dr.", "34", "000-023-4015") #Create instances from the person class
    person2 = Person("Murray", "40015 S. Fake Street.", "62", "000-524-3892") 
    person3 = Person("William", "1987 Hurricane Dr.", "51", "000-255-2550")
            
    print(person1.get_info()) #Function prints out the variables set in a string
    print(person2.get_info())
    print(person3.get_info())



main()
