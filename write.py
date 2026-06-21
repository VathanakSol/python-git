# create file or write file

# w : write 
# a : append 

# with open("global.txt","a") as f:
#     f.write("updated patch data!!!")

# try:
#     with open("fighter.txt", "x") as file:
#         file.write("This is fighter fighting\n")
#         file.write("Second fighter\n")
#         file.write("Third fighter\n")
# except Exception as error:
#     print(f"Error {error}")

import os

if os.path.exists("abc.txt"):
    print("File Exists")
else:
    print("File Not Found")
