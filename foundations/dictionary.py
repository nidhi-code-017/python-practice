#count the no of times each word appears in a sentence

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# counts = {}
# for i in words:
#     if i in counts:    # which word am i currently trying to count ?
#         counts[i] += 1
#     else:
#         counts[i] = 1
# for word in counts:
#     print(f"{word} : {counts[word]}")


#student_grades

students = {"SND": 82, "Ravi": 45, "Priya": 93, "Arun": 38}
def student_grades(students):
    result = {}
    for student, score in students.items():        # "student" - dictionary , to look at each student's name and their score one by one. "student.items()" - to get the key-value pairs from the dictionary.
        if score >=90:
            grade = "A"
        elif score >= 75:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 40:
            grade = "D"
        else:
            grade = "F"
        result [student] = grade
    return result
result = student_grades(students)
print(result)

