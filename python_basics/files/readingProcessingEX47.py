# to read
with open('files/bear.txt', "r") as myfile:
    content = myfile.read()

with open('files/first.txt', "w") as myfile:
    myfile.write(content[:89])