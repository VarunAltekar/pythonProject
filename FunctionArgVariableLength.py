# 2 ways to acheive var len arg
# arbitrary arg
def name(*name):
    print("Hello", name[0], name[1], name[2])

name("James", "Buchananes", "Barnes")

# keyword arbitrary arg
def name2(**name):
    print("Hello",name["lname"],name["fname"],name["mname"])

name2(lname="Altekar", mname="D", fname="Varun")


