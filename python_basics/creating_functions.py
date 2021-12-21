def  mean(mylist):
    the_mean = sum(mylist) /  len(mylist)
    return the_mean

print(mean([1,4,5]))

def  meanListDict(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    
    return the_mean

monday_temperatures = [8.8, 9.1, 9.8]
student_grades = {'marry':9.1,'sim':8.8,'john':7.5}
print(meanListDict(student_grades))
print(meanListDict(monday_temperatures))
