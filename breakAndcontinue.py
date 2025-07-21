for i in range(1,100,1):
    print(i, end=" ")
    if(i==10):
        print("i is : ", i)
        break
    else:
        print("Missi")

print("Over")

for i in [2,3,4,5,6,7,8,9,0]:
    if(i%2!=0):
        continue
    print(i)