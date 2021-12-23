# Program requirements:
# 1. get user input text
# 2. when user input is '\end' program should terminate
# 3. user inputs are append together. first sentence ends with dot. following sentence ends with question mark. [. ? . ? .. etc]


from typing import final


def print_text(array):
    final_text = ''
    for text in array:
        index = array.index(text)
        print('Index: %s' % index)

        if (index % 2) == 0:
            temp_text = text + '.'
            print('Final text even index: %s' % temp_text)
        else:
            temp_text = text + '?'
            print('Final text odd index: %s' % temp_text)

        final_text = final_text + ' ' + temp_text
    
    print('Final text after foor loop: %s' % final_text)
    return final_text


input_array = []

while True:
    user_input = input('Say something: ')

    if user_input == '\end':
        print("The input array when \end is entered: ")
        print(input_array)
        print("The final text is: %s" % print_text(input_array))
        break
    else:
        input_array.append(user_input) # store input in an array
        print(input_array)
        continue