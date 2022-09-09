values = [1, 2, "Girish", 4, 5]
# List is the data type that allows multiple values and can be with different data types

print(values[0])  # output should be 1
print(values[2])  # GIRISH should be the output
print(values[-1])  # -1 will print the last value in your list so answer will be 5
print(values[1:3])  # it will print values from index 1 to index 2 basically -1 value
values.insert(3, "Deshmukh")  # [1, 2, 'Girish', 'Deshmukh', 4, 5]
print(values)
values.append("End")  # [1, 2, 'Girish', 'Deshmukh', 4, 5, 'End']
print(values)
values[2] = "GIRISH"  # Updating
del values[0]  # For Deleting the value
print(values)
