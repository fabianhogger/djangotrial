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

    def __eq__(self,value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to non-book")
        return(self.title==value.title and self.author==value.author and self.price==value.price)
    def __ge__(self,value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to non-book")
        return (self.price>=value.price)
    def __lt__(self,value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to non-book")
        return (self.price<value.price)


b1=Book("War and Peace","Leo Tolstoy",39.95)
b2=Book("The Catcher in the Rye","JD Salinger",29.95)
b3=Book("War and Peace","Leo Tolstoy",39.95)
b4=Book("Python for dummies","Leo Tolstoy",30)
#print(str(b1))
#print(repr(b2))
"""
Object equality and comparison
"""
print(b1==b3)
print(b1==b2)
print(b1<b4)
print(b1<=b2)
