# list comprehension
temps = [221, 234, 340, 212]

# long process
new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)


# using list comprehension
new_temps = [temp / 10 for temp in temps]
print(new_temps)

temps = [221, 234, 340, 212, -9999]
new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)

temps = [221, 234, 340, 212, -9999]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps] # with if/else order changes
print(new_temps)

def zeros_instead(input_list):
    list_with_zeros = [list_entry if type(list_entry) == int else 0 for list_entry in input_list]
    return list_with_zeros

print(zeros_instead([99, 'no data', 95, 93, 'no data']))


def convert_and_sum(input_list):
    float_list = [float(temp) for temp in input_list]
    print(float_list)
    sum_temp = 0.0
    for float_temp in float_list:
        sum_temp = sum_temp + float_temp
    
    return sum_temp

print(convert_and_sum(['1.2', '2.3', '1.1']))