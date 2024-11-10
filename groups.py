# sorrounding part of a regular expression with parentheses
# a group can be given as an argument to metacharacters such as * and ?

import re 

pattern = r"egg(spam)*"

if re.match(pattern,"egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")

 #spam represents a group in the example 

   # group can be called using the method groups()
   # group(0) or group() - returns the whole match 
   # group(n) where n is greter than 0 returns nth group

import re

pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

    #abcdefghi
    #abcdefghi
    #bc
    #de
    # ('bc', 'de', 'fgh', 'g')


# named groups 
# non-capturing groups 
# named groups format (?P<name>...)
# ...is the content 
# they can be accessed by group(name) and number

# non-capturing groups  format (?:...)
# they are not accessible by the group method
#they can be added to an existing regural expression without breaking the numbering 

import re

pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

# abc
# ('abc', 'ghi')