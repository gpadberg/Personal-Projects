import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess is too low. Please guess again.")
        elif guess > random_number:
            print("Guess is too high. Please guess again.")
    print(f"Congratulations! You've guessed the number {random_number} correctly!")

def computer_guess(x):
    print("Think of a number between 1 and your target number. The computer will guess your number.")
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too low (L), high (H), or correct(C)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer has successfully guessed your number, {guess}!")

if __name__ == "__main__":
    mode = input("Welcome to Number Guess. Would you like yourself or the computer to guess? Enter 'me' to guess or 'computer' for the computer to guess: ").lower() 
    if mode == "me":
        x = int(input("Enter an upper bound, so that numbers in this game will range from 1 to this bound: "))
        guess(x)
    elif mode == "computer":
        x = int(input("Enter an upper bound, so that numbers in this game will range from 1 to this bound: "))
        computer_guess(x)
    else:
        print("Invalid input. Please try again.")
