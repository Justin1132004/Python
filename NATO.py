def get_word():
    userword = input("Please enter a word: ").upper() #Ask user to input word
    nato_alphebet = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliette","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-ray","Y":"Yankee","Z":"Zulu"}
    for v in userword: #Get each letter in the user inputted word
        print(nato_alphebet.get(v)) #Get tupple's equivalent of the letter

def main():

    get_word() #Run the get_word function
 

main()
