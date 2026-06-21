import json 

# Read JSON File
with open("users.json", "r") as file:
    content = json.load(file)

print(content[1]['email'])

# Create/Write JSON File

data = {
    "name": "Vichea",
    "age": 26,
    "email": "vichea@gmail.com"  
}

with open("customer.json", "a") as file:
    json.dump(data, file, indent=4)

print("File Create successfully!!")