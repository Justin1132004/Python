# Start with a try
def main():
    try:
        print(10/0)
        my_list=(1,2,3,4)
        print(my_list[5])


    except IndexError:
        print("Index error!")
    except ZeroDivisionError:
        print("You are not allowed to divide by zero.")
    except:
        print("That won't work!")

    else:
        print("Division successful!")
    finally:
        print("Execution completed. Well done, 47.")









main()