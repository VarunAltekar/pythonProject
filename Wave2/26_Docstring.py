# helps in describing python function, unlike comments
# string literals, that appears right after functin definition

def sqrprint(number):
    '''
    Prints square of number
    :param number:
    :return:
    '''

    print(f"square of {number} is : {number**2}")

sqrprint(3)
# python stores docstring inside __doc__ variable
print(sqrprint.__doc__)


'''
    Python Comments vs Docstrings
Python Comments
Comments are descriptions that help programmers better understand the intent and functionality of the program.
 They are completely ignored by the Python interpreter.

Python docstrings
As mentioned above, Python docstrings are strings used right after the definition of a function,
method, class, or module (like in Example 1). They are used to document our code.

We can access these docstrings using the doc attribute.
'''
