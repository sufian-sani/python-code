class Student:
    def __init__(self,name,subject,section):
        self.name = name
        self.subject = subject
        self.section = section
    
    def show(self):
        print("\nName : ",self.name,"\nSubject : ",self.subject,"\nSection : ",self.section)

first = Student(input("Enter Your Name: "),input("Subject: "),input("Section: "))
second = Student(input("Enter Your Name: "),input("Subject: "),input("Section: "))

first.show()
second.show()