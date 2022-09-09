#file = open('test.txt')  # pass path of the file over here
#print(file.read())
#print(file.read(7))  # read n number of characters by passing parameter

#print(file.readline())
# print(file.readline())  # remember to comment the read part above otherwise control will start from last read location


# ----------- print line by line using readline method ----  #

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# --------------------- readlines method ----------------------------------- #

#values = ['apple\n', 'ball\n', 'cat\n', 'dog\n', 'egg\n', 'fan\n', 'gravity']
for line in file.readlines():
    print(line)

file.close()  # Remember whenever you open any file always write close method too otherwise memory leaks could happen
