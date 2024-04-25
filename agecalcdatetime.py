"""""""""""""""""""""""""""

Age calculation assignment


"""""""""""""""""""""""""""

from datetime import datetime #Import datetime module
from datetime import timedelta #Import timedelta from datetime module

def main():


    try:
        today = datetime.today()
        birthyear = int(input("What year were you born? "))
        birthmonth = int(input("what month were you born? (As a number from 1-12) "))
        birthday = int(input("What day of the month were you born? "))
        birthdate = datetime(birthyear, birthmonth, birthday) #Turn user inputs into date 
        birth = birthdate.strftime("%Y-%m-%d")
        timedifference = today - birthdate #Difference between the inputted date and today's date
        timedifferencedays = timedifference.days #Get days in the differenced date
        timedifferenceyears = timedifferencedays // 365 #Divide total days by 365 to get one year
        timedifferencemonths = timedifferencedays // 30.41 #Divide total days by 30 to get months, not 100% accurate.
        timedifferenceweeks = timedifferencedays // 7
        print(f"You were born on {birth}. You are {timedifferenceyears} years, {timedifferencemonths} months, {timedifferenceweeks} weeks, and {timedifferencedays} days old.")
    except Exception as e:
        print(f"Something went horribly wrong: {e}")
        main()



main()
