# 1. VARIABLES AND DATA TYPES
name = "Ali"
age = 20
height = 5.8
is_student = True

print("\n--- Variables and Data Types ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# 2. USER INPUT AND OUTPUT
print("\n--- User Input ---")

student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))

print("Hello,", student_name)
print("Your age is:", student_age)

# 3. OPERATORS
print("\n--- Arithmetic Operators ---")

num1 = 20
num2 = 10

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)

# Comparison operators
print("\n--- Comparison Operators ---")
print("20 > 10:", num1 > num2)
print("20 == 10:", num1 == num2)

# 4. CONDITIONAL STATEMENTS
print("\n--- Conditional Statements ---")

marks = int(input("Enter your marks (0-100): "))

if marks >= 80 and marks <= 100:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
elif marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks!")

# 5. EVEN OR ODD
print("\n--- Even or Odd ---")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")
