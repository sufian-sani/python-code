import sqlite3
from students import students

std_1 = students(3,'John','Doe','A-')
std_2 = students(4,'Jonathon','Doe','A+')
std_3 = students(5,'Janny','Doe','B')

conn = sqlite3.connect('Emp.db')

c = conn.cursor()

# print(std_1.first)

# # c.execute("""CREATE TABLE student(
# #     roll integer,
# #     first text,
# #     last text,
# #     grade text
# # )""")
# # c.execute("INSERT INTO student VALUES(1, 'Talha','Khan','A')")
# # c.execute("INSERT INTO student VALUES(2, 'Mahin','Khan','A')")
# c.execute("INSERT INTO student VALUES(2, 'Azam','Khan','A')")
# conn.commit()
# # c.execute("SELECT* FROM student WHERE roll = 1 ")
# c.execute("SELECT* FROM student WHERE last = 'Khan' ")

# # c.fetchmany(3)
# # c.fetchall()
# c.execute("INSERT INTO student VALUES({},'{}','{}','{}')".format(std_1.roll,std_1.first,std_1.last,std_1.grade))

# c.execute("INSERT INTO student VALUES(?, ?, ?, ?)",(std_1.roll,std_1.first,std_1.last,std_1.grade))
# c.execute("INSERT INTO student VALUES(:roll, :first, :last, :grade)",(std_1.roll,std_1.first,std_1.last,std_1.grade))
# c.execute("INSERT INTO student VALUES(:roll, :first, :last, :grade)",{'roll':std_3.roll,'first':std_3.first,'last':std_3.last,'grade':std_3.grade})

conn.commit()
# c.execute("DELETE FROM student WHERE first = :first",{'first':'Azam'})
# conn.commit()
# c.execute("SELECT* FROM student WHERE last = ?",('Doe',))
c.execute("UPDATE student SET grade = :grade WHERE roll = :roll",{'grade':'A+','roll':1})
c.execute("SELECT* FROM student WHERE last = :last",{'last':'Khan'})
conn.commit()
print(c.fetchall())

conn.close()



