import random

# Constants
NUM_ROUNDS = 5

# Welcome message
print("Welcome to the High-Low Game!")
print("--------------------------------")

# Initialize the player's score
score = 0

# Game loop for multiple rounds
for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    
    # Generate random numbers for the player and the computer
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    # Show the player's number
    print(f"Your number is {player_number}")
    
    # Get the user's guess (ensure valid input)
    while True:
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        if guess in ['higher', 'lower']:
            break
        else:
            print("Please enter either 'higher' or 'lower'.")
    
    # Determine if the player was correct
    if (guess == 'higher' and player_number > computer_number) or (guess == 'lower' and player_number < computer_number):
        print("You were right!")
        score += 1
    else:
        print("Aww, that's incorrect.")
    
    # Show the computer's number
    print(f"The computer's number was {computer_number}")
    
    # Show the player's score
    print(f"Your score is now {score}")
    print()

# Conditional ending messages
print("Thanks for playing!")

if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
