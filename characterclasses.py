# provides a way to match only one of a specific set of characters 
# character class is created by putting the characters it matches inside square brackets 

import re 
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
    print("match 1")
if re.search(pattern, "qwertyuiop"):
    print("match 2")
if re.search(pattern, "rhythm myths"):
    print("Match 3")

# character classes can also match ranges of characters 
# [a-z] [G-P] [0-9]
#   multiple ranges can also be included in one class for example 
# [A-Za-z] matches any letter of any case

import re 
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern,"LS8"):
    print("match 1")
if re.search(pattern,"E3"):
    print("match 2")
if re.search(pattern, "1ab"):
    print("match 3")

#place a^ at the start of a character class to invert it 
# causes it to match any character other than the ones included 
# metacharacter ^ has no meaning unless it is the first character in a class 

import re
pattern = r"[^A-Z]"
if re.search(pattern, "this is all quiet"):
    print("match 1")
if re.search(pattern,"AbCdEfG123"):
    print("match 2")
if re.search(pattern, "THISISALLSHOUTING"):
    print("match 3")


# practise 
import re 
Id = input()

pattern = r"[A-Z][A-Z][0-9][0-9]$"

if re.search(pattern, Id):
    print("searching")
else:
    print("Wrong format")

# metacharacters  * + ? {and}
# these specify number of repetitions
# * means "zero or more repetitions of the previous thing "
# it tries to match as many repetitions as possible 
# the previous thing can be a single character , class or a group of characters in parentheses

import re 
pattern = r"egg(spam)*"

if re.match(pattern,"egg"):
    print("Match 1")
if re.match(pattern,"eggspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")

 # matches string that start with egg and follow with zero or more spams   

 # metacharacter + is very similar to * except it means one or more repetitions 
 # as opposed to "zero or more repetitions"


 import re

pattern = r"g+"

if re.match(pattern, "g"):
    print("match 1")
if re.match(pattern, "ggggggggg"):
    print("Match 2")
if re.match(pattern,"abc"):
    print("Match 3")

# metacharacter ? means "zero or one repetitions "

import re
pattern = r"ice(-)?cream"

if re.match(pattern,"ice-cream"):
    print("Match 1")
if re.match(pattern,"icecream"):
    print("Match 2")
if re.match(pattern, "sausages"):
    print("Match 3")
if re.match(pattern, "ice--cream"):
    print("Match 4")


 # Curly braces 
 # used to represent number of repetitions between two numbers 
 # if the first number is missing its taken to be zero 
 # if the second number is missing it is taken to be infinity 
 # 

import re 
pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print ("match 1")
if re.match(pattern,"999"):
    print("match 2")
if re.match(pattern, "9999"):
    print("match 3")

    # wont print match 3


# authentication system - takes password inputs
# returns  "password created" if 
# has  at least one uppercase character 
# has atleast one number 

import re 
password = input()

patter = r"[A-Z][a-z]*[0-9]+"

if re.search(pattern, password):
    print("password created")
else:
    print("wrong format")