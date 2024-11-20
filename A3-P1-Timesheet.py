#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #: W0516070     
#Student Name: Valentine Byrnes  


# YOUR CODE STARTS HERE, each line must be indented (one tab)

#User can input number of hours worked for 5 separate days.
def hoursInput():
    hrsDay = []
    days = [1, 2, 3, 4, 5]
    for i in range(len(days)):
        hrs = input("Enter hours worked on day #{0}: ".format(i + 1))
        while '+' in hrs or validNumber(hrs) == False:
            if '+' in hrs:
                print("Invalid input. Please enter a number from 0 to 24.")
            else:
                print("Invalid input. Please enter a number from 0 to 24.")
            hrs = input("Enter hours worked on day #{0}: ".format(i + 1))
        hrs = int(hrs)
        hrsDay.append(hrs)
    return hrsDay, days

#Danny helped me with this. I couldn't figure out how to error-check user input, 
# so he helped me create this function.

#Checks that user input is an integer, prints invalid input in the userInput()
#function otherwise.
def validNumber(n):
    try:
        num = int(n)
        if 0 <= num and num <= 24:
            return True
        else:
            return False
    except:
        return False
    
#Calculates the hours input by the user. Didn't really struggle with this, except working
#around it to error check.
def calcHours(hrsDay, days):
    mostHrs = max(hrsDay)
    totalHrs = sum(hrsDay)
    dayIndex = hrsDay.index(mostHrs)
    day = days[dayIndex]
    averageHrs = totalHrs / len(hrsDay)
    mostHrsDays = []
    for i in range(len(hrsDay)):
        if hrsDay[i] == mostHrs:
            mostHrsDays.append(days[i])
    print("------------------------------------------------------------------------------")
    print(f"The most hours you worked was on: ")
    for day in mostHrsDays:
        print(f"Day #{day} when you worked {mostHrs} hours.")
    print("------------------------------------------------------------------------------")
    print(f"The total number of hours you worked was: {totalHrs}")
    print(f"The average number of hours worked each day was: {averageHrs:.1f} ")
    print("------------------------------------------------------------------------------")

#Calculates and outputs the days the user worked less than 7 hours.
def slackedOff(hrsDay, days):
    slackingNum = 7
    print("Days you slacked off (i.e. worked less than 7 hours): ")
    for i in range(len(hrsDay)):
        slackHrs = hrsDay[i]
        if slackHrs < slackingNum:
            day = days[i]
            print(f"Day #{day}: {slackHrs} hours")

#I call a majority of my functions here and make sure all proper arguments are given.
def main():
    hrsDay, days = hoursInput()
    calcHours(hrsDay, days) 
    slackedOff(hrsDay, days)  
    # YOUR CODE ENDS HERE

main()