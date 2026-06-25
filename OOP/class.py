class Student:
    college= "ABC College"   #class attribute

    def __init__(self, name, marks):     #constructor
        self.name=name     #object attribute
        self.marks=marks
        print("Adding new Student.... ")
        

s1=Student("nikki", 85)   
print(s1.name, s1.marks)

s2=Student("karan",79)
print(s2.name, s2.marks)
print(Student.college)