level1 = {
    "rooms": {
        "kitchen": {
            "name": "kitchen",
            "objects": [
                {
                    "name": "chicken",
                    "description": "The chicken lays an egg. You eat it and get salminila."
                    "use_desc": "a chicken. wonder if it lays eggs"
                },
                {
                    "name": "couch",
                    "description": "Achievment Unlocked: Laziness"
                    "use_desc": "a comfortable enough looking couch. if i had aching bones i would sit on it"
                },
                {
                    "name": "microwaved game console",
                    "description": "You get electricuted and die"
                    "use_desc": "a fried to the core game console. wonder what would happen if you tried playing it"
                }
            ],
            "description": "In this room there is a chicken, a couch, and a microwaved game console.",
            "exits": {
                "north": "living room",
                "east": "closet",
            },
            "enemy": {
                "name": "stove",
                "hitpoints": 10,
                "muddy_turns": 0,
                "attack": 5,
                "coins": 10
            }
        },
        "living room": {
            "name": "living room",
            "description": "You better know what's in here, otherwise you're a geezer.",
            "objects": [
                {
                    "name": "potato",
                    "description": "The potato explodes. Good Job."
                    "use_desc": "a large potato. i don't know if it will stay around for long though"
                },
                {
                    "name": "nothing",
                    "description": "Nothing happens."
                    "use_desc": "nothing. if you use it something very interesting will clearly happen"
                }
            ],
            "exits": {
                "south": "kitchen",
                "north": "mudville"
            },
        },
        "closet": {
            "name": "closet",
            "exits": {},
            "description": "There is no way out of the closet.",
            "objects": [
                {
                    "name": "magic portal",
                    "description": "You were transported to never never land"
                    "use_desc": "a magical portal. this could help if you're stuck"
                }
            ],
            "enemy": {
                "name": "THE DREADED COAT HANGER",
                "hitpoints": 10,

                "muddy_turns": 0,
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
            "objects": [
                {
                    "name": "mud",
                    "description": "You throw a nice, big, glob of mud. Nice job."
                    "use_desc": "a infinite supply of mud. maybe you should throw it"
                }
            ],
            "exits": {
                "south": "living room",
                "west": "dining room"
            },
            "enemy": {
                "name": "Muddy Shoe",
                "hitpoints": 10,
                "muddy_turns": 0,
                "hitpoints": 20,
                "attack": 10,
                "coins": 20
            }
        },
        "dining room": {
            "name": "dining room",
            "description": "Here you find an assortment of plates, forks, and water pitchers.",
            "objects": [
                {
                    "name": "plates",
                    "description": "The stack of plates falls to the floor and shatters. Given the way I made this game, it is surprising that you managed to override my code and be unhurt. I'll have to fix that bug soon.",
                    "use_desc": "a stack of plates. you'll probably die if you drop them"
                },
                {
                    "name": "forks",
                    "description": "All of the forks except one are swept away by a sudden breeze. You then use the one to make a stabbing motion."
                    "use_desc": "a pile of forks. couldn't be a better fighting tool than a knife, could it?"
                },
                {
                    "name": "water pitchers",
                    "description": "The many water pitchers fall to the floor and crash causing extreme injury and death. You die."
                    "use_desc": "a ton of precariously stacked water pitchers. why did you pick all these up anyway?"
                }
            ],
            "exits": {
                "east": "mudville",
                "south": "bathroom"
            }
        },
        "bathroom": {
            "name": "bathroom",
            "description": "There is nothing in this room you want. Unless you want a toilet seat.",
            "objects": [
                {
                    "name": "toilet seat",
                    "description": "You stop to wonder why you ever wanted this. You throw it out the window. Your spider sense tingles. Something has changed."
                    "use_desc": "a toilet seat. (game creator silently facepalms) why on earth did you think that picking this up would be a good idea. it's not like it's gonna be entirely key to you winning the game or anything"
                }
            ],
            "exits": {
                "north": "dining room",
                "east": "nowhere"
            },
            "enemy": {
                "hitpoints": 10,

                "muddy_turns": 0,
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
