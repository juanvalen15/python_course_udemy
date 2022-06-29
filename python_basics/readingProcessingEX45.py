# function 
# gets a single string character and a filepath as parameters
# returns the number of occurences of the character in the file

def ex45(inputString, filepath):
    with open(filepath, "r") as myfile:
        data = myfile.read()        
    numberStr = data.count(inputString)
    return numberStr

stringTest = 'is'
pathTest = 'files/bear.txt'
n = ex45(stringTest, pathTest)
print('number of occurrences of '+stringTest+' is: ', n)