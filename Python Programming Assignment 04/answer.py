"""Instructions: Implement Python programs to accomplish the following task
Task
You are tasked with creating a Python program that serves as an interactive tool for a friend who enjoys exploring numbers. The program should begin by prompting the user to enter their name and then ask them for three of their favorite numbers. After gathering this information, the program should greet the user with a personalized message that includes their name. The three numbers provided by the user should be stored in a list. The program should then check if any of the numbers are even or odd, and store this information in a separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" or "odd". Following this, the program should use a for loop to iterate over the list of numbers, and for each number, it should create a tuple containing the number and its square. These tuples should be printed in a creative and engaging format. Additionally, the program should calculate the sum of the three numbers and print the result, accompanied by an encouraging message. Finally, the program should determine if the sum is a prime number and notify the user with an appropriate message. The goal is to make the tool both enjoyable and informative, allowing the user to explore their favorite numbers in a fun and interactive way, while also introducing some interesting logical checks.

Example Output:

Enter your name: Alex
Enter your first favorite number: 4
Enter your second favorite number: 6
Enter your third favorite number: 9
Hello, Alex! Let's explore your favorite numbers:
The number 4 is even.
The number 6 is even.
The number 9 is odd.
The number 4 and its square: (4, 16)
The number 6 and its square: (6, 36)
The number 9 and its square: (9, 81)
Amazing! The sum of your favorite numbers is: 19
Wow, 19 is a prime number!
"""

# Solution:
def get_numbers():
    return [int(input(f"Enter your {i} favorite number: ")) for i in range(1, 4)]

def check_even_odd(numbers):
    return [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

def calculate_squares(numbers):
    return [(num, num**2) for num in numbers]

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    name = input("Enter your name: ")
    numbers = get_numbers()

    print(f"Hello, {name}! Let's explore your favorite numbers:")

    even_odd_list = check_even_odd(numbers)
    for num, even_odd in even_odd_list:
        print(f"The number {num} is {even_odd}.")

    square_list = calculate_squares(numbers)
    for num, square in square_list:
        print(f"The number {num} and its square: ({num}, {square})")

    total_sum = sum(numbers)
    print(f"Amazing! The sum of your favorite numbers is: {total_sum}")

    if check_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"The sum {total_sum} is not a prime number.")

main()
