# you are given a number input 
# need to check if its a valid phone number 
# valid phone number has exactly 8 digits and starts with 1,8 or 9
# output valid if valid and invalid if not 

import re 

number = input()

pattern = r"\A(1|8|9)\d{7}$"

if re.match(pattern,num):
    print("Valid")
else:
    print("Invalid")
    