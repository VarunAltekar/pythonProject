def name(*num):
    sum = 0;
    for i in num:
        sum = sum + i

    return sum / len(num)


print(name(2,3,4))