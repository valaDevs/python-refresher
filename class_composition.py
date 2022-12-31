class BookShelf:
    def __init__(self, *books):
        self.books = books
        
    def __str__(self):
        return f"BookShelf with {len(slef.books)} books."
    

class Book(BookShelf):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Book {self.name}"