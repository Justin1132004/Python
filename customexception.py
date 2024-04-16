class InvalidInputError(ValueError): #Custom exception for non numeric/out of range input
    def __init__(self,message="That number is not a number between 1 and 10. Do you think this is a joke?"):
        self.message = ValueError

def main():
    try:
        value = input("Pick a number, any number between 1 and 10!\n") #String to be converted into input, isnumeric() only takes strings so this was a hacky method
        valueint = int(value) #Convert the string into an integer value so that it can be compared as lesser or greater
        if valueint > 10 or valueint < 1 or value.isnumeric() == False:
            raise InvalidInputError() #Raise our custom error if these conditions are met
    except InvalidInputError:
        print("That is not a number between 1 and 10. Do you think this is a joke?")
    except ValueError:
        print("That is not a number. You fool, you absolute buffoon. Are you genuinely stupid or are you trying to make me look like a fool!? You lose! Good DAY SIR.")
    except Exception as e:
        print(f"This is what went wrong: {e}") #Explain any errors that we haven't caught with a special exception
        main()
    else:
        print(f"Thank you! Was {value} your number?")
    finally:
        print(f"Thank you so much-a for to playing my game!")

main()