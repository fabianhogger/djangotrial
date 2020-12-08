"""
magic methods display
"""
"""
String Representation
"""
class Book:

    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __repr__(self):
        return  f"title={self.title} ,author= {self.author}, price= {self.price}"
"""
Object equality and comparison
"""
    def __eq__(self,value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to non-book")
        return(self.title==value.title and self.author==value.author and self.price==value.price)


b1=Book("War and Peace","Leo Tolstoy",39.95)
b2=Book("The Catcher in the Rye","JD Salinger",29.95)
#print(str(b1))
#print(repr(b2))
