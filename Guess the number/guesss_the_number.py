import random

attempts_list =[]
attempts=0
random_num=random.randint(1,10)

def show_score():
    if not attempts_list:
        print("there is no currently a high score")
    else: print (f"the current high score is {min(attempts_list)} attempts")

print('Hello champ, welcome to the guessing game')
player_name=input("What's your name ? ")
wanna_play = input(f'Hi {player_name},would you like to play the game? (yes/no) ').lower()

if wanna_play == "no":
    print("cool")
    exit()
else: show_score()

while wanna_play=="yes":
        try:
            guess=int(input("please choose a number between 1 and 10: "))
            if (guess < 1 or guess > 10):
                raise ValueError("please enter a number within the given range")
            elif guess == random_num:   
                    print("Great! you Won")
                    # attempts_increment()
                    attempts = attempts + 1
                    attempts_list.append(attempts)
                    print(f'it took you {attempts} attempts')
                    wanna_play=input("would you like to play again? (yes/no)").lower()
                    if wanna_play=="no":
                        print("cool, have a nice day")
                    else :
                        attempts = 0
                        show_score()
                        random_num=random.randint(1,10)
                        continue
            elif guess < random_num : 
                    attempts = attempts + 1
                    print("wrong, try higher")
                    # attempts_increment()
            else : 
                    attempts = attempts + 1
                    print("wrong, try lower")
        except ValueError as err:
            print(err)



   
