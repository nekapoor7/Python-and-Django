'''Given the names and grades for each student in a Physics class of

students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,
, the number of students.
The subsequent lines describe each student over lines; the first line contains a student's name, and the second line
contains their grade. '''

N = int(input())
final = list()
for i in range(N):
    lst = list()
    name = str(input())
    marks = float(input())
    lst.append(name)
    lst.append(marks)
    final.append(lst)
k = list()
for i in range(len(final)):
    k.append(final[i][1])
x = min(k)
k1 = list()
for i in range(len(k)):
    if x != k[i]:
        k1.append(k[i])
y = min(k1)
student = list()
for i in range(len(final)):
    if y == final[i][1]:
        student.append(final[i][0])
student.sort()
for i in range(len(student)):
    print(student[i])

    