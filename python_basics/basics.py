day_hours = 24
week_days = 7

week_hours = week_days * day_hours
print(week_hours)

x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

student_grades = [9.1, 8.2, 7.5]
student_grades = {"marry": 9.1, "sim": 8.8, "john": 7.5}

new_list = list(range(1, 10 , 2))
print(new_list)

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum/length
print(mean)

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
student_grades.__contains__(10)
print(student_grades.count(10))


monday_temperatures = (1, 4, 5) # tuple declaration. tuples cannot be mutated e.g., with append
print(monday_temperatures)

monday_temperatures = [1, 4, 5] # list declaration. list can be mutated e.g., with append
print(monday_temperatures)
monday_temperatures.append(6)
print(monday_temperatures)
