# Program requirements:
# 1. phrase = get user input text
# 2. capitalize first letter of phrase
# 3. identify if phrase is question or sentence
# 4. when user input is '\end' program should display all phrases together
# 5. program terminates

def sentence_maker(phrase):
    interrogatives = ("is","are","how","what","where","when")
    capitalized = phrase.capitalize() # capitalize first letter
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


input_array = []
while True:
    user_input = input('Say something: ')

    if user_input == '\end':
        break
    else:
        input_array.append(sentence_maker(user_input)) # store input in an array
        continue

print(" ".join(input_array))