# Basic Data Types

# String

print("Hello"[4])

# Integer

print(123 + 345)

# Float (with decimal numbers/floating point number)

3.14159

# Boolean

True
False

# num_char = len(input("What is your name? "))
# print("Your name has " + num_char + "characters.")

#  type checking using type()
# print(type(num_char))

print(type("Hello"))

# type casting converting other data types
# new_num_char = str(num_char)
# print("Your name contains " + new_num_char + " characters.")

a = float(123)
print(type(a))

# PEMDASLR
# () (Parenthesis)
# ** (Exponents)
# * / (Multiplication and Division)
# + - (Addition and Subtraction)

print(3 * (3 + 3) / 3 - 3)

# rounding numbers
print(8/3)

# rounding with 2 decimal points
print(round(8/3, 2))

# floor division (2 forward slashes) and output will be an int
print(8//2)

# F strings
# mix string and different data type
score = 0
height = 1.8
isWinning = True

print(f"your score {score}, your height is {height} and is winning {isWinning}")

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# current age - 90 * 365 days
# current age - 90 * 52 weeks
# current age - 90 * 12 months

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")