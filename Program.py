from random import random as rng
from Character import player_class as player
from Character import enemy_class as enemy



print("\tWelcome to the very start of a grand adventure")
user_input = input("Enter a name, to go by: >")
string_name = str(user_input)
Player01 = player(string_name, 25, 1, 10)
Enemy01 = enemy("Basic Bandit Man", 15, 2, 25)
#print(Player01)
#print(Enemy01)

unique_events = [0, 0, 0, 0, 0] # make these 1 if they reach a "special event" so story can continue!



def start_game(gamer):
    print("Every game needs a starting area for the main protagonist to originate from, which of these sound the most interesting?")
    first_choice = (input("\nWhat is your choice\n[1]: Within the Hartokan Forest\n[2]: At Juniper's Gate\n[3]: In the midst of a grand battle\n>"))
    print(type(first_choice))
    


    while (True):
        try:
            first_choice = int(input("\nWhat is your choice\n[1]: Within the Hartokan Forest\n[2]: At Juniper's Gate\n[3]: In the midst of a grand battle\n>"))
            while (first_choice > 3 or first_choice < 1):
                first_choice = int(input("\nWhat is your choice\n[1]: Within the Hartokan Forest\n[2]: At Juniper's Gate\n[3]: In the midst of a grand battle\n>"))
        except (ValueError):
            print("Not an integer, try again.")
            continue
        else:
            #correct entry is an int
            break
       
    if first_choice == 1:
        pass
    elif first_choice == 2:
        pass
    elif first_choice == 3:
        pass

start_game(Player01)



