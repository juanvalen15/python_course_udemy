monday_temperatures = [9.1, 8.8, 7.5]

# append
monday_temperatures.append(8.1)
print(monday_temperatures)

# clear
monday_temperatures.clear()
print(monday_temperatures)

# index
monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures.index(8.8))
print(monday_temperatures.index(8.8,1,2)) # limiting the index search from element 1 to element 2 of the list. Skipping element 0

# __getitem__
print(monday_temperatures.__getitem__(1))
print(monday_temperatures[1])

