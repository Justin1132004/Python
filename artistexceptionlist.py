def main():
    try: 
        top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
        print(top_artists)
        userreplace = int(input("Please enter the index of an artist to replace: ")) #Get user to choose the number index of the value they want to replace. This is where the errors occur if a non numeric integer is submitted or an index that is higher than the original list.
        userreplacename = input("Please enter the new artist name: ")
        top_artists.pop(userreplace) #Remove the index value given from the user input
        top_artists.insert(userreplace,userreplacename) #Put user index in place of removed index
        print(top_artists) #Show modified list

    except (ValueError, IndexError): #Catch both ValueError and IndexError in exception
        print("An input error occured.")

main()