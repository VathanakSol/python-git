# File Python - File Input/Output (I/O)

# Open File 
# Operation ...
# Close File

# open("name file", "mode")
 
# opening a file

# open
content = open("example.txt","r")
# operation 
print(content.read())
# close
content.close()

# opening file has with statement (auto close file)
with open("example.txt", "r") as file:
    print(file.read())
print("Reading File Successfully!!!")