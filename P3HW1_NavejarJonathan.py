# Jonathan Navejar
# November 20, 2025
# P3HW1
# This is a program provides statistics for six module grades.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

print("\n------------Results------------")
print(f"Lowest Grade:     {lowest}")
print(f"Highest Grade:    {highest}")
print(f"Sum of Grades:    {total}")
print(f"Average:          {average:.2f}")
print("----------------------------------------")

if average >= 90:
    print("Your grade is: A")
elif average >= 80:
    print("Your grade is: B")
elif average >= 70:
    print("Your grade is: C")
elif average >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")