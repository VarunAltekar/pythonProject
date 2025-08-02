# place python variables inside string - py 3.6
# it solves problems related to string formatting

# 1. the problem
letter = "Hey my name is {} and i am from {}"
country = "India"
name = "Varun"

print( letter.format(name, country) )
print(letter.format(country,name))
# here we need to remember the arg order

letterOrder = "Hey my name is {0} and i am from {1}"
print(letterOrder.format(name,country))
print(letterOrder.format(country,name))

# 2. the solution
print(f"Hey my name is {name} and i am from {country}")

# 2 decimals for floating values
price = "Price only {price:.2f} dollars"
print(price.format(price = 99.999))

print(f"{2*3}")
print(type(f"{2*3}"))

print(f"So we use f string like this {{demo}} and i am from {{country}}")
