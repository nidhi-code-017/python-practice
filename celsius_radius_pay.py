#program 1

celsius =input("Enter the required temperature in Celsius:")
fahrenheit = (float(celsius) * 9/5) + 32
print(f"The temperature in Fahrenheit is:{fahrenheit}°F")
print(f"{celsius}°C = {fahrenheit}°F")

#program 2

radius = float(input("Enter the radius of a circle:"))
pi = 3.14159
area = pi * (radius ** 2)
circumference = 2 * pi * radius
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")

#program 3

hours = float(input("Enter the number of hours worked:"))
rate = float(input("Enter the hourly wage:"))
if hours > 8:
    overtime = hours - 8
    extra_pay = overtime * (rate * 1.5)
    total_pay = (8 * rate) + extra_pay
else:
    total_pay = hours * rate
print(f"The total pay is: {total_pay}")