from inspect import modulesbyfile

# with content manager closes the file automatically
with open('files/fruits.txt') as myfile:
    content = myfile.read()

print(content)