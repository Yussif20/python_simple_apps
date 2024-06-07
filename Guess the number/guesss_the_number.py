import random

attempts_list =[]
attempts=0
random_num=random.randint(1,10)
print(random_num)

def show_score():
    if not attempts_list:
        print("there is no currently a high score")
    else: print (f"the current high score is {min(attempts_list)} attempts")
def attempts_increment():
     global attempts
     attempts = attempts + 1
     attempts_list.append(attempts)

print('Hello champ, welcome to the guessing game')
player_name=input("What's your name ? ")
wanna_play = input(f'Hi {player_name},would you like to play the game? (yes/no) ').lower()

if wanna_play == "yes":
    print("cool")
    while wanna_play=="yes":
        guess=int(input("please choose a number between 1 and 10: "))
        if (guess < 1 or guess > 10):
            raise ValueError("please enter a number within the given range")
        else :
            if guess == random_num:    
                print("Great! you Won")
                attempts_increment()
                show_score()
                break
            else : 
                print("wrong, guess again")
                attempts_increment()
    exit()
else: show_score()


   
