var_name = input("Enter pattern")
match var_name:
    # 1. Normal
    case "pattern1":
        print("Hey")
    case "pattern2":
        print("You")
    # 2. Empty case with if-condition
    case _ if (var_name != "pattern101"):
        print("Hey again")
    # 4. Default case
    case _:
        print("def case")

num = int(input("Enter num"))
print(type(num))
match num:
    case 2:
        print("num is 2")
    # 3. case with if-condition
    case 4 if num%2==0:
        print("num is even")
