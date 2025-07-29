# length of string
str1 = "Mango"
leng = len(str1)
print("Mango is",leng,"letter word")

'''
This method of specifying the start and end index to specify a part of a string 
    is called slicing.
'''
pie = "ApplePie"

print("ApplePie is of length is ",len(pie))
print("Slicing pie from start till index 5 (excluding 5) :",pie[:5]) #Slicing from start
print("Slicing pie till end :",pie[5:]) #Slicing till end
print("Slicing in between start index 2 exclude index 6 :", pie[2:6]) #Slicing in between - index 2 start : exclude index 6
print(pie[:-3])
print(pie[-3:len(pie)-1])

# negative index representation
#   V   a   r   u   n
#   -5  -4  -3  -2  -1
nm = "Varun"
print(nm[-4:-2])