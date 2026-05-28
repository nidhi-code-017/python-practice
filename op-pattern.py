#operators

number = int(input("Enter a number :"))
if number == 0:
    print("The number is zero")
elif number > 0:
    print("The number is positive")
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else: 
    print("The number is negative")

# loops
# Normal pattern
print("Normal Pattern")

for i in range(1, 6):
    print("*" * i)

# Inverted pattern
print("\nInverted Pattern")

for i in range(5, 0, -1):
    print("*" * i)

# Number triangle pattern
print("\nNumber Triangle Pattern")
for i in range(5):
    for j in range(0, i+1):
        print(j+1, end="")
    print()  # Move to the next line after inner loop

# diamond pattern
print("\nDiamond Pattern")
# Upper Pyramid
for i in range(3):
    print(" " * (2- i) + "*" * (2 * i + 1))

# Lower Pyramid
for i in range(1, -1, -1):
    print(" " * (2- i) + "*" * (2 * i + 1))

# Number triangle pattern with spaces

print("\nNumber Triangle Pattern")
for i in range(5):
    print(" " * (4- i), end="")
    for j in range(i + 1):
        print(j + 1, end="")
    print()
