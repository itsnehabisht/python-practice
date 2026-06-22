import random
num=random.randint(1,100)

while True:

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    for i in range(1, 6):
        guess = int(input("Guess the number: "))
        if guess == num:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess > num:
            print("Too high! Try again.")
        elif guess < num:
            print("Too low! Try again.")
        else:
            print("Sorry, that's not the correct number. The correct number was:", num)

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing! Goodbye!")
        break