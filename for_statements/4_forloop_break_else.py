#!/usr/bin/python3
"""program to display student marks from record"""
student_name = 'Gabby'

marks = {'pius': 90, 'james': 77, 'Arthur': 70}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No record matches.')
