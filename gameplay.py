import requests
from api import comp_sequence

#game play function
def game():
    attempt = 1
    guess_history = {}
    while attempt < 11:
        attempts_left = (10 - int(attempt))
        count = 0
        #obtain users guess
        num_a = input(f"\nAttempt #{attempt}. Please enter your first number.\n")
        num_b = input("\nPlease enter your second number.\n")
        num_c = input("\nPlease enter your third number.\n")
        num_d = input("\nPlease enter your fourth number.\n")
        #string to integer
        int_num_a = int(num_a)
        int_num_b = int(num_b)
        int_num_c = int(num_c)
        int_num_d = int(num_d)
        user_guess = num_a + num_b + num_c + num_d
    #confirming guess is within range
        if (int_num_a < 0 or int_num_a > 7) or (int_num_b < 0 or int_num_b > 7) or (int_num_c < 0 or int_num_c > 7) or (int_num_d < 0 or int_num_d > 7):
            print('Please enter valid guess. Guesses should be within the range of 0 to 7.')
        elif len(user_guess) != len(comp_sequence):
            print('Only four digits should have been selected.')
        else: 
            print(f'\nYour guess is {user_guess}')
            attempt += 1
            for i in range(4):
                if user_guess[i] == comp_sequence[i]:
                    count += 1
            if count == 4:
                play_game = False
                print(f'\n\nYou win! The secret code was {comp_sequence}. Great job!')
                break
    #print responses after attempt made that shows number correct and attempts left
            elif count == 1 and attempts_left == 1:
                print(f'\nYou have {count} number correct and {attempts_left} attempt left')
            elif count == 1 and attempts_left != 1:
                print(f'\nYou have {count} number correct and {attempts_left} attempts left')
            elif count != 1 and attempts_left == 1:
                print(f'\nYou have {count} numbers correct and {attempts_left} attempt left.')
            elif attempts_left == 0:
                print(f'\nYou ran out of attempts! The secret code was {comp_sequence}.')
            else:
                print(f'\nYou have {count} numbers correct and {attempts_left} attempts left.')
        while attempt <= 10:           
            guess_history[user_guess] = count
            view_history = input("\nWould you like to see your previous attempts and count of correct numbers? Press 'y' to view history or any key to continue \n").lower()
            if view_history == "y":
                print(guess_history)
            break

