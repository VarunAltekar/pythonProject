# 1. tuple declaration n definition
tup = (1,3,5)
print(type(tup), tup)

tup1 = (1)
print(type(tup1), tup1, "How???")

tup2 = (1,)
print(type(tup2), tup2, "Okk")

tup3 = (1,4,3,"green")
print(type(tup3), tup3)

# 2. tuple index based access
print(tup3[0])
print(tup3[3])

# 3. tuple negative index based access
print(tup3[-1])
print(tup3[-4])

# 4. check for tuple value
if "green" in tup3:
    print("Yes")

# 5. tuple slicing
tupNewSlice = tup3[1:3]
print(tupNewSlice)

tupRangeIndex = (1,2,3,4,5,6,7,8,9,"green",True,False)

print(tupRangeIndex[2:7])
print(tupRangeIndex[-5:-1])

print(tupRangeIndex[:8])
print(tupRangeIndex[:-4])

print(tupRangeIndex[5:])
print(tupRangeIndex[-6:])

print(tupRangeIndex[:len(tupRangeIndex): 2])