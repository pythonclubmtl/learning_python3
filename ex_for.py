purchases = [6.9, 7.2, 10.3, 4.5, 6.8, 7.4, 11.4, 3.8]

weekly_spendings = 0
for purchase in purchases:
    weekly_spendings = weekly_spendings + purchase
    # The fist time we got through this loop, weekly_spendings = 0
    # First loop, this operation is: 6.9 = 0 + purchases[0]
    # Second loop it is: 14.1 = 6.9 + purchases[1]
    # etc ...
    

print("This week, you spent:", weekly_spendings)