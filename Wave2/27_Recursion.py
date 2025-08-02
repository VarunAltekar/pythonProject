def fact(n):
    '''
    Returns factorial of n
    :param n:
    :return:
    '''
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

number = 4
print(f"factorial of {number} is {fact(number)}")