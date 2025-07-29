print("Python is dynamically typed, OO language used for scripting")

#Variables & Data types in python
#Numeric datatype
a = 5
print(a)
print(type(5))
b = 55.8
print(b)
c = complex(4,3)
print(c)
#Textual datatype
d = "Varun"
print(d)
# None datatype
e = None
print(e)
#Boolean
f = True #False
print(f)

# ordered collection - mutable
list = [1,2.8,[2,5.6],["apple", "banana"]]
print(list)

# ordered collection - immutable
tupple = (1,3,4,("carrot", "beetroot"))
print(tupple)

# un ordered collection - mutable - k:v pair
dict = {"name": "Varun", "age":20, "canVote":True}
print(dict)

#Type Casting - conversion betweeen data types
g = "5"
print("first convert String to int")
print(int(g) + 1)

nahi = "Wrong"
print(int(nahi)) # invalid literal for int() with base 10: 'Wrong'
