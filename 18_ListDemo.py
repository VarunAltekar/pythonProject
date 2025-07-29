# 1. define python list
list = [2,4,6,"Harry", True, 23, 65, False, "Varun", 2.3]
print(list)
print(type(list))

# 2. index based access
print(list[0])
print(list[1])
print(list[2])

# 3. negative index access
print(list[-2])
print(list[len(list)-2])
print(list[5-2])
print(list[3])

# 4. check if item is present using in keyword
if True in list:
    print("present")
else:
    print("not present")

# listName[startIndex : endIndex : jumpIndex] / jumpIndex is optional / just like string slicing
# 5. list slicing
print(list[2:6])
print(list[-7:-3])
print(list[:6])
print(list[-3:])
print(len(list))
print(list[::2])