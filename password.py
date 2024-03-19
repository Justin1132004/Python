def main():
    valid = False
    while not valid: #Loop this if the password is not valid
        hasuppercase = False
        haslowercase = False
        hasnumber = False
        hassymbol = False
        valid = True
        symbolt = ['!', '@', '#', '$', '%', '&', '*']
        print("Password must be: \n" "between 8 to 20 characters long. \n" 
            "Contain at least one uppercase letter. \n"
                "Contain at least one lowercase letter. \n" 
                "Include at least one number. \n"
                "Includes at least one symbol from the set: !@#$%&*.")
        
        userpassword = input("\n\nPlease enter your password: ")

        if len(userpassword) < 7 or len(userpassword) > 21: #If password is not a number between 7 and 21 (8 to 20), invalid password
            print("Password must be between 8 to 20 characters long")
            valid = False
        else:
             continue

        for chara in userpassword: # Loop through characters in the user inputted password
            if chara.isupper(): # Catch any capital letters and switch hasuppercase flag to true
               hasuppercase = True
            else:
                valid = False
                continue
        if hasuppercase == False:
            print("Password must contain at least one uppercase letter.")
        
        for chara1 in userpassword: # Loop through characters in the user inputted password
            if chara1.islower(): # Catch any lowercase letters and switch haslowercase flag to true
               haslowercase = True
            else:
                valid = False
                continue
        if haslowercase == False:
            print("Password must contain at least one lowercase letter.")

        for chara2 in userpassword: # Loop through characters in the user inputted password
            if chara2.isnumeric(): # Catch any numbers and switch hasnumber flag to true
               hasnumber = True
            else:
                valid = False
                continue
        if hasnumber == False:
            print("Password must contain at least one number.")

        for chara3 in userpassword: # Loop through characters in the user inputted password
            if chara3 in symbolt: # Catch any variables from the "symbol" tupple and switch to true
                hassymbol = True
            else:
                valid = False
                continue
        if hassymbol == False:
                print("Password must contain at least one symbol from the set: !@#$%&*.")

    if valid == True: #Yay, the password went through all checks and is valid!
            print("Password accepted")



main()
