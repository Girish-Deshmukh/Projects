greeting = "Good Morning"
a = 4
if a > 2:
    print("Condition matches")
    print("second line")
else:
    print("condition do not match")
print("if else condition code is completed")  # Python takes spaces in consideration since it do not have curly braces

# --------------- For Loop in Python -------------------------#

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

# ------------------- Sum of 5 natural numbers -----------------#
summation = 0
for j in range(1, 6):  # range(i,j) --> i to j-1
    # in java for this we use for(i=0;i<5;i++)
    summation = summation + j
    print(summation)

print(summation)

# -------------------- One more test for jumping 2 values for each iteration  ----------------#

print("*************************************************")
for k in range(1, 10, 2):
    print(k)
print("******************** Skipping first index *****************************")
for k in range(10):
    print(k)



