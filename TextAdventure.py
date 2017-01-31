import time
from random import random

"""
 Text Adventure Notes:

  • Worse enemy every other rooms - Done
  • Damage of each is half their health if can be divided evenly, otherwise one less (ex: 20hp - 10atk, 25hp - 12atk) - Done

  • In shop can get better fork enchantments and health potions
  • Sword prices go up equivelant to enemies, and the last enemy you faced gives you the exact gold to get the next sword
  • Also, each sword has a damage equivelant to the damage of the enemy with the same health as it (ex: after stove w/ 10hp and 5atk u get 10gp and that buys a 5atk sword)
"""

# TODO import level 1
level1 = {
    "rooms": {
        "kitchen": {
            "name": "kitchen",
            "objects": ["chicken", "couch", "microwaved game console"],
            "description": "In this room there is a chicken, a couch, and a microwaved game console.",
            "exits": {
                "north": "living room",
                "east": "closet",
            },
            "enemy": {
                "name": "stove",
                "hitpoints": 10,
                "attack": 5,
                "coins": 10
            }
        },
        "living room": {
            "name": "living room",
            "description": "You better know what's in here, otherwise you're a geezer.",
            "objects": ["potato", "nothing"],
            "exits": {
                "south": "kitchen",
                "north": "mudville"
            },
        },
        "closet": {
            "name": "closet",
            "exits": {},
            "description": "There is no way out of the closet.",
            "objects": ["magic portal"],
            "enemy": {
                "name": "THE DREADED COAT HANGER",
                "hitpoints": 15,
                "attack": 7,
                "coins": 15
            }
        },
        "never never land": {
            "name": "never never land",
            "description": "What did you expect?",
            "exits": {
                "south": "closet",
                "north": "kitchen",
                "west": "closet",
                "east": "closet",
            }
        },
        "mudville": {
            "name": "mudville",
            "description": "Look at all that mud...",
            "objects": ["mud"],
            "exits": {
                "south": "living room",
                "west": "dining room"
            },
            "enemy": {
                "name": "Muddy Shoe",
                "hitpoints": 20,
                "attack": 10,
                "coins": 20
            }
        },
        "dining room": {
            "name": "dining room",
            "description": "Here you find an assortment of plates, forks, and water pitchers.",
            "objects": ["plates", "forks", "water pitchers"],
            "exits": {
                "east": "mudville",
                "south": "bathroom"
            }
        },
        "bathroom": {
            "name": "bathroom",
            "description": "There is nothing in this room you want. Unless you want a toilet seat.",
            "objects": ["toilet seat"],
            "exits": {
                "north": "dining room",
                "east": "nowhere"
            },
            "enemy": {
                "name": "Toilet",
                "hitpoints": 25,
                "attack": 12,
                "coins": 25
            }
        },
        "nowhere": {
            "name": "nowhere",
            "description": "There is no way out of the closet, so the only way out of nowhere is the closet.",
            "exits": {
                "west": "closet"
            }
        }
    },
}

player_status = {
    "health": 100,
    "items": ["knife"],
    "coins": 0,
    "old": False,
    "attack": 2,
}

current_room = level1["rooms"]["kitchen"]
game_status = "playing" # or "won" or "lost"

def print_exits():
    if len(current_room["exits"]) == 0:
        return
    print("The exits are:")
    for e in current_room["exits"]:
        print(e)
    print("")


def go_direction(direction):
    global current_room
    if direction in current_room["exits"]:
        room_name = current_room["exits"][direction] # living room
        current_room = level1["rooms"][room_name]
    else:
        print("Your head slams into the wall. You lose 5 health and are knocked out for 50 years.")
        time.sleep(5)
        print("\nYou wake up as an old dying geezer with the full capabilites and looks of your previous age... somehow.")
        player_status["old"] = True
        player_status["health"] -= 5


