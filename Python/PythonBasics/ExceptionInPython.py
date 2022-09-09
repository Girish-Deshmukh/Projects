# ItemsInCart = 0
# 2 items will be added to cart

# if ItemsInCart != 2:
# raise Exception("Product Cart Count not matching")
#     pass
#
# assert (ItemsInCart == 2)

# these are two examples of ways to handle exception in Python

print("**************************************************************************")

# try , catch
try:
    with open('test.txt', 'r') as reader:
        reader.read()
except:
    print("control reached to this block since there is failure in try block")
finally:
    print("this will get executed even if test fails or passes")

print("**************************************************************************")

# try , catch
# try:
#     with open('fileLog.txt', 'r') as reader:
#         reader.read()
# except Exception as e:
#     # print("control reached to this block since there is failure in try block")
#     print(e)  # here test will not fail but on console we will get the pyton error and not the except file which we
#     # wrote
# finally:
#     print("Cleaning up resources")

print("**************************************************************************")
