
class Person:
    def __init__(self,person_name:str,year_of_baath:int,ht_inches: int=None):
        self.__name = person_name
        self.__year_of_baath=year_of_baath
        self.__height=ht_inches
        self.abc = None

    def get_year_of_birth(self):
        return self.__year_of_baath

    def get_name(self):
        return self.__name

    def set_name(self,new_name):
        if(self.__has_any_number(new_name)):
            print("The Name is invalid")
            return
        self.__name = new_name

    def __has_any_number(self,string):
        return "0" in string

    def get_summary(self):
        # pass
        return f"Name:{self.__name}, DOB: {self.__year_of_baath}, Height: {self.__height if self.__height is not None else 'Invalid'}"


property_list = [Person("Abu", 1997, 72),
                 Person("Are", 1990),
                 Person("bar", 1987, 65),
                 Person("Baz", 2020, 80),
                 Person("ban", 1945),
                 Person("Ben", 1900, 72)]

# for person in property_list:
#     if person.get_year_of_birth() >= 1930:
#         print(person.get_summary())

class Student(Person):
    def __init__(self, person_name: str, year_of_baath: int, email_id:str, student_id:str):
        super().__init__(person_name, year_of_baath)
        self.id=student_id
        self.email=email_id

    def get_summary(self):
        return f"Name: {self.get_name()} Email: {self.email} Birth: {self.get_year_of_birth()}"

    def __str__(self):
        return self.get_summary()
        # return f"Name: {self.get_name()} Email: {self.email} Birth: {self.get_year_of_birth()}"

    def __repr__(self):
        return self.get_summary()
    #     return f"Name: {self.get_name()} Email: {self.email} Birth: {self.get_year_of_birth()}"


student = Student("A",2000,"a@google","123123gfe")
# print(student)
student.set_name("abu sufian")
# print(student)

class Teacher(Person):
    def __init__(self, person_name: str, year_of_baath: int, department: str):
        super().__init__(person_name, year_of_baath)
        self.dept = department

    def get_summary(self):
        return f"{self.get_name()} is a teacher"

new_person_list=[
    Person("Abu Sufian",1990),
    Student("S",2000,"a@google.com","stid"),
    Teacher("T",1980,"tid")
]

for p in new_person_list:
    print(p.get_summary())
    # print(p.get_name())


class PlainClass:
    pass
abc = PlainClass()
abc.age = 30
abc.name = "Movie"

print(abc.age)