def check(get_input):
    global current_room, old, game_status
    cmd = get_input()
    print("")

    if cmd == "help":
        helpPage(get_input)
    elif cmd == "I am the king of the ivory throne!":
        current_room = level1["rooms"]["bathroom"]
    elif current_room == level1["rooms"]["closet"] and cmd == "shop":
        shop(get_input)
    elif cmd == "status":
        print("Health: " + str(player_status['health']))
        print("Items: " + str(", ".join(player_status["items"])))
        print("Coins: " + str(player_status["coins"]))
    elif cmd == "north":
        go_direction("north")
    elif cmd == "south":
        go_direction("south")
    elif cmd == "east":
        go_direction("east")
    elif cmd == "west":
        go_direction("west")
    elif cmd == "pick up":
        if "enemy" not in current_room:
            if current_room["objects"] == None:
                print("You can pick up NOTHING! YOU ARE DOOMED TO EAT CHEESE!")
            else:
                for i, obj in enumerate(current_room["objects"]):
                    print(str(i + 1) + ") ", obj)
                choice = get_input()

                if choice.isdigit():
                    choice_num = int(choice)
                    if choice_num <= len(current_room["objects"]):
                        player_status["items"].append(current_room["objects"][choice_num - 1])
                        current_room["objects"].remove(current_room["objects"][choice_num - 1])
                    else:
                        print("You can't pick that up silly!")
                else:
                    print("That's not a number you numberskull!")
        else:
            print("You are being attacked by furniture! Show some respect! Don't go picking up toilet seats or something like that when there is furniture present! It's quite disrespectful!")
    elif cmd == "use":
        if len(player_status["items"]) == 0:
            print("YOU HAVE NO ITEMS IN YOUR POTATO SACK. YOU ALSO HAVE NO HOPE!")
            print("After that extremely uplifting message by our sponsors, we would like to inform you of your insanity and demise.")
        else:
            for i, it in enumerate(player_status["items"]):
                print(str(i + 1) + ") ", it)
            choice = get_input()

            if choice.isdigit():
                choice_num = int(choice)
                if choice_num <= len(player_status["items"]):
                    item = player_status["items"][choice_num - 1] # "knife"
                    if item == "knife":
                        print("You cut your heart out by accident and die")
                        game_status = "lost"
                    elif item == "magic portal":
                        current_room = level1["rooms"]["never never land"]
                        print("You were transported to never never land")
                    elif item == "microwaved game console":
                        print("You get electricuted and die")
                        game_status = "lost"
                    elif item == "chicken":
                        print("The chicken lays an egg. You eat it and get salminila.")
                        game_status = "lost"
                    elif item == "couch":
                        if player_status["old"] == True:
                            print("You are no longer internally an old geezer!")
                        else:
                            print("Achievment Unlocked: Laziness")
                    elif item == "mud":
                        print("You throw a nice, big, glob of mud. Nice job.")
                        # TODO make it slow down enemies
                    elif item == "nothing":
                        print("Nothing happens.")
                    elif item == "plates":
                        print("The stack of plates falls to the floor and shatters. Given the way I made this game, it is surprising that you managed to override my code and be unhurt. I'll have to fix that bug soon.")
                    elif item == "forks":
                        print("All of the forks except one are swept away by a sudden breeze. You then use the one to make a stabbing motion.")
                        if "enemy" in current_room:
                            print("\nYou hit the " + current_room["enemy"]["name"] + "!")
                            current_room["enemy"]["hitpoints"] -= player_status["attack"]
                            print("It is now at " + str(current_room["enemy"]["hitpoints"]) + " health.")
                            if current_room["enemy"]["hitpoints"] <= 0:
                                player_status["coins"] += current_room["enemy"]["coins"]
                                del current_room["enemy"]
                                print("Enemy defeated! You get 10 gold!")
                    elif item == "water pitchers":
                        print("The many water pitchers fall to the floor and crash causing extreme injury and death. You die.")
                        game_status = "lost"
                    elif item == "toilet seat":
                        print("You stop to wonder why you ever wanted this. You throw it out the window. Your spider sense tingles. Something has changed.")
                        player_status["items"].remove("toilet seat")
                        level1["rooms"]["bathroom"]["objects"].append("treasure chest")
                    elif item == "treasure chest":
                        print("You open up the chest and find a ton of gold. You find a button inside the chest as well.")
                        player_status["items"].append("button")
                        player_status["coins"] += 1000000000000
                    elif item == "button":
                        game_status = "won"
                    else:
                        print("Umm I can't use that yet. go bug Mark to fix the game")
                else:
                    print("You can't pick that up silly!")
            else:
                print("That's not a number you numberskull!")
    else:
        print("We did not recognize your command. Please try again.")

