class Student:
    def __init__(self,name,grades):
        # self.name = "vala"
        self.name = name
        # self.grades = (12,34,56,7,8)
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)
    
        
st1 = Student("amirvala", (12,4,5,6,7,5,3,3,1))
print(st1.name)      
print(st1.grades)
# print(Student.average(st1)) code below is the same thing as this one
print(st1.average())

st2 = Student("gholi", (1,23,4,5,6,7,8,34,54,))
print(st2.average())