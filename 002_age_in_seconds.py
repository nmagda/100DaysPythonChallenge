import datetime
from datetime import date

while True:
    birth_day = input("Which day were you born on ?")
    if birth_day.isdigit() and int(birth_day) in range(1, 32):
        break
    else:
        print("Value is not correct, enter number from 1 to 31")

while True:
    birth_month = input("Which month were you born in ?")
    if birth_month.isdigit() and int(birth_month) in range(1, 13):
        break
    else:
        print("Value is not correct, enter number from 1 to 12")

while True:
    birth_year = input("Which year were you born in ?")
    if birth_year.isdigit() and int(birth_year) in range(1900, 2018):
        break
    else:
        print("Value is not correct, enter your year of birth")

birth_date = date(int(birth_year), int(birth_month), int(birth_day))
print("You were born on {}.".format(birth_date))

age_sec = (date.today() - birth_date).total_seconds()
print("You're ", int(age_sec), "seconds old.")