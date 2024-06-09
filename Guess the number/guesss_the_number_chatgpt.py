import random

def play_game(player_name):
    attempts_list = []
    attempts = 0
    random_num = random.randint(1, 10)

    def show_score():
        if not attempts_list:
            print("There is no current high score.")
        else:
            print(f"The current high score is {min(attempts_list)} attempts.")

    print('Hello champ, welcome to the guessing game!')
    print(f'Hi {player_name}, would you like to play the game? (yes/no) ')

    wanna_play = input().lower()

    if wanna_play == "no":
        print("Cool.")
        return
    else:
        show_score()

    while wanna_play.lower() == "yes":
        try:
            guess = int(input("Please choose a number between 1 and 10: "))

            if guess < 1 or guess > 10:
                raise ValueError("Please enter a number within the given range.")

            elif guess == random_num:
                print("Great! You Won!")
                attempts += 1
                attempts_list.append(attempts)
                print(f'It took you {attempts} attempts.')
                wanna_play = input("Would you like to play again? (yes/no) ").lower()

                if wanna_play.lower() == "no":
                    print("Cool, have a nice day!")
                    return
                else:
                    attempts = 0
                    show_score()
                    random_num = random.randint(1, 10)
                    continue

            elif guess < random_num:
                attempts += 1
                print("Wrong, try higher.")

            else:
                attempts += 1
                print("Wrong, try lower.")

        except ValueError as err:
            print(err)