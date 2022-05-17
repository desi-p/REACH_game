#select random number range 0-7
#select 4 integer from range
#user guesses 4 integers
#response with correct 

from gameplay import game

play_game = True

#get user name
user_name = input("Welcome to Mastermind! What is your name? ")
print(f"\nWelcome {user_name}!\n\n")

#print instructions
print("The computer will select a random code (made of 4 integers ranging from 0 - 7). Numbers may be repeated. You will have 8 attempts to crack the code! Think you can do it?\n\nLet's go!\n\n")


#loop for game play
while play_game is True:
    game()

    repeat_game = input(f"\n\n{user_name}, would you like to play again? Y or N\n").lower()
    if repeat_game == "y":
        print(f"\nAwesome, {user_name}. Try to guess the secret code before you run out of attempts!")
        play_game = True
    elif repeat_game == "n":
        print(f"\nThank you {user_name} for playing Mastermind.")
        exit()
    else: 
        print("\nPlease select valid option.")

