from inspect import modulesbyfile

# with content manager closes the file automatically

# # to read
# with open('files/fruits.txt') as myfile:
#     content = myfile.read()

# to write
with open('files/fruits.txt', "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion")
