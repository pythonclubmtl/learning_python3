import csv

with open('../datasets/Popular_Baby_Names_NY.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # At this point, row is a list, each element of the list is one of the column header
            # Try playing around with the command "-".join(list), it concatenates elements of a
            # list as a string and puts "-" between each element
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line_count += 1
    print(f'Processed {line_count} lines.')