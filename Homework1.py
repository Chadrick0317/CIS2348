#Chad Johnson 1323504 Homework Assignment 1

from datetime import date

def calculateAge(currentDate, birthDate):
    today = currentDate
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

print("Chad's Birthday Calculator")
print("What's Today's Date?")

month = int(input('Month: '))
day = int(input('Day: '))
year = int(input('Year: '))
print('When is your Birthday?')

birthdaymonth = int(input('Month: '))
birthdayday = int(input('Day: '))
birthdayyear = int(input('Year: '))
print("you are ", calculateAge(date(year, month, day), date(birthdayyear, birthdaymonth, birthdayday)), "years old.")

if day == birthdayday:
    print("Happy Birthday!")
