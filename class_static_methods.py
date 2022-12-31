class classTest:
    def instance_method(self):
        print(f"called instane_methd of {self}")
    
    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")
        
    @staticmethod
    def static_metod():
        print("called static method")
        
        
# test = classTest()
# test.instance_method()
# classTest.instance_method(test)
# classTest.class_method()
# classTest.static_metod()


class Book:
    TYPES = ("Hardcover", "Paperback")
    
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
        
    @classmethod
    def hardcover(cls,name, page_weight):
        return Book(name,Book.TYPES[0], page_weight + 100)    
    
    @classmethod
    def paper_back(cls,name,page_weight):
        return Book(name,Book.TYPES[1], page_weight)
    
    
# print(Book.TYPES)
# book = Book('Harry potter', 'hard cover', 1233)
book = Book.hardcover("Harry Poter", 1000)
light = Book.paper_back("bug bounty bootcamp", 700)

print(book)
print(light)




