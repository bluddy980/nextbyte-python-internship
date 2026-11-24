# Problem 1: Sum of Natural Numbers
def calculate_sum(number):
    total = 0
    for value in range(1, number + 1):
        total += value
    return total


# Problem 2: Multiplication Table
def display_table(number):
    for multiplier in range(1, 11):
        print(number, "x", multiplier, "=", number * multiplier)


# Problem 3: Factorial of a Number
def calculate_factorial(number):
    factorial = 1
    for value in range(1, number + 1):
        factorial *= value
    return factorial


# Problem 4: Check Prime Number
def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


# Problem 5: Count Vowels
def count_vowels(text):
    vowels = "aeiou"
    vowel_count = 0

    for character in text.lower():
        if character in vowels:
            vowel_count += 1

    return vowel_count


# Function to Get a Valid Integer
def get_integer(message, minimum=None):
    while True:
        try:
            number = int(input(message))

            if minimum is not None and number < minimum:
                print("Please enter a number greater than or equal to", minimum)
                continue

            return number

        except ValueError:
            print("Invalid input! Please enter an integer.")


# Main Menu
def main():
    while True:
        
        print("1. Sum of Natural Numbers")
        print("2. Multiplication Table")
        print("3. Factorial of a Number")
        print("4. Check Prime Number")
        print("5. Count Vowels")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            number = get_integer("Enter a positive number: ", 1)
            print("Sum of natural numbers:", calculate_sum(number))

        elif choice == "2":
            number = get_integer("Enter a number: ")
            print("Multiplication Table:")
            display_table(number)

        elif choice == "3":
            number = get_integer("Enter a non-negative number: ", 0)
            print("Factorial:", calculate_factorial(number))

        elif choice == "4":
            number = get_integer("Enter a positive integer: ", 1)

            if is_prime(number):
                print(number, "is a prime number.")
            else:
                print(number, "is not a prime number.")

        elif choice == "5":
            text = input("Enter a text: ")

            while not text.strip():
                print("Text cannot be empty!")
                text = input("Enter a text: ")

            print("Total vowels:", count_vowels(text))

        elif choice == "6":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please select between 1 and 6.")
