# Jonathan Navejar
# November 21, 2025
# P3HW2
# This is a program provides employee wages based on hours worked and hourly rate.

#Pseudocode
#Ask user to enter number of hours the employee worked this week
#Ask user to enter employee's pay rate
#Evaluate if employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours
#The employee should receive 1.5 times their normal pay rate for any overtime hours worked.
#Calculate amount employee should be paid for regular hours worked.
#Display gross pay (total amount that should be paid to employee)
#The program is to display the following (Employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours and gross pay).

# Get user input for hours worked and pay rate
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Add some space and a header for clarity
print("---------------------------------------")
print("Employee name: ", employee_name)
print()

# Calculate the overtime and regular hours using if-else statement
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Finalize the output calculations
overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Creat the table format for easy reading
# Play with spacing to get the desired output
print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("-----------------------------------------------------------------------------------------")
print(f"{hours_worked:<15}{pay_rate:<12.2f}{overtime_hours:<10}{overtime_pay:<15.2f}${regular_pay:<13.2f}${gross_pay:.3f}")