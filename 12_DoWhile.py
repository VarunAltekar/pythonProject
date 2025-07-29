# execute atleast once
# exit controlled loop

while True:
    number = int(input("Enter positive number:"))
    print(number)
    if not number > 0:
        break


