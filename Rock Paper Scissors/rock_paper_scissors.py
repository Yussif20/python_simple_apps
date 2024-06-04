import random 

# Start the game
print( "Welcome to Rock Paper Scissors game!")

# Get the player choice and validate it
user= input("Choose your move ('r', 'p' or 's'): ")
if user!="r" and user!="p" and user!="s":
    print("Invalid input")
    exit()

# generate the pc choice randomly
pc=random.choice(["r", "p", "s"])

# Print the results
print("You chose " + user + " rand the pc chose " + pc)
if user==pc: print("it's a tie")
elif user=="r" and pc=="s" or user == "s" and pc == "p" or user=="p" and pc == "r" :
     print("You won!")
else :print("You lost!")