# convert tuple to list / modify list / convert back to tuple
tup = ("india", "sri lanka", "finland", "norway", "denmark", "usa")
print(tup)

list = list(tup)

list.append("afghan")   # add item
list.pop(2)             # remove item
list[1] = "Bhutan"      # change item

tup = tuple(list)
print(tup)

# append tupple to create new tuple
tup1 = ("france", "poland", "spain")
tup2 = ("germany", "uk")

tup3 = tup1 + tup2
print(tup3)