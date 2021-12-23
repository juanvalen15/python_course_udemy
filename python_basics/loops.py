monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))


student_grades = {"marry": 9.1, "sim": 8.8, "john": 7.5}

for grades in student_grades.items():
    print(grades)

for grades in student_grades.keys():
    print(grades)    

for grades in student_grades.values():
    print(grades)    


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    number_no_plus = str.removeprefix(value,"+")
    number_with_zeros = "00"+number_no_plus
    print(number_with_zeros)