set1 = {1,2,5,6}
set2 = {3,6,7}
print("set1",set1,"set2", set2)
print("union",set1.union(set2))

#set1.update(set2)
#print( "updated set1 with values from set2",set1, set2 )

print("intersection",set1.intersection(set2))

#set1.intersection_update(set2)
#print(set1)

print("symmetric difference", set1.symmetric_difference(set2))

#set1.symmetric_difference_update(set2)
#print(set1)

print("difference", set1.difference(set2))