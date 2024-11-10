class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())   

# new one 

class person:
    def __init__(self, name):
        self.name = name

        @classmethod
        def sayHi(cls):
            print("Hi")

  #Static methods 

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = pizza(ingredients)          

# calculator that adds 
class Calculator:
    @staticmethod
    def add(g1,g2):
        return g1 + g2
    
n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))

# making egg attribute strongly private and accessing it from outside the class

class Test:
    __egg = 7
t= Test()
print(t._Test __egg)