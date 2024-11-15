#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #: W0516070     
#Student Name: Valentine Byrnes 


# YOUR CODE STARTS HERE, each line must be indented (one tab)
def hoursInput():
    hrsDay = []
    days = [1, 2, 3, 4, 5]
    for i in range(len(days)):
        hrs = int(input(f"Enter hours worked on day #{days[i]}: "))
        hrsDay.append(hrs)
    return hrsDay, days

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

def slackedOff(hrsDay, days):
    print("Days you slacked off (i.e. worked less than 7 hours): ")
    for i in range(len(hrsDay)):
        slackHrs = hrsDay[i]
        if slackHrs < 7:
            day = days[i]
            print(f"Day #{day}: {slackHrs} hours")
     
def main():
    hrsDay, days = hoursInput()
    calcHours(hrsDay, days) 
    slackedOff(hrsDay, days)  
    # YOUR CODE ENDS HERE

main()
