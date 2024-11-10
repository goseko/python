# function that takes multiple words as argument and returns a concatenated version of those words separated by dashes (-)
# function should be able to take a varying number of words as the argument 


# recall using *args as a function parameter enables you to pass an arbitrary number of arguments to that function 

def concatenate(*args):
    return '-'.join(args)

print(concatenate("I", "love", "Python", "!"))