from dataclasses import dataclass
@dataclass#decorator
class Book:
    title:str
    author:str
    pages:int
    price:float
    def bookinfo(self):
        return f"{self.title} by {self.author}, costs {self.price}"
b1=Book("War and Peace","Leo Tolstoy",1222,39.95)
b2=Book("The Catcher in the Rye","JD Salinger",433,29.95)
b3=Book("War and Peace","Leo Tolstoy",434,39.95)
b4=Book("Python for dummies","Leo Tolstoy",1231,30.0)

print(b1.title)
"""
creating a dataclass available in python7 is easier and impliments the functions seen before automatically
"""
print(b1==b3)
print(b1.bookinfo())
