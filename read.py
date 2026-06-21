# read(), readlines(), readline()

# with open("number.txt", "r") as file:
#     # read entire file
#     content = file.read()

#     # read first line
#     content = file.readline()

#     # read line by line
#     content = file.readlines()

#     print(content)

import csv

with open("students.csv","r") as file:
    content = csv.reader(file)
    for row in content:
        print(row)

