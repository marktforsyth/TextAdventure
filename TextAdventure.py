import time
from random import random
from Level1 import level1

current_room = level1["rooms"]["kitchen"]
game_status = "playing" # or "won" or "lost"

player_status = {
    "health": 100,
    "items": [
        {
            "name": "knife",
            "description": "You cut your heart out by accident and die"
        }
    ],
    "coins": 0,
    "old": False,
    "attack": 2,
}

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

def find_tool_in_pack(item):
    global result
    items = player_status["items"]
    resultlist = [d    for d in items     if d.get('name', '') == item]
    result = resultlist[0]


def check(get_input):
    global current_room, old, game_status
    cmd = get_input()
    print("")

    if cmd == "help":
        helpPage(get_input)
    elif cmd == "drink":
        drink()
    elif cmd == "I am the king of the ivory throne!":
        current_room = level1["rooms"]["bathroom"]
    elif current_room == level1["rooms"]["closet"] and cmd == "shop":
        shop(get_input)
    elif cmd == "status":
        print("Health: " + str(player_status['health']))
        #print("Items: " + player_status["items"]["name"])
        print("Items: ", end="")
        first = True
        for num, i in enumerate(player_status["items"]):
            if num == len(player_status["items"]) - 1:
                print(i["name"])
            else:
                print(i["name"], end=", ")
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
        if "enemy" not in current_room or current_room["enemy"]["muddy_turns"] > 0:
            if current_room["objects"] == None:
                print("You can pick up NOTHING! YOU ARE DOOMED TO EAT CHEESE!")
            else:
                for i, obj in enumerate(current_room["objects"]):
                    print(str(i + 1) + ") ", obj["name"])
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
                print(str(i + 1) + ") ", it["name"])
            choice = get_input()

            if choice.isdigit():
                choice_num = int(choice)
                global result
                if choice_num <= len(player_status["items"]):
                    item = player_status["items"][choice_num - 1] # "knife"
                    if item["name"] == "knife":
                        find_tool_in_pack("knife")
                        print(result["description"])
                        game_status = "lost"
                    elif item["name"] == "magic portal":
                        find_tool_in_pack("magic portal")
                        current_room = level1["rooms"]["never never land"]
                        print(result["description"])
                    elif item["name"] == "microwaved game console":
                        find_tool_in_pack("microwaved game console")
                        print(result["description"])
                        game_status = "lost"
                    elif item["name"] == "chicken":
                        find_tool_in_pack("chicken")
                        print(result["description"])
                        game_status = "lost"
                    elif item["name"] == "couch":
                        find_tool_in_pack("couch")
                        if player_status["old"] == True:
                            print("You are no longer internally an old geezer!")
                        else:
                            print(result["description"])
                    elif item["name"] == "mud":
                        find_tool_in_pack("mud")
                        print(result["description"])
                        if "enemy" in current_room:
                            if "Muddy Shoe" == current_room["enemy"]["name"]:
                                print("The Muddy Shoe laughs at your patehtic attempt to use its natural element.")
                            else:
                                current_room["enemy"]["muddy_turns"] = 2
                                print("The " + current_room["enemy"]["name"] + " is now covered in mud! Quick, make your escape!")

                    elif item["name"] == "nothing":
                        find_tool_in_pack("nothing")
                        print(result["description"])
                    elif item["name"] == "plates":
                        find_tool_in_pack("plates")
                        print(result["description"])
                    elif item["name"] == "forks":
                        find_tool_in_pack("forks")
                        print(result["description"])
                        if "enemy" in current_room:
                            print("\nYou hit the " + current_room["enemy"]["name"] + "!")
                            current_room["enemy"]["hitpoints"] -= player_status["attack"]
                            print("It is now at " + str(current_room["enemy"]["hitpoints"]) + " health.")
                            if current_room["enemy"]["hitpoints"] <= 0:
                                player_status["coins"] += current_room["enemy"]["coins"]
                                del current_room["enemy"]
                                print("Enemy defeated! You now have " + str(player_status["coins"]) + " gold!")
                    elif item["name"] == "water pitchers":
                        find_tool_in_pack("water pitchers")
                        print(result["description"])
                        game_status = "lost"
                    elif item["name"] == "toilet seat":
                        find_tool_in_pack("toilet seat")
                        print(result["description"])
                        player_status["items"].remove(result)
                        level1["rooms"]["bathroom"]["objects"].update({{"name": "treasure chest", "description": "You open up the chest and find a ton of gold. You find a button inside the chest as well."}})
                    elif item["name"] == "treasure chest":
                        find_tool_in_pack("treasure chest")
                        print(result["description"])
                        player_status["items"].append({"button": {"name": "button"}})
                        player_status["coins"] += 1000000000000
                    elif item["name"] == "button":
                        game_status = "won"
                    elif item["name"] == "potato":
                        find_tool_in_pack("potato")
                        print(result["description"])
                        player_status["items"].remove(result)
                    elif item["name"] == "ice enchantment":
                        find_tool_in_pack("ice enchantment")
                        player_status["attack"] += result["damage"]
                        player_status["items"].remove(result)
                    elif item["name"] == "sandstone sharpening":
                        find_tool_in_pack("sandstone sharpening")
                        player_status["attack"] += result["damage"]
                        player_status["items"].remove(result)
                    elif item["name"] == "draconic bestowment":
                        find_tool_in_pack("draconic bestowment")
                        player_status["attack"] += result["damage"]
                        player_status["items"].remove(result)
                    elif item["name"] == "spearmint":
                        find_tool_in_pack("spearmint")
                        player_status["attack"] += result["damage"]
                        player_status["items"].remove(result)
                    elif item["name"] == "health potion":
                        print("You can't use this, you have to drink it!")
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
        if current_room["enemy"]["muddy_turns"] > 0:
            current_room["enemy"]["muddy_turns"] -= 1
            print("The " + current_room["enemy"]["name"] + " is covered in mud. Onlooking peasants laugh at it")
        elif chance <= 0.7:
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


def drink():
    #TODO make this work
    drinkables = {}
    for i in player_status["items"]:
        if "healing" in i:
            drinkables.update(i)

    for i, it in enumerate(drinkables):
        print(str(i + 1) + ") " + it["name"])
    choice = get_input()

    if choice.isdigit():
        choice_num = int(choice)
        if choice_num <= len(drinkables):
            item = drinkables[choice_num - 1]
            player_status["health"] += item["healing"]
            print("You are at " + str(player_status["health"]) + " health")
            player_status["items"].remove(item)
            drinkables.remove(item)

def buy(cost, item):
    if player_status["coins"] < cost:
        print("You don't have enough money to buy that!")
    elif player_status["coins"] >= cost:
        print("You have succesfully bought " + item["name"] + "!")
        player_status["items"].append(item)
        player_status["coins"] -= cost
    else:
        print("They're the wrong trousers and they've gone wrong!")

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
            item_definition(i, it, "raises damage by")
        else:
            item_definition(i, it, "raises health by")
    choice = get_input()

    if choice.isdigit():
        choice_num = int(choice)
        if choice_num <= len(shop_items):
            buy(shop_items[choice_num - 1]["cost"], shop_items[choice_num - 1])
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
