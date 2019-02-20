import csv

## !!! This code is not written as proper python code (imports, functions then scripts) for "learning purposes"
## The code itself is not that long, it is just full of comments

csv_data = []
# We import the csv file using a with statement, otherwise, we need to 
# open and close the file ourselves and it can be tricky
with open('Popular_Baby_Names_NY.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("The first line contains the column headers:")
            print(row)
            line_count += 1
        else:
            csv_data.append(row)
            line_count += 1
    print('Processed %s lines.' %(line_count)) #Can also use len(csv_data)

# At this point, csv_data contains the complete data from the file 
# organized as 
# [
# [row_1],
# [row_2],
# ...
# [row_n]
# ]

# Tasks:
# The **most popular female name** for **each year**
# The **most popular hispanic name for males between 2011-2016** 
# The **most popular female name for any ethnicity between 2012-2015**
# We can easily see that most tasks require the ability to filter our data by year
# Let's write a function to do so

# The function takes a start and end year and returns data filtered between those two years
def years_interval(csv_data, start_year, end_year):
    filtered_data = []
    print("This function will filter the data and only return data between %s and %s" %(start_year, end_year))
    # We go through our year (range does not go up to the last one, so we need to add one)
    for year in range(start_year, end_year+1):
        for row in csv_data:
            # data from the dataset is pulled by python as strings
            if row[0] == str(year):
                filtered_data.append(row)
    return filtered_data

# Let's start working on the first task, this is our plan:
# We need to find the most popular female name for each year from the whole dataset
# Our main issue is that we cannot use the rank column as it is only for each ethnicity for each year
# So we need to find all the occurrences of each name and sum the count column for each name for each year, regardless of ethnicity
# We are going to go through the dataset and create a list of all female names mentionned
# We are also going to create a list containing all years mentionned in this dataset
female_names = []
years = []
# We go through the data again
for row in csv_data:
    # we create a list containing all the years (the first [0] column)
    years.append(row[0])
    # we check if this row is for a female or not
    if row[1].lower() == "female":
        # if it is a female, we add the name to a list (huge list)
        # this list contains duplicates since a name might appear for several years
        female_names.append(row[3].lower())
# We transform our lists into sets which removes all duplicates and keeps only unique elements
# This way we have all the female names mentionned in the list only once
female_names_set = set(female_names)
# we do the same for years
years_set = set(years)
# Let's also sort the years to have them ordered from lower to higher (not necessary)
years_set = sorted(years_set)

print("")
print("Most popular female name and count for each year:")
# Regarding the first task, our main issue is that names are ranked by ethnicity first, then by year 
# so we cannot use the ranking provided as we want the most popular by year regardless of ethnicity
# In this dictionary, we are going to store years
# {2011: <2011 female dataset>; 2012: <2012 female dataset>; ...}
total_female_count_by_year = {}
# Since we want the most popular name by year, let's first go through our years, one by one
for year in years_set:
    # Now we go through the unique female names and create a dictionary where:
    # key = unique_female_name ; value = sum of counts from all ethnicities for that year
    # let's create our empty dictionary
    yearly_female_count= {}
    # now we go through the list containing all the unique female names
    for female_name in female_names_set:
        # we create an object in the dictionary for which the key is the current unique female name and initialize the count at 0
        yearly_female_count[female_name] = 0
        # we now go through the rows of the dataset again
        for row in csv_data:
            # we check for each row if the year is the same as the current year in our first for loop
            if int(row[0]) == int(year):
                # We only look at female names
                if str(row[1]).lower() == "female":
                    # we check for each row if the current female name is the same as the name mentionned in the current row
                    # we might meet each unique female name several times because there will be a different count for each ethnicity
                    if str(female_name).lower() == str(row[3]).lower():
                        # if they are the same, we add the count from the row of the current female unique name to the dictionary
                        # object which key is the current female name (we keep count for each unique female name in our dictionary basically)
                        yearly_female_count[female_name] = yearly_female_count[female_name] + int(row[4])
    # At the end of each year for loop we add to {total_female_count_by_year} the dictionary for the year
    total_female_count_by_year[year] = yearly_female_count
    # we retrieve the dictionary key (unique_female_name) with the highest value (highest total count for the year) fron the yearly dataset
    # the max function can take a list or a dictionary, if it is a dictionary, we need to specify that we need to retrieve the key associated with the highest value
    max_count_female_name = max(yearly_female_count, key=yearly_female_count.get)
    # We print the year and name with highest count and the count for each year (at the end of each year loop)
    print(year, max_count_female_name, yearly_female_count[max_count_female_name])
    # What we got here is the most popular names for all years, we actually need to get it for each year
    print("Does anyone know why Olivia is so popular ?")

