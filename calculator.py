
print("""
      
      ++++++++++++++++++++++++++++
      WELCOME TO ROLAND CALCULATOR
      ++++++++++++++++++++++++++++
      
      """)

number_one =int(input("enter your first number: "))
number_two =int(input("enter your second number: "))

sum = number_one + number_two
sub = number_one - number_two
mult = number_one * number_two
div = number_one / number_two
power = number_one ** number_two


print(f"the sum of {number_one} + {number_two} = {sum}")
print(f"the substraction of {number_one} - {number_two} = {sub}")
print(f"the multiplication of {number_one} * {number_two} = {mult}")
print(f"the division of {number_one} / {number_two} = {div}")
print(f"the power of {number_one} ** {number_two} = {power}")
