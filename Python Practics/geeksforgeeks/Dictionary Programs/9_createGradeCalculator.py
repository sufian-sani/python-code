jack = { "name":"Jack Frost",
         "assignment" : [80, 50, 40, 20],
         "test" : [75, 75],
         "lab" : [78.20, 77.20]
       }
james = { "name":"James Potter",
          "assignment" : [82, 56, 44, 30],
          "test" : [80, 80],
          "lab" : [67.90, 78.72]
        }
dylan = { "name" : "Dylan Rhodes",
          "assignment" : [77, 82, 23, 39],
          "test" : [78, 77],
          "lab" : [80, 80]
        }
jess = { "name" : "Jessica Stone",
         "assignment" : [67, 55, 77, 21],
         "test" : [40, 50],
         "lab" : [69, 44.56]
       }
tom = { "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]
      }

def get_average(marks):
    total_sum=sum(marks)
    total_sum=float(total_sum)
    l=len(marks)
    total_avg_mark = total_sum/l
    return total_avg_mark

def mark_distibution(d_name):
    assisment=get_average(d_name['assignment'])
    test = get_average(d_name['test'])
    lab = get_average(d_name['lab'])

    assisment_dis = assisment*0.1
    test_dis = test * 0.7
    lab_dis = lab * 0.2

    return assisment_dis+test_dis+lab_dis

def get_grade(avg_mark):
    if avg_mark >= 90:
        return 'A'
    elif avg_mark >= 80:
        return 'B'
    elif avg_mark >= 70:
        return 'C'
    elif avg_mark >= 60:
        return 'D'
    else:
        return 'E'

def name_print(name_dic):
    if name_dic == jack:
        return 'Jack Frost'
    elif name_dic == james:
        return 'James Potter'
    elif name_dic == dylan:
        return 'Dylan Rhodes'
    elif name_dic == jess:
        return 'Jessica Stone'
    elif name_dic == tom:
        return 'Tom Hanks'
    else:
        return 'Nothing'

student_list=[jack, james, dylan, jess, tom]

for i in student_list:
    print(name_print(i))
    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    m=mark_distibution(i)
    print('Average marks of Jack Frost is: ',m)
    print('Letter Grade of Jack Frost is: ',get_grade(m))
    print()