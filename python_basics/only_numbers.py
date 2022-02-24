def only_numbers(input_list):
    integers_list = [list_entry for list_entry in input_list if type(list_entry) == int]
    return integers_list

print(only_numbers([99, 'no data', 95, 93, 'no data']))


def only_numbers_greater_zero(input_list):
    integers_list = [list_entry for list_entry in input_list if list_entry > 0]
    return integers_list

print(only_numbers_greater_zero([99, -95, 93, 0.4]))    


def zeros_instead(input_list):
    list_with_zeros = [list_entry if type(list_entry) == int else 0 for list_entry in input_list]
    return list_with_zeros

print(zeros_instead([99, 'no data', 95, 93, 'no data']))