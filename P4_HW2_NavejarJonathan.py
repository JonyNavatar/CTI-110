# Jonathan Navejar
# November 21, 2025
# P4HW2
# Salary Calculator with Loops

#Pseudocode
#Asks the user employee name
#Enter user pay rate and hours worked
#Calculate overpay and regular pay. Store these values in variables, at the end of the program you will display overtime total, regular pay total, gross pay total, and number of employees entered
#Ask user to enter another employee's name to calculate salary for or "Done" to terminate program. Note we are using sentinels here.
#When user chooses to stop entering employee information , display results as shown in image below.
#THE PROGRAM ONLY TERMINATES IF THE USER ENTERS "Done" for employee name.

# Get user input for hours worked and pay rate
employee_name = input("Enter employee's name or 'done' to finish: ")

# Create Accumulator Variables for overtime pay, regular pay, gross pay, and exmployee count
overtime_pay_total = 0
regular_pay_total = 0
gross_pay_total = 0
employee_count = 0

while employee_name != 'done':
    # Add employee count plus one
    employee_count += 1 # employee_counrt = employee_count + 1
    # Ask for employee info
    hours = float(input("How many hours did " +employee_name+ " work this week? "))
    rate = float(input("What is " +employee_name+ "'s hourly pay rate? $"))

    # Calculate the overtime and regular hours using if-else statement
    if hours > 40:
        overtime_hours = hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours  

    # Finalize the output calculations
    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = regular_hours * rate
    gross_pay = regular_pay + overtime_pay

    # Add to accumulators
    overtime_pay_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay

    # Creat the table format for easy reading
    # Play with spacing to get the desired output
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("-----------------------------------------------------------------------------------------")
    print(f"{hours:<15}{rate:<12.2f}{overtime_hours:<10}{overtime_pay:<15.2f}${regular_pay:<13.2f}${gross_pay:.2f}")

    # Prompt for next employee
    employee_name = input("Enter employee's name or 'done' to finish: ")

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(overtime_pay_total, ',.2f'))
print("Total amount paid for regular hours: $", format(regular_pay_total, ',.2f'))
print("Total gross pay for all employees: $", format(gross_pay_total, ',.2f'))