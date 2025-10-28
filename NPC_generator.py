import random

npc_names = input("List ten names seperated by commas: ")
name_list = npc_names.split(", ")
# print(name_list)

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



for name in name_list:
    level = random.randint(1,10) # Whole number for each character to determine their level
    gold_int = random.randint(100, 500) #Random whole number for gold
    gold = gold_int / 100.0 #Divide by float to get the gold as a float (To complete the requirement of floats)
    npc_trait = random.choice(attributes)
    print(f"{name} is level {level} and has {gold} grams of gold. They are {npc_trait} ")




