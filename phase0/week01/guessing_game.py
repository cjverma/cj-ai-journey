import random

def check_guess(secret, guess):
    if secret == guess:
        return 'correct'
    elif guess > secret:
        return 'high'
    else:
        return 'low'

def run_game():
    secret = random.randint(1, 50)
    x = 0
    while x < 6:
        try:
            guess = int(input("What is your guess? "))
        except ValueError:
            print("Please enter a number!")
            continue
        result = check_guess(secret, guess)
        print(result)
        if result == 'correct':
            print(f'It took you {x+1} attempt(s) to get it right!')
            break
        x = x + 1
    if x == 6:
        print (f'You ran out of attempts! Correct number was {secret} ! Try again!')

run_game()