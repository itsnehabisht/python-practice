class Student:
    college= "ABC College"   #class attribute

    def __init__(self, name, marks):
        self.name=name     #object attribute
        self.marks=marks
        
    @staticmethod    #decorator
    def hello():
        print("Hello Student")

    def welcome(self):
        print("Welcome Student", s1.name)

    def get_marks(self):
        return self.marks

s1=Student("nikki", 85)   
s1.welcome()
print(s1.get_marks())