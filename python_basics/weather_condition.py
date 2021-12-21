def weather_condition(temperature):
    if temperature > 7:
        return "warm"
    else:
        return "cold"

user_input = float(input("Enter temperature in [C]: "))

print(type(user_input))

print(weather_condition(user_input))