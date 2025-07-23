#Guessing Game - Anthony, Alvert, Tammy, Liz


import random


def generate_random_number():
    random_number = random.randint(1, 100)
    return random_number


def get_user_guess():
    while True:
        user_input = input("testing; ")
        if 1 <= int(user_input) <= 100:
            return user_input
        else: 
            print("This is invalid")
        


def play_guessing_game():
    secret_number = generate_random_number()
    Attempts = 0
    while True:
        guess = int(get_user_guess())
        if guess > secret_number:
            print('Your guess is too high!')
            Attempts += 1
            print(f'Attempts {Attempts}')
        elif guess < secret_number:
            print('Your guess is too low!')
            Attempts += 1
            print(f'Attempts {Attempts}')
        else:
            print(f'You win! You guessed the number in {Attempts} attempts!')
            break



def game_loop():
    while True:
        play_guessing_game()

        play_again = input('Would you like to play again? (yes/no): ').lower()
        if play_again == 'no':
            print('Quitting now')
            break

if __name__ == "__main__": 
    game_loop()




