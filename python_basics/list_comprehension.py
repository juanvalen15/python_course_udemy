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