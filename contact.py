"""
    Exercise: Create System for saved user's contact
    - Get input from user
    - Save user's information in system as text file
    - Store and see user's data
"""

FILE_NAME = "users.txt" 
MODE = "x"

name = input("Enter name: ")
phone = input("Enter phone number: ")

with open(FILE_NAME, MODE) as file:
    file.write(f"Full name    : {name}\n")
    file.write(f"Phone number : {phone}\n")


print("File Successfully created!!!")