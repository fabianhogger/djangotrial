class Book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price
        self._discount=0.1

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
    def __repr__(self):
        return  f"title={self.title} ,author= {self.author}, price= {self.price}"
    def __call__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
        self._discount=0.1
    def __getattribute__(self,name):
        if (name=="price"):
            p=super().__getattribute__("price")
            d=super().__getattribute__("_discount")
            return (p-p*d)
    def __setattr__(self,name,value):
        if name=="price":
            if type(value) is not float:
                raise ValueError("value must be a float")
        return (super().__setattr__(name,value))

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

    def __getattr__(self,name):
        return name+"it not here!"


b1=Book("War and Peace","Leo Tolstoy",39.95)
b2=Book("The Catcher in the Rye","JD Salinger",29.95)
b3=Book("War and Peace","Leo Tolstoy",39.95)
b4=Book("Python for dummies","Leo Tolstoy",30.0)
#print(str(b1))
#print(repr(b2))
"""
print(b1==b3)
print(b1==b2)
print(b1<b4)
print(b1<=b2)
"""
