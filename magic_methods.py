class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self): # Magic Method
        return f"person {self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"
        
vala = Person('vala', 21)
print(vala)
