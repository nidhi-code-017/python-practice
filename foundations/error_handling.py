def calculate(num1, num2, operation):   
     if operation == "+":
           return num1 + num2
     elif operation == "-":
           return num1 - num2
     elif operation == "*":
          return num1 * num2
     elif operation == "/":
              if num2 == 0:
                return "Error: Cannot divide by zero."
              else:
                return num1 / num2
     else:
           return "Invalid operation"  
while True:
     num1 = input("Enter a number: ")
     if num1 == "quit":
         break
     try:
         num1 = float(num1)
         num2 = float(input("Enter another number: "))
     except ValueError:
         print("That's not a valid number.")
         continue
     operation = input("Enter the operation (+, -, *, /): ") 
     result = calculate(num1, num2, operation)
     print("The result is:", result)