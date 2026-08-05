def calculate(num1, num2 , operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        if num2 == 0:
            return "cannot divide by zero"
        return num1 / num2
    elif operator == "*":
        return num1 * num2
    else :
        return "invalid operator"
    
print(calculate(10, 5, "+"))
print(calculate(10, 5, "-"))
print(calculate(10, 5, "*"))
print(calculate(10, 5, "/"))
print(calculate(10, 0, "/"))
print(calculate(10, 5, "^"))


# #program 2

def analyze_text(text):
    word_count = len(text.split())
    character_count = len(text.replace(" ", ""))
    reversed_text = text[::-1]
    return word_count, character_count, reversed_text
words, characters, reversed_text = analyze_text("Hello World")
print(words)
print(characters)
print(reversed_text)

#palindrome

def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome("racecar"))
print(is_palindrome("hello"))

# count no.of vowels
def count_vowels(text):
    text = text.lower()
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))
print(count_vowels("PYTHON PROGRAMMING"))