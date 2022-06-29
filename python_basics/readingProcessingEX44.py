with open('files/bear.txt', "r") as myfile:
    content = myfile.read()

print(content[0:90])