import os
import random as rng
import time 
from Character import player_class as player
from Character import enemy_class as enemy


os.system("cls")
print("\t\t\t\t\tWelcome to the very start of a grand adventure")
user_input = input("Enter a name, to go by: >")
string_name = str(user_input)
Player01 = player(string_name, 50, 3, 10)
Enemy01 = enemy("Basic Bandit Man", 15, 2, 25)
#print(Player01)
#print(Enemy01)
"""
event list:
1: Player met and be-friended Alys
2: Player ascended the grandstairs and made it to Juniper's Gate;
    2a: Meet Alys' friend, who already knows you.
    2b: Alys does not know you and so when you meet her friend, its cordial and short.
3: Player is asked to assist in the battlefield:
    3a: Alys' friend is alongside you and you get more dialog into how Alys talks about the Player
    3b: You head into the battlefield, ready for a fight, lone-wolf style.

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


def choose_input(event_message, inp1 = None, inp2 = None, inp3 = None, inp4 = None):
    input_list =  []
    
    if inp1 != None:
            input_list.append(inp1)
    if inp2 != None:
            input_list.append(inp2)
    if inp3 != None:
            input_list.append(inp3)
    if inp4 != None:
            input_list.append(inp4)
            
    print('\n'+event_message+'\n')

    def display_list_info():
        for v in range(len(input_list)):
            print(f"[{v+1}]: {input_list[v]}")
    
    while True:

        try:
            display_list_info()
            user_inp = input("Enter: >")
            num_find = int(user_inp) - 1
            while (input_list[num_find] not in input_list):#(num_find > len(input_list) - 1 or num_find < 1 ):
                print('\n')
                display_list_info()
                print("\nEnter a real entry number")
                user_inp = input("Enter: >")
                num_find = int(user_inp) - 1

        except ValueError:
            print('\n')
            display_list_info()
            print("\nEnter a real entry number, not a string!")
            continue
        else:
            print(num_find)
            break
    
    return int(num_find)
    


def begin_battle(plr, enemy_count, enemy_name = "Bandit", enemy_health = 10, enemy_damage = 2, enemy_gold = 2):
    print("BATTLE BEGIN")
    time.sleep(0.85)
    enemy_list = []
    for i in range(enemy_count):
        new_enemy = enemy(enemy_name, enemy_health, enemy_damage, enemy_gold)
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
    
    while (not plr.health <= 0 or plr.is_alive == True ):
        if len(enemy_list) == 0:
            print("Battle over!")
            print("Player's stats:")
            print(plr)
            input("Enter to Continue!")
            break
        dice_roll = rng.randint(0, 2)
        if dice_roll == 1:
            #enemy_stringlist = str(enemy_list)
            if len(enemy_list) > 1:
                countl = len(enemy_list)
                for id in range(countl):
                    time.sleep(0.0015)
                    realc = str(id+1)
                    enemy_text = "[" +realc+ "] " + str(enemy_list[id])
                    print(enemy_text)
            else:
                print("[1] Enemy: " + str(enemy_list[0]))
            #
            minusentry = None
            while True:
                try:
                    print(f"-----------------------------------------------------------------\nPlayer HP: {plr.start_health} / {plr.health}\n-----------------------------------------------------------------")
                    fight_input = input("\nWhich one do you choose [1] - [n\'th]\n>") 
                    print("-------------------------------------------------------------")
                    minusentry = int(fight_input) - 1
                    while ((minusentry > len(enemy_list) - 1)):
                        print(f"Player HP: {plr.start_health} / {plr.health}")
                        print("[[[Enter an enemy number in the list!]]]")
                        if len(enemy_list) > 1:
                            countl = len(enemy_list)
                            for id in range(countl):
                                time.sleep(0.0015)
                                realc = str(id+1)
                                enemy_text = "[" + realc + "] " + str(enemy_list[id])
                                print(enemy_text)
                        else:
                            print(f"Player HP: {plr.start_health} / {plr.health}")
                            print("[1] Enemy: " + str(enemy_list[0]))
                        
                        fight_input = input("\nWhich one do you choose [1] - [n\'th]\n> ")
                        print("-------------------------------------------------------------") 
                        minusentry = int(fight_input) - 1
                    
                except ValueError:
                    print("[[[Please, input a number within the range given, no string entries!]]]\n")
                    if len(enemy_list) > 1:
                        countl = len(enemy_list)
                        for id in range(countl):
                            time.sleep(0.0015)
                            realc = str(id+1)
                            enemy_text = "[" + realc + "] " + str(enemy_list[id])
                            print(enemy_text)
                        else:
                            print(f"Player HP: {plr.start_health} / {plr.health}")
                            print("[1] Enemy: " + str(enemy_list[0]))
                    continue

                else:
                    #print("execute here?")
                    
                    break
            
            print(str(enemy_list[minusentry]) + " index: " + str(minusentry))
            rolled_dmg = rng.randint(plr.damage, plr.damage + 2)
            if rolled_dmg != plr.damage:
                print("Critical hit!")
            
            enemy_list[minusentry].take_damage(rolled_dmg, plr)
            
            if enemy_list[minusentry].is_alive == False:
                print(f'{enemy_list[minusentry].name} has died, removing from table!')
                enemy_list.remove(enemy_list[minusentry])
            
                
        


            


            
            

            #enemy_list[minusentry].take_damage(plr.damage, plr)
            #player_turn, they get to choose which bandit to hurt
        elif dice_roll == 2:
            print("-------------------------------------------------------------")
            print("\tvvvvENEMY TURN\tENEMY TURN\tENEMY TURNvvvv")
            time.sleep(0.255)
            if plr.is_alive == False:
                break
            rand_bandit = rng.choice(enemy_list)
            plr.take_damage(rand_bandit.damage, rand_bandit)
            print("\t^^^^ENEMY TURN\tENEMY TURN\tENEMY TURN^^^^")
            print("-------------------------------------------------------------")
            print()
            #input("Press enter to advance\n")
            
            #enemy hurt


def junipers_entry(plr): #passed intro, middle of game
    print("\n" + plr.name + ", as you slowly ascend the many stairs, a dense murmur from beyond the gate can be heard. You reach the apex and before you is a grand door over twenty-stories high, it's a wonder how anybody could have constructed this gate.")
    input("Enter to Continue")
    if unique_events["event1"] == 0:
        print("\nYou spot a smaller doorway where others are congregated, going through in single-file.\nYou join the others in the line and are allowed access into the Grand City.")
    else:
        print("\nYou see a small doorway where many are gathered, slowly gaining access to the city one by one.\nWhile admiring the grandness of Juniper's Gate, Alys quickly tells one of her friends Irmin about you, pointing and laughing before going into the city. Irmin quickly nudges you. He is adorned in guard gear and wields quite the weapon, it has its fair share of scratches and nicks but it's clearly been useful.\nIrmin's face lights up brightly with a toothy grin, 'Any friend of Alys' is a friend of mine, I can expedite your entry if you would follow me!'")
    print("The grand scale of the city's walls and gate were no joke, the city is dense but there are a few areas where people are condensed in.")
    place_find = choose_input("Where do you decide to go?", "Armitage Family's Alchemic Shop", "The Barracks", "Armor and Swords")
    if place_find == 0:
        print("You head toward the alchemy shop.") ##check if they have event1 == 1 or 0
    elif place_find == 1:
        print("You head towards the barracks") ## check if they have event2 == 1 or 0
    elif place_find == 2:
        print("You head towards the shop")
    

def grand_battle_entry(plr): #into the battle, end of game player will fight (3) fight(s)?
    print("\n" + plr.name + ", recovering from a tunnel vision of black, you are surrounded by your comrades in the center of the battlefield, face-to-face with your enemies. You see a young man who last week you considered a friend get quickly cut down in front of you before you ready your weapon, determined to make it out alive.")

    begin_battle(plr, 2, "Battle-hardened Bandit", 12, 2, 24)
    print("After slaying those bandits four more head towards you!")
    begin_battle(plr, 4)



##each story_start requires 3 choices!
def hartokan_entry(plr): #beginning of game start
    print("\n" + plr.name + ", you awaken in a dense forest with strange geometrically angular rocks, you slowly rise from the ground, gathering your bearings, you find a rusted, chipped sword, it has clearly had its uses..")
    choice_01 = choose_input("After gaining yourself, there is a well-walked path to your left and a slightly less interacted path to your right.", "Left pathway", "Right pathway")
    if choice_01 == 0: ##player will not meet Alys
        print("You take the Left pathway\nWalking through the forest you take in the green scenery and uniquely shaped rocks that encompass the area.\nOut of no-where, you hear a deathly, bloodcurdling screeching sound coming a couple feet behind you.\nMultiple fast, frantic, heavy footsteps approach you at high-speeds, something is coming to you.\nYou ready yourself.")
        begin_battle(plr, 3, "Hartokan Native Wolf", 6, 1, 4)
        print("\n'Simply amazing, we could use your skills in the battlefield!' a gruff voice calls out.\nYou whip your head up from the last wolf's corpse and spot a unit of a man. Wielding a greatsword resting on his shoulder, a big man looks down upon you.\n'The name's Tyr and I could use somebody like you, follow me. No questions.' the man tells you.")
        input("Enter to Continue!")
        print("After what seemed like forever, you and Tyr make it out of the forest and in view of a grand staircase that leads up to a massive gate.\n'That is Juniper's Gate, the only thing holding the abyssal demons and other kingdoms from raiding the 'greatest city' to ever be constructed.' Tyr quickly tells you before walking up the steps.")
        junipers_entry(plr)

    elif choice_01 == 1: ##player meets Alys, Tyr's daughter
        print("You take a second look at the Left pathway before taking the less beaten path.\nIt is unnerving to you, however you press on through the denser grove ahead of you.\nYou stumble across another person travelling the less beaten path not too far ahead of you.\nThey look toward you and raise an arm to beckon you to come toward them.")
        print("\nAfter a brisk walk, you make it to the other person, its a young woman.\nShe has reading glasses, messy hair, and its as if she's been in the forest for days.\n'I don't recognize you, are you from here or just coming through?' she asks you.")
        choice_02 = choose_input("What is your choice?", "State your name", "Ignore her")

        if choice_02 == 0:
            print(f"You state, 'I go by {plr.name}, nice to meet you, what's your name?'\nShe quickly sizes you up before she says, 'My name is Alys and I work for my father's alchemic shop, he sent me here to gather some herbs for him, if you wouldn't mind would you help me in finding them?'")
            choice_03 = choose_input("Do you help or not?", "Yes", "No")
            if choice_03 == 0:
                print(f'Alys\'s eyes light up brightly before she clasps her hands together and says, "Okay, he wants me to gather some Hartokan Lomas, they are multi-colored, very difficult to miss one since they stand out against the constant green."')
                set_event(1)
                print(f'After what seems like hours staring at similar looking scenery, you spot a small grove of Hartokan Lomas and pick them up.') 
                input("Enter to Continue!")
                print('Out of nowhere comes out two Treants, natural guardians of Hartokan Forest.')
                
                begin_battle(plr, 2, "Hartokan Treant", 15, 3, 25)
                print(f'"I saw you handle yourself against those two treants, I would\'ve been scared stiff," Alys tells you.\nShe looks at your pocket and notices you have the Lomas before she says, "And I believe we are done here, you can follow me to Juniper\'s Gate so we can get into the city!"\nThe two of you begin to make your way towards the entrance of the forest.')
                input("Enter to Continue!")
                print(f'After 20 minutes of walking through the forest you both finally make it out and before you lay an empty plain with what seemingly is a grand staircase leading up to a very large gate.\nAlys lets you know, "This is Juniper\'s Gate, first time outside the city I was mezmerized by its sheer size, like how could humans construct such a grand structure,"')
                input("Enter to Continue!")
                junipers_entry(plr)


            elif choice_03 == 1:
                print(f'Alys looks a bit dejected but says, "Yeah I understand, it\'s a bit odd of me to ask a stranger to help simply look for some plants, see you around {plr.name}!"\nAlys walks toward the entrance of the path, you quickly spy she has at least one flower.')
                input("Enter to Continue!")
                print("You decide its a great time to leave the forest and so you do so.")
                input("Enter to Continue!")
                print("Right before you make it to the exit of the forest, four men step out of the shrubs, weapons drawn and crazed looks on their faces.")
                begin_battle(plr, 4)
                print("After the last man is defeated, you immediately make your way toward the massive staircase that the path from the forest leads to.")
                junipers_entry(plr)




        elif choice_02 == 1:
            print(f'You blankly stare at the young woman for a solid minute, awkawrdly weirding her out and causing her to brush you off and head toward the entrance where you awoke.\nYou press on through the grove, not thinking for another second about the non-interaction.')
            input("Enter to Continue!")
            print("You decide its a great time to leave the forest and so you do so.")
            input("Enter to Continue!")
            print("Right before you make it to the exit of the forest, four men step out of the shrubs, weapons drawn and crazed looks on their faces.")
            begin_battle(plr, 4)
            print("After the last man is defeated, you immediately make your way toward the massive staircase that the path from the forest leads to.")
            junipers_entry(plr)








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
        junipers_entry(gamer)
    elif first_choice == 3:
        grand_battle_entry(gamer)

start_game(Player01)



