import random

outcomes_dict = { 'rock': 'scissors',
                  'paper': 'rock',
                  'scissors': 'paper'  
                }

player_wins = 0
comp_wins = 0
draw = 0

def input_your_selection():
    while True:
        choice = input('Choose: [1] rock, [2] paper or [3] scissors: ')
        #you can input entire selected word
        if choice.lower() in outcomes_dict:
            return choice.lower()
        #or just number 
        try:
            choice = int(choice)
        except:
            continue
        #if number exists in this dict below, then return your choice
        if (int_choice := {1: 'rock', 2: 'paper', 3: 'scissors'}).get(int(choice)):
            return int_choice[ choice ]

def it_is_time_for_end_the_game():
    while True:
        choice = input('Do You want to play again? [Y/N]')
        if choice.lower() in ['n', 'no']:
            return True
        elif choice.lower() in ['y', 'yes']:
            return False

def s_just_for_a_better_look( variable ):
    return  's.' if variable != 1 else '.'

while True:
    #player's choice
    player_choice = input_your_selection()
  
    #Get comp choice
    comp_choice = random.choice( list(outcomes_dict.keys()) )
  
    #Print players choice
    print('[PLAYER] '+player_choice.upper()+' versus '+comp_choice.upper()+' [CPU]')
  
    #compute who wins
    if player_choice in outcomes_dict[comp_choice]:
        print('CPU won this round!')
        comp_wins += 1
    elif comp_choice in outcomes_dict[player_choice]:
        print('You won this round!')
        player_wins += 1
    else:
        print('Draw! (nobody win)')
        draw += 1
      
    #Ask for next round
    if it_is_time_for_end_the_game():
        #If player don't want to play again, show the result
        print('Player won '+str(player_wins)+' time' + s_just_for_a_better_look( player_wins ) )
        print('Computer won '+str(comp_wins)+' time' + s_just_for_a_better_look( comp_wins ) )
        print(str(draw)+' draw' + s_just_for_a_better_look( draw ))
        break
