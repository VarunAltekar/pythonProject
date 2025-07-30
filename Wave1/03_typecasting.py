'''
Python’s built-in type conversion functions
int(), float(), hex(), oct(), str(), etc .
'''

str1 = "1"
str2 = "2"

print("wrong op : ", str1 + str2)
print("right op with explicit type casting", int(str1) + int(str2))

'''
Implicit type casting:
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python.
 Some of the data types have higher-order, and some have lower order.
  While performing any operations on variables with different data types in Python, 
  one of the variable's data types will be changed to the higher data type. 
  According to the level, one data type is converted into other by the Python interpreter itself (automatically).
   This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.
'''

num1 = 4        # converts num1 to int
num2 = 4.2      # convert num2 to float
res = num1+num2 # convert res to float as it is float addition

print("implicit typecasting to avoid data loss : ", res)


