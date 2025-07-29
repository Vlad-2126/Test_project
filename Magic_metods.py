class Book:
    def __init__(self,title,author,pages):
        self.title = title.capitalize()
        self.author = author.capitalize()
        self.pages = int(pages)
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
def book_test():
    book1 = Book("Python", "Smith", 300)
    book2 = Book("Python", "Smith", 300)
    book3 = Book("C++", "Johnson", 250)

    print(book1 == book2)  # True
    print(book1 < book3)   # False
    
# book_test()

class IPhonPrice:
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return "Product: iPhone, Price: $1200"
    
    def __repr__(self):
        return "'iPhone', 1200"

def iphon_price_test():
    c =IPhonPrice("Oleg")
    print(c)
    print(repr(c))

# iphon_price_test()

class CustomList:
    def __init__(self,items):
        self.items = items
    
    def __getitem__(self,index):
        print(f"Item: {self.items[index]}")
        return self.items[index]
    
    def __setitem__(self,item,value):
        print(f"{self.items[item]} is now {value}")
        self.items[item] = value
        
    def __delitem__(self,value):
        print("Object is gone")
        del self.items[value]
        
        
def custom_list_test():
    lst = CustomList([1, 2, 3])
    print(lst[1])     
    lst[1] = 10       
    del lst[0]
    
# custom_list_test()

class Cart:
    def __init__(self):
        self.products = []
    
    def __len__(self):
        print(f"Your card has {len(self.products)} items")
        return len(self.products)
    
    def __bool__(self):
        if len(self.products) == 0:
            print("Your card is empty")
        return len(self.products) == 0
        
    def add_product(self, product):
        self.products.append(product)
    
def cart_test():
    cast1 = Cart()
    len(cast1)
    bool(cast1)
    cast1.add_product("Pelmeni")
    cast1.add_product("Craboue")
    cast1.add_product("Lemon")
    len(cast1)
    bool(cast1)

# cart_test()

class Wallet:
    def __init__(self,ammount):
        self.ammount = ammount
    
    def __add__(self,other):
        return self.ammount + other.ammount
    
    def __sub__(self,other):
        return self.ammount / other.ammount

def wallet_test():
    w1 = Wallet(50)
    w2 = Wallet(30)
    w3 = w1 + w2  # Wallet(80)
    print(w3)
    
# wallet_test()