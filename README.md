# Get started:

1. [Starting python](001-installing-python3.md)
2. [Using python from the shell](002-using-pythonshell.md)
3. [Strings and integers](003-strings-and-integers.md) 

[Keep learning](learn_more.md)


### Exras:
* [Editors Four spaces VS tabs](001b-space-tabs.md)


> Exercises suggested from exercises suggested by Dr. Kristian Rother (krother@academis.eu) and Michele Pratusevich (mprat@alum.mit.edu)from datetime import date

def monday_check(specimen_date):
    if specimen_date.weekday() == 0:
        message = "Monday again ... Go away Monday!"
    else:
        message = "Today is not a Monday!"
    return message

print("This program will tell you if it is already the worst day of the week.")
today = date.today()
print( monday_check(today) )