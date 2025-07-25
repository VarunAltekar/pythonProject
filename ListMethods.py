# sort
listSort = [6,2,8,3,9,4,1,5]
listSort.sort()
print(listSort)
listSort.sort(reverse=True)
print(listSort)

# reverse
listReverse = [6,2,7,3,8,4,9,5]
listReverse.reverse()
print(listReverse)

# index
listIndex = ["green", "yellow", "red", "violet", "green"]
print(listIndex.index("violet"))

# count
print(listIndex.count("green"))

# copy
listCopy = listIndex.copy()
print(listCopy)

# append
listIndex.append("yellow")
print(listIndex)

# insert
listIndex.insert(2, "marron")
print(listIndex)

# extend
listExtend = ["white", "black"]
listIndex.extend(listExtend)
print(listIndex)
