var_name = input("Enter pattern")
match var_name:
    case "pattern1":
        print("Hey")
    case "pattern2":
        print("You")
    # Empty case with if-condition
    case _ if (var_name != "pattern101"):
        print("Hey again")
    case _:
        print("def case")

num = int(input("Enter num"))
print(type(num))
match num:
    case 2:
        print("num is 2")
    # case with if-condition
    case 4 if num%2==0:
        print("num is even")
