import random as rng
from Character import player_class as player
from Character import enemy_class as enemy



print("\tWelcome to the very start of a grand adventure")
user_input = input("Enter a name, to go by: >")
string_name = str(user_input)
Player01 = player(string_name, 50, 3, 10)
Enemy01 = enemy("Basic Bandit Man", 15, 2, 25)
#print(Player01)
#print(Enemy01)
"""
event list:
1: Player met and be-friended Alys
2: Player ascended the grandstairs and made it to Juniper's Gate

"""
unique_events = {"event1" : 0, "event2" : 0, "event3" : 0, "event4" : 0} # make these 1 if they reach a "special event" so story can continue!

def set_event(event_num):
    if event_num == 1:
        unique_events["event1"] = 1
    elif event_num == 2:
        unique_events["event2"] = 1
    elif event_num == 3:
        unique_events["event3"] = 1
    elif event_num == 4:
        unique_events["event4"] = 1


def begin_battle(plr, enemy_count):
    enemy_list = []
    for i in range(enemy_count):
        new_enemy = enemy("Battle-hardened Bandit", 25, 2, 10)
        enemy_list.append(new_enemy)
    
    if len(enemy_list) > 1:
        countlist = len(enemy_list)
        #for id in range(countlist):
            #realcount = str(id+1)
            #enemy_text = "[" +realcount+ "] " + str(enemy_list[id])
            #print(enemy_text)
            #print(enemy_list[id])
        print(plr.name +  ", " + str(len(enemy_list)) + " enemies stand before you!")
    else:
        print("One enemy stands before you!")
    
    while (not plr.health <= 0 or plr.is_alive == True):
        dice_roll = rng.randint(0, 2)
        if dice_roll == 1:
            #enemy_stringlist = str(enemy_list)
            if len(enemy_list) > 1:
                countl = len(enemy_list)
                for id in range(countl):
                    realc = str(id+1)
                    enemy_text = "[" +realc+ "] " + str(enemy_list[id])
                    print(enemy_text)
            else:
                print("One enemy stands before you!")
            #
            minusentry = 0
            while True:
                try:
                    fight_input = input("\nWhich one do you choose [1] - [n\'th]") 
                    minusentry = int(fight_input) - 1
                    while (enemy_list[minusentry] not in enemy_list):
                        print("ENTER A REAL ENEMY ENTRY")
                    
                except ValueError:
                    continue

                else:
                    print("execute here?")
                    break
            
            #print(str(enemy_list[minusentry]) + " index: " + str(minusentry))
            """
            enemy_list[minusentry].take_damage(plr.damage, plr)
            if enemy_list[minusentry].health <= 0:
                print(f'{enemy_list[minusentry].name} has died, removing from table!')
                enemy_list.remove(minusentry)
            """
            
            
            #print(minusentry)
            enemy_list[minusentry].take_damage(plr.damage, plr)
            #player_turn, they get to choose which bandit to hurt
        elif dice_roll == 2:
            if plr.is_alive == False:
                break
            rand_bandit = rng.choice(enemy_list)
            plr.take_damage(rand_bandit.damage, rand_bandit)
            
            #enemy hurt

def hartokan_entry(plr): #beginning of game start
    print("\n" + plr.name + ", you awaken in a dense forest with strange geometrically angular rocks, you slowly rise from the ground, gathering your bearings.")

def junipers_entry(plr): #passed intro, middle of game
    print("\n" + plr.name + ", as you slowly ascend the many stairs, a dense murmur from beyond the gate can be heard. You reach the apex and before you is a grand door over twenty-stories high, it's a wonder how anybody could have constructed this gate.")

def grand_battle_entry(plr): #into the battle, end of game player will fight (3) fight(s)?
    print("\n" + plr.name + ", recovering from a tunnel vision of black, you are surrounded by your comrades in the center of the battlefield, face-to-face with your enemies. You see a young man who last week you considered a friend get quickly cut down in front of you before you ready your weapon, determined to make it out alive.")

    begin_battle(plr, 2)




def start_game(gamer):
    print("Every game needs a starting area for the main protagonist to originate from, which of these sound the most interesting?")
    #first_choice = (input("\nWhat is your choice\n[1]: Within the Hartokan Forest\n[2]: At Juniper's Gate\n[3]: In the midst of a grand battle\n>"))
    #print(type(first_choice))
    


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
        hartokan_entry(gamer)
    elif first_choice == 2:
        set_event(2)
        junipers_entry(gamer)
    elif first_choice == 3:
        grand_battle_entry(gamer)

start_game(Player01)



