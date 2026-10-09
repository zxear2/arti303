# Task 1 
name = "Sara Al-Otaibi"
age = 20
gpa = 3.6
is_enrolled = True



# Task 2 
dean_list = gpa >= 3.5


# Task 3 
report = f"{name} (age {age}, GPA {gpa}) is enrolled and made the Dean's list."
print(report)
print()

# Task 4 
raw_gpa = "3.87"
bad_value = "N/A"

# 1
raw_gpa_value = float(raw_gpa)

# 2
try:
    bad_value_converted = float(bad_value)
except ValueError:
    print(f"Could not convert '{bad_value}' to a number.")
    print()


# Task 5 
name2 = "Omar Al-Zahrani"
age2 = 22
gpa2 = 4.0
is_enrolled2 = True
dean_list2 = gpa2 >= 3.5
report2 = f"{name2} (age {age2}, GPA {gpa2}) is enrolled and made the Dean's list."
print(report2)
print()

name3 = "Fatima Al-Harbi"
age3 = 19
gpa3 = 3.1
is_enrolled3 = True
dean_list3 = gpa3 >= 3.5
status3 = "made" if dean_list3 else "did not make"
report3 = f"{name3} (age {age3}, GPA {gpa3}) is enrolled and {status3} the Dean's list."
print(report3)
print()

# Task 6 
m = 2.0
x = 3.5
b = 1.0
y = m * x + b
print(f"y = {y} (Represents a linear equation calculation used in AI/Machine Learning models).")
print()

ai_name = "Khalid"
ai_age = 23
print(f"Hello, my name is {ai_name} and I am {ai_age} years old.")
print()
