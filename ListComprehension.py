# List Comprehension - create new list from other iterables
list = [2,3,4,5,6,7]

listSub = [i for i in list[2:5] if i%2==0]

print(listSub)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
names_o = [i for i in names if "o" in i]
print(names_o)

names_len = [i for i in names if len(i) > 4]
print(names_len)