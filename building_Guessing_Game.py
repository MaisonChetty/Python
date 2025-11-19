secret_number = 9
guess_count = 0
lives = 3

while lives >= 1:
    guess = int(input("Guess the secret number (between 1 and 10): "))
    guess_count += 1

    if guess < secret_number:
        print("Too low!")
        lives -= 1
    elif guess > secret_number:
        print("Too high!")
        lives -= 1
    else:
        print("Congratulations! You've guessed the secret number.")
        break
else:
    print("Sorry, you've run out of lives. The secret number was:", secret_number)

