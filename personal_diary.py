def main():

    date = input("What is today's date: ")
    diaryentry = input("What did you do today? \n")
    record = open('diary.txt', 'a') #Open diary.txt internally so that we can modify it
    record.write(f"{date} \n\n{diaryentry}\n\n") #Write in the lines including the user specified date and entry.
    record.close() #Close the file internally


main()