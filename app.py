# data hiding 
# weakly private methods have a single underscore in the beginning that does not stop external code from accessing them. 
# its only actual effect is that from module_name import * wont import names beginning with an underscore
'''
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)
    def push(self, value):
        self._hiddenlist.insert(0, value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
    

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
'''
# strong private methods 
# they have double underscores at the beginning of their names 
# this is to avoid bugs if there are subclasses that have methods or attributes with same name 
'''
class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)
'''

# you are given a BankAccount class and need to add a deposit() method to it, which adds the given amount to the private balance property. the code should declare a BankAccount object with an initial balance of 0, take a number from user input, add it to the balance using the deposit() method  and output the object 
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def __repr__(self):
        return "Account Balance: {}".format(self._balance)
    
    def deposit(self, amount):
        self._balance += amount

acc = BankAccount(0)
acc.deposit(int(input()))
print(acc)

   