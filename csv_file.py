# CSV = Comma-Seperated Value

import csv

# Read CSV File
with open("students.csv","r") as file: 
    content = csv.reader(file)
    for row in content:
        print(row)

# Create CSV File

data = [
    ["name","gender","university"],
    ["kongea","male","RUPP"],
    ["vichet","male","RULE"],
    ["neary","female","ITC"]
]

with open("classes.csv","w", newline="") as file:
    content = csv.writer(file)
    content.writerows(data)