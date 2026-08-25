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

#Write a program that takes a list of numbers from the user (keep asking until they type "done"), then prints:
# The unique numbers (use a set)
# How many duplicates were removed
# The numbers as a tuple (sorted)

list_of_numbers = []
while True:
     num = input("Enter numbers : ")
     if num == "done":
        break
     try:
          num = int(num)
          list_of_numbers.append(num) # add the numbers in the list 
     except ValueError:
          print("That's not a valid number.")
          continue
unique_numbers = set(list_of_numbers)
duplicate_numbers = len(list_of_numbers) - len(unique_numbers)
sorted_tuple = tuple(sorted(unique_numbers))
print("Unique numbers:", unique_numbers)
print("Duplicates removed:", duplicate_numbers)
print("Sorted tuple:", sorted_tuple)