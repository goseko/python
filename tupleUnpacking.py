# allows you to assign each item an iterable(often a tuple) to a variable 

numbers = (1, 2, 3)
a, b, c = numbers 
print(a)
print(b)
print(c)

# 1 2 3

# this can be used to swap variables by doing 
# a, b = b, a

# a variable that is prefaced with an asterisk (*)
# takes all values from the iterable 
# that are left over from other variables 

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)