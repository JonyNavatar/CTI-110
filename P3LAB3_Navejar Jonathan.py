# Jonathan Navejar
# November 20, 2025
# P3LAB3
# This is a program for calculating bill and coin currency amounts. 

#Get Value from user

change = float(input("Enter an amount of money as a float: $"))

#Converting the valuej to an integer
change = round(change * 100)

#Determin how many coins are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickles = change // 5
change = change - (num_nickles * 5)

num_pennies = change

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickles > 0:
    if num_nickles == 1:
        print(f"{num_nickles} Nickle")
    else:
        print(f"{num_nickles} Nickles")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")

# If there are no bills or coins print "No change"
if num_dollars == 0 and num_quarters == 0 and num_dimes == 0 and num_nickles == 0 and num_pennies == 0:
    print("No change")
