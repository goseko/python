# else can also follow  a for or while loop 
# the code within it is called the loop finishes
# when a break statement does not cause an exit from the loop 

for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 3")

# for  the first loop executes normally  resulting in 
# "unbroken 1"
# second loop exits due to a break which is why else statements is not executed


# carousel designed for 3 people who are each at least 16 years old 
# program takes 3 passengers ages as inputs and inserts them in a list 
#complete program that it finds a value less than 16, breaks the loop and outputs "too young 
# if age requirement is satisfied the program outputs "get ready"

ages = []
i = 0
while i<3:
    age = int(input())
    if age < 16:
        i = 0
        break
    else:
        ages.append(age)
        i+=1
    # print(ages)
if i > 0:
    print("Get ready!")
else:
    print("Too young!")


# what is the largest number this code prints 

for i in range(10):
    if i > 5:
        print(i)
        break
    else:
        print("7")

        # 6

# TRY/ EXCEPT 
#  only executed if no errors occurs in the try statement 

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

    # 1 3 4

# what is the sum of the numbers printed by this code 

try:
    print(1)
    print(1 + "1" == 2)
    print(2)
except TypeError:
    print(3)
else:
    print(4)