level1 = {
    "rooms": {
        "kitchen": {
            "name": "kitchen",
            "objects": [
                {
                    "name": "chicken",
                    "description": "The chicken lays an egg. You eat it and get salminila."
                },
                {
                    "name": "couch",
                    "description": "Achievment Unlocked: Laziness"
                },
                {
                    "name": "microwaved game console",
                    "description": "You get electricuted and die"
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
                },
                {
                    "name": "nothing",
                    "description": "Nothing happens."
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
                }
            ],
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
            "objects": [
                {
                    "name": "mud",
                    "description": "You throw a nice, big, glob of mud. Nice job."
                }
            ],
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
            "objects": [
                {
                    "name": "plates",
                    "description": "The stack of plates falls to the floor and shatters. Given the way I made this game, it is surprising that you managed to override my code and be unhurt. I'll have to fix that bug soon.",
                },
                {
                    "name": "forks",
                    "description": "All of the forks except one are swept away by a sudden breeze. You then use the one to make a stabbing motion."
                },
                {
                    "name": "water pitchers",
                    "description": "The many water pitchers fall to the floor and crash causing extreme injury and death. You die."
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
                }
            ],
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
