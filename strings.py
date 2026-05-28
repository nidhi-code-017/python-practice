#strings

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



