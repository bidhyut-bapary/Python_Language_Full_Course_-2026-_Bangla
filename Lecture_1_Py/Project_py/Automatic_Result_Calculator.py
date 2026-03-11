# Project Name: Automatic Student Result Calculator
# The Python Code
# 1. Input & Type Casting

name = input("Enter Student name:")
math_marks = float(input("Enter math marks:")) # type casting to float
science_marks = float(input("Enter science marks:"))
english_marks = float(input("Enter english marks:"))

# 2. Average Marks Calculation
# Total Marks Calculation
total_marks = math_marks + science_marks + english_marks # Total marks calculation
average_marks = total_marks / 3 # Average marks calculation

# 3. Pass-Fail Validation (Relational Operator)
# For example, pass if the average marks are 40 or more

is_passed = average_marks >= 40 # Relational operator to check pass or fail

# 4. Results are shown as Output.
# Output the results
print("Student Name:", name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Pass Status:", is_passed) # Boolean output