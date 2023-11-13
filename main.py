# # Importing the 'random' module to generate random numbers
# import random

# # Printing the welcome message and game instructions to the user
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100")

# # Asking the user to choose a difficulty level (easy or hard) and converting the input to lowercase
import random


def generate_random_number():
  return random.randint(1, 100)


def compare_numbers(generated_number, guess):
  if guess > generated_number:
    return "Too High"
  elif guess < generated_number:
    return "Too Low"
  else:
    return "Correct"


def play_game(attempts):
  generated_number = generate_random_number()

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")

  while attempts > 0:
    guess = int(input("Make a guess: "))
    result = compare_numbers(generated_number, guess)
    print(result)

    if result == "Correct":
      print(f"You got it! The answer was {generated_number}")
      return True

    attempts -= 1
    print(
        f"You have {attempts} {'attempts' if attempts > 1 else 'attempt'} remaining to guess the number."
    )

  print(f"Sorry, you ran out of attempts. The number was {generated_number}.")
  return False


def main():
  difficulty_level = input(
      "Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if difficulty_level == 'easy':
    attempts = 10
  elif difficulty_level == 'hard':
    attempts = 5
  else:
    print("Wrong difficulty level chosen. Please try again.")
    return

  play_game(attempts)


if __name__ == "__main__":
  main()
