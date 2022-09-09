# Tuple - same as a LIST Data type but immutable means we cannot update it

val = (1, 2, 2, "Girish", 4.5)

print(val[1])
# val[2] = 5 --> not allowing to update the data in the tuple.

print(val[2])
print(val)


#  Dictionary

dic = {"a": 2, 4: "bcd", "c": "Hello world"}

print(dic[4])
print(dic["c"])

# ----------------------------- Example 2 -------------------------------------#

# a sample dictionary variable

a = {1: "first name", 2: "last name", "age": 33}

# print value having key=1
print(a[1])
# print value having key=2
print(a[2])
# print value having key="age"
print(a["age"])

# -- Creating dictionaries at run time and adding data to it ---#

dct = {}
dct["firstname"] = "Girish"
dct["lastname"] = "Deshmukh"
dct["gender"] = "Male"
print(dct)