def enemy_attacks():
    global game_status
    if "enemy" in current_room:
        chance = random()
        if chance <= 0.7:
            print("The " + current_room["enemy"]["name"] + " hit you")
            player_status["health"] -= current_room["enemy"]["attack"]
            if player_status["health"] <= 0:
                player_status["health"] = 0
                game_status = "lost"
            print("You are at " + str(player_status["health"]) + " health.")
        else:
            print("The " + current_room["enemy"]["name"] + " missed. Furniture these days is getting worse and worse :(")

def helpPage(get_input):
    print("Your commands are 'status', 'north', 'south', 'east', 'west', 'use', and 'pick up'. You can also type 'help' at any time to view this again.\n")
    check(get_input)

def item_definition(i, it, in_between_phrase):
    if "damage" in it:
        print(str(i + 1) + ") ", it["name"], "-", in_between_phrase, it["damage"], "-", "cost:", it["cost"])
    else:
        print(str(i + 1) + ") ", it["name"], "-", in_between_phrase, it["healing"], "-", "cost:", it["cost"])


def drink(item):
    if not item:
        print("There's nothing here")
    elif "healing" not in item and item:
        print("You can't drink that!")
    else:
        player_status["health"] += item["healing"]

def shop(get_input):
    shop_items = [
        {
            "name": "ice enchantment",
            "cost": 10,
            "damage": 5,
            "type": "weapon"
        },
        {
            "name": "sandstone sharpening",
            "cost": 15,
            "damage": 7,
            "type": "weapon"
        },
        {
            "name": "draconic bestowment",
            "cost": 20,
            "damage": 10,
            "type": "weapon"
        },
        {
            "name": "spearmint",
            "cost": 25,
            "damage": 12,
            "type": "weapon"
        },
        {
            "name": "health potion",
            "cost": 15,
            "type": "potion",
            "healing": 25
        }
    ]

    print("Hello and welcome to the shop! Here you may buy exquisitely non exquisite enchantments given as they all do the same thing. Except slightly different.\n")
    print("Here are the items:")
    for i, it in enumerate(shop_items):
        if it["type"] == "weapon":
            item_definition(i, it, "raises damage to")
        else:
            item_definition(i, it, "raises health by")
    choice = get_input()

    if choice.isdigit():
        choice_num = int(choice)
        if choice_num <= len(shop_items):
            # TODO make item more readable w/o glitches
            # Also make it usable
            player_status["items"].append(shop_items[choice_num - 1])
            player_status["coins"] -= it["cost"]
        else:
            print("You can't buy that silly!")
    else:
        print("That's not a number you numberskull!")

def default_get_input():
    return input('>>> ')

TEST_INPUTS = [
    'I am the king of the ivory throne!',
    'north',
    'pick up',
    '2',
    'east',
    'south',
    'south',
    'george',
    'use',
    '1'
]

def test_get_input():
    if len(TEST_INPUTS):
        next_item = TEST_INPUTS[0] # get the first thing in the list
        print("<<TEST INPUT>>", next_item)
        TEST_INPUTS.pop(0) # remove the first thing
        return next_item
    else:
        return default_get_input()


def gameLoop(get_input):
    global game_status
    print("\nYou are in the " + current_room["name"] + ". " + current_room["description"])
    print_exits()
    enemy_attacks()
    try:
        if game_status == "playing":
            check(get_input)
    except KeyboardInterrupt:
        game_status = "lost"

    if game_status == "playing":
        gameLoop(get_input)
    elif game_status == "won":
        print("YOU WON!!! Imagine digital confetti showering over you.")
    elif game_status == "lost":
        print("Awwwww. You lost. Imagine a digital rotten tomato hitting you in the face.")
    else:
        pass

import sys
get_input = None
if len(sys.argv) > 1 and sys.argv[1] == "test":
    get_input = test_get_input
else:
    get_input = default_get_input
helpPage(get_input)
gameLoop(get_input)
