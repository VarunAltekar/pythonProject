# 1. default function arg
def printNames(fname, mname="Jack", lname="Trump"):
    print("Hello",fname,mname,lname)

# if we dont provide value, function assumes default value for that arg
printNames("Amy")
printNames("Amy", "John")
printNames("Gary","Kill","Bill")

# 2. keyword arg - key=value : the order in which arg is passed does not matter
printNames(lname="Jackson", fname="Amy")
#printNames(lname="Jackson", "Amy") - This will not work as we have to mention key

# 3. required function args
def printNamesRequired(fname, mname, lname):
    print("Hello",fname,mname,lname)

printNamesRequired(lname="Gandhi", fname="Mohandas", mname="Karamchand")
#printNamesRequired("Pandit","Nehru") - printNamesRequired() missing 1 required positional argument: 'lname'



