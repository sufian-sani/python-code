class Student_Dtails:
    versity='Deffodil International University'
    def __init__(self,name,subject,section):
        self.name=name
        self.subject=subject
        self.section=section

    def show(self):
        print(self.name,self.subject,self.section,self.versity)


student_1=Student_Dtails(input('1st Student Name: '),input('1st Student Subject: '),input('1st Student section: '))
student_2=Student_Dtails(input('2nd Student Name: '),input('2nd Student Subject: '),input('2nd Student section: '))
student_3=Student_Dtails(input('3rd Student Name: '),input('3rd Student Subject: '),input('3rd Student section: '))

student_1.show()
student_2.show()
student_3.show()
