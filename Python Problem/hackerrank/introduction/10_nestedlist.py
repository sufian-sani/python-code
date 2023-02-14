# def find_minScore(score_ls):
#     s_m = min(score_ls)
#     return s_m

ls=[]
s_list=[]
score_ls=[]
s=1
for _ in range(int(input())):
    name = input()
    score = float(input())
    ls.append([name,score])
    score_ls.append(score)

s_set=set(score_ls)
score_ls=list(s_set)
score_ls.sort()
score_ls.reverse()
score_ls.pop()


s_m = min(score_ls)

ls.sort()
for i in ls:
    if i[1]==s_m:
        print(i[0])

# score_ls.pop()

# min_score=[]

# for i in range(2):
#     f_v=find_minScore(score_ls)
#     min_score.append(f_v)
#     score_ls.remove(f_v)

# ls.sort()
# min_score.sort()
# min_score.reverse()
# m_s=len(min_score)
# for i in ls:
#     for j in range(len(min_score)):
#         if i[1]==min_score[j]:
#             print(i[0])


# for i in ls:
#     if i[1]==s_m:
#         print(i[0])

# for i in ls:
#     print(i[1])


'''
students = []
sec_name = []
second_low = 0
n = int(input("Input number of students: "))
for _ in range(n):
   s_name = input("Name: ")
   score = float(input("Grade: "))
   students.append([s_name,score])
print("\nNames and Grades of all students:")
print(students)
order =sorted(students, key = lambda x: int(x[1]))
for i in range(n):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
print("\nSecond lowest grade: ",second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nNames:")
for s_name in sec_student_name:
   print(s_name)
'''