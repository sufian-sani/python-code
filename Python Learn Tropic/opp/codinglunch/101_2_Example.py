# from datetime import date

class Datedifferent:
    def __init__(self,year1,year2):
        self.year1=year1
        self.year2=year2
        # self.month=month
        # self.date=date
    def check(self):
        if self.year1 >= self.year2:
            print(self.year1 - self.year2)
        else:
            print(self.year2 - self.year1)

a = Datedifferent(2002,1998)
a.check()