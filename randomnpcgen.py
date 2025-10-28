#libraries
import random
import time
import math

# storage for the names
usernames = []

for i in range(10):
    usernames.append(input("Gimmie Names:"))

 # list for attributes and jobs of the npc
personality = [
    "accepting", "adaptable", "adventurous", "ambitious", "analytical", "brave",
    "calm", "caring", "charismatic", "clever", "compassionate", "confident", 
    "considerate", "courageous", "creative", "curious", "decisive", "dedicated",
    "diligent", "disciplined", "easygoing", "empathetic", "energetic", "enthusiastic",
    "fearless",  "flexible", "forgiving", "friendly", "funny", "generous", "grateful",
    "hard-working", "honest", "humble", "imaginative", "independent", "industrious",
    "intelligent", "kind", "logical", "loyal", "mature", "observant", "optimistic",
    "patient", "perceptive", "persistent", "resourceful", "responsible", "sincere"
]

trades = [
    "blacksmith", "baker", "carpenter", "farmer", "merchant",
    "soldier", "hunter", "healer", "priest", "miner",
    "tailor", "cook", "innkeeper", "scribe", "teacher",
    "alchemist", "guard", "ranger", "bard", "fisher"
]

# to print the npc's traits and trade
for name in usernames:
    traits = random.sample(personality, 4)
    job = random.choice(trades)

# last minute atempt to add bool and floats

    is_magic_user = random.choice([True, False])
    skill_level = round(random.uniform(0.0, 10.0), 2)

    print(f"\n{name} is a {job} who is {', '.join(traits)}.")
    print(f"Magic User: {is_magic_user}")
    print(f"Skill Level: {skill_level}")
    
# made by the magnificient shiven