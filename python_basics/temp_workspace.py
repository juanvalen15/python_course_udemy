# temporal workspace: file to write down temporal programs for quizes and exercises 

def multParams(strA, strB):
    return (strA + strB)


print(multParams('a','b'))


def mean(*args):
    return sum(args)/len(args)


print(mean(1,2,3))



def E(*args):
    return sum(args)/len(args)


print(E(1,2,3))


def numStrings(*args):
    # convert to capital
    new_temps = []
    for temp in args:
        new_temps.append(str.upper(temp))
    # sort
    return sorted(new_temps)


print(numStrings('aaa','ddd','ccc'))


# multiple keyword arguments
def meankw(**kwargs):
    return kwargs

print(meankw(a=1,b=2,c=3))