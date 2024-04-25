"""""""""""""""""""""

calendar assignment


"""""""""""""""""""""

from datetime import datetime

import calendar

def main():

    try:
        currentyear = datetime.now().year #Get current year
        birthmonth = int(input("Please enter your birth month (As a number from 1-12) ")) #Have user input their birthmonth
        if birthmonth > 12 or birthmonth < 1: raise ValueError #Raise an error if the user's input is out of range of the 12 months.

        print(calendar.month(currentyear,birthmonth))




    except ValueError: #Catch invalid non integer inputs
        print("Error: Please enter a valid month number from 1-12")
        main()

    except Exception as e:
        print(f"Something went wrong: {e}")
        main()




main()