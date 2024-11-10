# conditional expressions provide the functionality of if statements while using less code 
#  shouldnt be overused since they can easily reduce code readability
# used when assigning variables 
# also known as applications of the ternary operator 

a = 7
b = 1 if a >= 5 else 42
print(b)

# 1

# ternary operators takes three arguments 



# bank card withdrawal system 
# takes amount the user wants to withdraw and outputs remaining money
#if requested cash is greater than the balance the program outputs "Error"
# the bank wants to set a minimal value of $500 for withdrawal

balance = int(imput())
to_cash = int(input())

money_left = balance - to_cash if to_cash <= balance and to_cash >= 500 else print("Error")

print(money_left)

# 
status = 1
msg = "Logout" if status == 1 else "LOGIN"

print(msg)