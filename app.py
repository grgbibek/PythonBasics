import math

course = "  Python Programming "
print(len(course))  # Output: 20
print(course[0])  # Output: P
print(course[-1])  # Output: g
print(course[0:3])  # Output: Pyt

print(course[0:])
print(course[:3])  # Output: Pyt
print(course[:])  # Output: Python Programming

# formatted string

first = "Bibek"
last = "Gurung"
full = f"{len(first)} {last}"
print(full)  # Output: Bibek Gurung


print(course.upper())  # Output: PYTHON PROGRAMMING
print("Strip : " + course.strip())  # Output: Python Programming
print(course.find("Pro"))  # Output: 10

# numbers
print(10 / 3)  # Output: 3.3333333333333335
print(10 // 3)  # Output: 3
print(10 % 3)  # Output: 1
print(10 ** 3)  # Output: 1000

print(round(2.9))  # Output: 3
print(abs(-2.9))  # Output: 2.9
print(math.ceil(2.2))  # Output: 3

# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")  # Output: x: <input_value>, y: <input_value + 1>

# Falsy values
print(bool(""))  # Output: False
print(bool(0))  # Output: False
print(bool(None))  # Output: False
print(bool([]))  # Output: False
print(bool({}))  # Output: False

# conditional
temperature = 15
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif (temperature > 20):
    print("It's a nice day")
else:
    print("It's a cold day")
print("Done")

# Ternary operator
age = 12
message = "Eligible" if age >= 18 else "Not eligible"
print(message)  # Output: Not eligible

# Operators
high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible for loan")  # Output: Eligible for loan
else:
    print("Not eligible for loan")

# Loops
for number in range(5):
    print("Attempt", number + 1, (number + 1) * ".")  # Output: 0 1 2 3 4

for number in range(1, 4):
    print("Attempt", number, (number) * ".")  # Output: 0 1 2 3 4
