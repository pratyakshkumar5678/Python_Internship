import random
guess_number=random.randint(1,100)
max_attempts=5
attempts=0
print("Welcome to the number guessing game.\n")
print("Rules are simple:\n1.)Guess a number from 1 to 100.\n2.) You only get 5 chances. ")
while attempts < max_attempts:
    guess=int(input(f"Attempt {attempts+1}/{max_attempts}: "))
    if guess==guess_number and attempts==0:
        print(f"Are you Human. You guessed it in {attempts+1} attempts.")
        break
    elif guess==guess_number and attempts>=1 and attempts<max_attempts:
        print(f"Congratulations! You guessed the number in {attempts+1} attempts.")
        break
    elif guess<(guess_number-10):
        print("Guessed number is too low.")
    elif (guess_number-10)<guess<guess_number:
        print("Close but slightly higher.")
    elif (guess_number+10)<guess:
        print("Guessed number is too high.")
    else:
        print("Close but slightly lower.")
    attempts+=1
    if guess!=guess_number and attempts==max_attempts:
        print(f"Sorry, out of chances. The correct number to guess was {guess_number}.")
        