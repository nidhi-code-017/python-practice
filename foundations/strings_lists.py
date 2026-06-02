strings

sentence = input("Enter a sentence: ")
upper = sentence.upper()
print(f"uppercase: {upper}")
words = sentence.split()
length = len(words)
print(f"word count: {length}")
print(f"first character: {sentence[0]}")
print(f"last character: {sentence[-1]}")
sentence = sentence.replace(" ", "-")
print(f"hyphenated: {sentence}")

#lists

num  = []
for i in range(5):
    n = (int(input("Enter a number: ")))
    num.append(n)
    if i == 0:
        largest = n
        smallest = n
        total = n
    else:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
        total = total + n
avg = total / 5
num.sort()
print(f"largest: {largest}")
print(f"smallest: {smallest}")
print(f"sum: {total}")
print(f"average: {avg}")
print(f"sorted: {num}")

#reversed word by word

s = input("Enter a sentence: ")
words = s.split()
reversed_words = words[::-1]
reversed_sentence = " ".join(reversed_words)
print(f"reversed: {reversed_sentence}")

#word counter

s = input("Enter a sentence : ")
visited  = []
words = s.split()
for i in words :
    if i in visited :
        continue #if the word is already in the list, skip to the next iteration    
    visited.append(i)
    count = 0
    for j in words :
        if i == j :
            count = count + 1
    print(f"{i} : {count}")

#guessing game 

import random
number = random.randint(1, 20)
guess = int(input("Guess a number which is between 1 to 20 : "))
counter = 1
while guess != number :
    counter = counter + 1
    if guess < number : 
        print("Too Low")
    else :
        print("Too High")
    guess = int(input("Guess again : "))
print(f"Number of guesses : {counter}")
print("Congratulations! You guessed the number.")
