l1 = ["42", "11", "33", "97", "63", "86", "4", "46", "72", "88", "59", "55", "13" ]
l2 = ["24", "98", "56", "59", "3", "42", "14", "37", "75", "5", "34", "63", "4" ]

common_elements = []
common_dividable = []

for x in l1:
    for y in l2:
        if x == y:
            common_elements.append(x)
            if int(x) % 7 == 0:
                common_dividable.append(x)

print('Common elements:')
print(common_elements)
print('Common elements and dividable by 7:')
print(common_dividable)