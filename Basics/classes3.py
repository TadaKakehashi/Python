class Student:
    def funct(self):
        print("Student funct called")


class Kid(Student):
    def funct1(self):
        print("This is a child class!")


obj = Kid()
obj.funct()
obj.funct1()
