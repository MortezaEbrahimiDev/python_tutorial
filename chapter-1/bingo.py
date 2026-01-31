# inports and variables

import random

MAX_NUM=10
MIN_NUM=1


# generate a random number

def generaete_random_number():
    return random.randint(MIN_NUM,MAX_NUM)

# get user input
def get_user_input():
    print(f'the number is between {MIN_NUM} and {MAX_NUM}')
    while True:
        try:
            user_input=int(input('enter your number:'))
        except ValueError:
            print('enter a valid number')
        else:
            return user_input

# check guessed number

def check_guessed_number(user_input,random_number):
    return user_input==random_number

# main function

def main():
    random_number= generaete_random_number()
    max_guess_count=3
    while max_guess_count>0:
        user_input=get_user_input()
        if check_guessed_number(user_input,random_number):
            print("\033[92mSuccess!!!")
            break
        max_guess_count-=1
    else:
        print(f'you can not guessed the number')


if __name__=="__main__":
    main()