#Our list values to access
time_slots = ["Morning","Midday","Afternoon","Evening"]
time = []
dailyheartrate = []

for time in time_slots: #Get user input for each time listed in the list. Loop until there is an input for every time value.
    heartrate = int(input(f"Please enter your heart rate during the {time}: "))
    dailyheartrate.append([time,heartrate])

total = 0
for heartbpm in dailyheartrate:
    total += heartbpm[1] #Use loop to collect each input from the user

average = round(total / len(heartbpm)) #Round out the inputs
print(f"Your average heart rate during the day was {average} bpm.")