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
        print(birthdate)
        birth = birthdate.strftime("%Y-%m-%d")
        print(birth)
    except Exception as e:
        print(f"Something went horribly wrong: {e}")
        main()



    #birthday = datetime.strptime(birthdayinput, "%Y-%m-%d")
    #print(birthday)
    #print(datetime.now().time())
    #print(datetime.now() / timedelta(birthday))



main()