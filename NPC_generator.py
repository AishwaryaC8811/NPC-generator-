npc_names = input("List ten names seperates by commas: ")

npc_list = []
npc_list.append(npc_names)

for name in npc_list:
    level = random.randit(1,10) # Whole number for each character to determine their level
    gold_int = random.randit(100, 500) #Random whole number for gold
    gold = gold_int / 100.0 #Divide by float to get the gold as a float (To complete the requirement of floats)
    

import random


attributes = [
    "brave",
    "loyal",
    "curious",
    "wise",
    "kind",
    "honest",
    "clever",
    "bold",
    "gentle",
    "cunning",
    "patient",
    "fearless",
    "stubborn",
    "generous",
    "ruthless",
    "calm",
    "charming",
    "proud",
    "humble",
    "caring",
    "mysterious",
    "stern",
    "witty",
    "thoughtful",
    "reckless",
    "focused",
    "cheerful",
    "vengeful",
    "serious",
    "forgiving",
    "confident",
    "quiet",
    "daring",
    "shy",
    "friendly",
    "jealous",
    "noble",
    "cruel",
    "hopeful",
    "ambitious"
]

