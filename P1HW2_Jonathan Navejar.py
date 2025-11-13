# Jonathan Navejar
# November 12, 2025
# P1HW2_Jonathan Navejar.py
# This is a program for calculating and displaying travel expenses. 

print("This program calculates and displays travel expenses")
print()
#Ask user to enter their budget
budget = int(input("Enter Budget: "))
#Ask user to enter travel destination
destination = input("Enter your travel destination: ")
#Ask user for amount they will spend on gas
fuel = int(input("How much do you think you will spend on gas? "))
#Ask user for amount they will spend on accomodation
accomodation = int(input("Approximately, how much will you need for accomodation/hotel? "))
#Ask user for amount they will spend on food
food = int(input("Last, how much do you need for food? "))
# add expenses and subtract from budget to get remaining balance
remaining_balance = budget - (fuel + accomodation + food)
print()
#Display result
print("------------Travel Expenses------------ ")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", fuel)
print("Accomodation:", accomodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)