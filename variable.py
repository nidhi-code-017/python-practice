college_name = "AU"
year = 2026
goal = "Get an internship by 2027"
print(college_name)
print(year)
print(goal)

#datatype

a ="100"
b = 50
print (type(a))
print (type(b))
print(a + a)
print(b+b)

#input

name = input ("Enter your name: ")
birth_year = input ("Enter your birth year: ")
age = str(2026 - int(birth_year))
print(name + " is " + age + " years old ")

x = input("Enter a number: ")
print(x + x)

# strings 

name = input ("Enter your name: ")
birth_year = input ("Enter your birth year: ")
age = 2026 - int(birth_year)
print(f"{name} is {age} years old")

#day 3 end program

product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
total_price = product_price * quantity
print(f"The total price for {quantity} {product_name}(s) is: {total_price}")

product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
total_price = product_price * quantity
print(f"{quantity} x {product_name} =  ₹{total_price}")

