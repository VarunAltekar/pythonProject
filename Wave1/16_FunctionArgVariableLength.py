# 2 ways to achieve var len arg
# 1. arbitrary arg ( index based )
def name(*name):
    print("Hello", name[0], name[1], name[2])

name("James", "Buchananes", "Barnes")

# 2. keyword arbitrary arg ( k-v pair based )
def name2(**name):
    print("Hello",name["lname"],name["fname"],name["mname"])

name2(lname="Altekar", mname="D", fname="Varun")


