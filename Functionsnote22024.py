#Class notes, functions sandbox

"""
# define a function
def fun(adjective):
    print(f"Functions are {adjective}!")

fun("rad, man")
"""

# calculate sales tax
TAX = .05 # tax is a constant, she capitalizes constants
def main():
    sales_total = sales() # assigning result of a function to a variable
    sales_tax(sales_total) # passing a variable to a function
    print(f"sales_total: {sales_total}")

#Having a function and a variable with the same name = shadow error
def sales_tax(sales_total): #variable becomes parameter
    sales_total = 1000.0
    tax_amount = sales_total * TAX
    print(tax_amount)

def sales():
    my_sales = float(input("What is the price: "))
    return my_sales

main()