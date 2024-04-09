class Employee:
    #Main employee super-class
    def __init__(self, employeename, employeenumber):
        self.employeename = employeename
        self.employeenumber = employeenumber

    def __str__(self):
        return f"Employee name: {self.employeename} \nEmployee number: {self.employeenumber} \n"
    
class ProductionWorker(Employee):
    #Subclass of Employee
    def __init__(self, employeename, employeenumber, shiftnumber, hourlypay):
        super().__init__(employeename,employeenumber) #Inherit employee name and number from employee superclass
        self.shiftnumber = shiftnumber

        if shiftnumber == 1: self.shiftnumber = "day"
        else: self.shiftnumber = "night"

        self.hourlypay = hourlypay

    def __str__(self):
        return super().__str__() + f"Shift number: {self.shiftnumber} \nHourly pay: {self.hourlypay}"


def main():
    print("Please enter the following details of the employee: \n") 
    
    nameinput = input("Please input Employee name: ") #Get user input for each of the class objects.
    numberinput = int(input("Please input employee number: "))
    shiftinput = int(input("Please enter shift number: "))
    payinput = int(input("Please enter rate of pay:"))

    inputemployee = ProductionWorker(nameinput,numberinput,shiftinput,payinput) #ProductionWorker instance with user inputted objects
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(inputemployee)

    







main()