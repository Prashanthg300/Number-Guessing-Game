from art import logo
import random

print(logo)
computer_generated_number = random.randint(1, 100)

def guessing(guess):
    if guess == computer_generated_number:
        return "You guessed the number right!"
    elif guess < computer_generated_number:
        return "Your guess is too low"
    else:
        return "Your guess is too high"

def difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == 'easy':
    return 10
  else:
    return 5
  
def play_game():
  
  print("I'm thinking of a number between 1 and 100")
  attempts = difficulty()
  guess = 0
  while attempts > 0 and guess != computer_generated_number:
    print(f'You have {attempts} attempts to guess the number')
    guess = int(input("Make a Guess: "))
    print(guessing(guess))
    attempts -= 1
    if attempts == 0:
      print("You've run out of guesses. You lose")
      print(f"The answer was {computer_generated_number}")
      break

print("Welcome to the number guessing game.")
users_choice = input("Do you wanna play guessing number ?. Type 'yes' to play or 'no' to quit. ").lower()

while users_choice == 'yes':
  play_game()