import random

npc_names = input("List at least ten names seperated by commas: ")
name_list = npc_names.split(", ")

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
    level = random.randint(1, 20) # Whole number for each character to determine their level
    gold_int = random.randint(100, 500) #Random whole number for gold
    gold = gold_int / 100.0 #Divide by float to get the gold as a float (To complete the requirement of floats)
    npc_trait = random.sample(attributes, 3)
    trait1 = npc_trait[0]
    trait2 = npc_trait[1]
    trait3 = npc_trait[2]
    fight = random.choice([True, False]) #Boolean
    if fight == True:
        fight_status = "can"
    elif fight == False:
        fight_status = "can not"

    print(f"**{name}** (Lvl {level}) has {gold}g of gold, {fight_status} fight, and is known to be {trait1}, {trait2}, and {trait3}.")
    print("------------------------")




