# imports and global variables
import random 
USER_CHOISES=('roke','paper','scissor')


# create function get user input


def get_user_input():
    choice=input("pick your choice ['roke','paper','scissor']:")

    while choice not in USER_CHOISES:
        choice=input("pick your choice ['roke','paper','scissor']:")
    return choice

# create function for get pc innput

def get_pc_input():
    return random.choice(USER_CHOISES)


# compare and determine whitch is the winner

def determine_winner(user_input,pc_input):
    print(f'user:{user_input} and pc:{pc_input}')
    if user_input==pc_input:
        return "DRAW!"
    if user_input=="roke":
        if pc_input=="paper":
            return "PC"
        else:
            return "USER"
    if user_input=="paper":
        if pc_input=="roke":
            return "USER"
        else:
            return "PC"
    if user_input=="scissor":
        if pc_input=="roke":
            return "PC"
        else:
            return "USER"
        


# بهینه تر
def determine_winner_2(user_input,pc_input):
    print(f'user:{user_input} and pc:{pc_input}')
    wins={'roke':'scissor',
          'paper':'roke',
          'scissor':'paper'
          }
    if user_input==pc_input:
        return "DRAW!"
    if wins[user_input]==pc_input:
        return 'USER'
    else:
        return 'PC'




def main():
    user_input=get_user_input()
    pc_input=get_pc_input()
    res=determine_winner_2(user_input,pc_input)
    print(res)

answer='y'
while answer=="y":
    main()
    answer=input('do you want to continue?(y/n)')

# cretae a main function as the runner



# make an iteration 