from datetime import date

def monday_check(specimen_date):
    if specimen_date.weekday() == 0:
        message = "Monday again ... Go away Monday!"
    else:
        message = "Today is not a Monday!"
    return message

print("This program will tell you if it is already the worst day of the week.")
today = date.today()
print( monday_check(today) )