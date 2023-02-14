n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
number = student_marks[query_name]

size=len(number)
index = 0
for i in number:
    index = index + i

totalAvg = index/size

print("%.2f"%totalAvg)