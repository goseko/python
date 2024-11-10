# property make an attribute read-only
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pinapple_allowed(self):
        return False
    
pizza = Pizza(["cheese", "tomato"])
print(pizza.pinapple_allowed)
pizza.pinapple_allowed = True

#example
class Person:
    def __init__(self, age):
        self.age = int(age)

    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False
        
# properties can also be set by defining setter/getter functions 
# setter - sets the corresponding property's value 
# getter gets the value 

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password:")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")
            
pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)


#isEven
class Number:
    def __init__(self, num):
        self.value = num

    @property
    def isEven(self):
        return self.value % 2 == 0
    
x = Number(int(input()))
print(x.isEven)

#making a setter for the property name

class Person:
    def __init__(self, name):
        self._name = name  
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value 
        