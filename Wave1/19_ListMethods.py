# 1. sort
listSort = [6,2,8,3,9,4,1,5]
listSort.sort()
print(listSort)
listSort.sort(reverse=True)
print(listSort)

# 2. reverse
listReverse = [6,2,7,3,8,4,9,5]
listReverse.reverse()
print(listReverse)

# 3. index - index of first occurrence
listIndex = ["green", "yellow", "red", "violet", "green"]
print(listIndex.index("violet"))

# 4. count - no of times given parameter exist in list
print(listIndex.count("green"))

# copy - list copy
listCopy = listIndex.copy()
print(listCopy)

# append - add to end of list
listIndex.append("yellow")
print(listIndex)

# insert - add to specific index
listIndex.insert(2, "marron")
print(listIndex)

# extend - add list to end of list
listExtend = ["white", "black"]
listIndex.extend(listExtend)
print(listIndex)
