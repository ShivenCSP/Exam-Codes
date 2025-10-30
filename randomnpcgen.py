#libraries
import random
import time
import math

# storage for the names
usernames = []

for i in range(10):
    usernames.append(input("Give me 10 Names:"))

 # list for attributes and jobs of the npc
personality = [
    "accepting" , "adaptable" , "adventurous" , "ambitious" , "analytical" , "brave" ,
    "calm" , "caring", "charismatic" , "clever" , "compassionate" , "confident" , 
    "considerate" , "courageous" , "creative" , "curious" , "decisive" , "dedicated" ,
    "diligent" , "disciplined" , "easygoing" , "empathetic" , "energetic" , "enthusiastic" ,
    "fearless" ,  "flexible" , "forgiving" , "friendly" , "funny" , "generous" , "grateful" ,
    "hard-working" , "honest" , "humble" , "imaginative" , "independent" , "industrious" ,
    "intelligent" , "kind" , "logical" , "loyal", "mature" , "observant" , "optimistic" ,
    "patient" , "perceptive" , "persistent" , "resourceful" , "responsible" , "sincere"
]

trades = [
    "blacksmith" , "baker" , "carpenter" , "farmer" , "merchant",
    "soldier" , "hunter" , "healer" , "priest" , "miner" ,
    "tailor" , "cook" , "innkeeper" , "scribe" , "teacher" ,
    "alchemist" , "guard" , "ranger" , "bard" , "fisher"
]

# to print the npc's traits and trade
for name in usernames:
    traits = random.sample(personality, 2)
    job = random.choice(trades)
    age = random.randint(18, 65)

# attempt to add bool and floats

    mage = bool(random.randint(0, 1))
    skill = round(random.uniform(0.0, 10.0), 2)
    height = round(random.uniform(1.7, 2.0), 2)

# prints everything in 0.2 second intrevals

    print("\n\n____________________________________")
    print(f"Name: {name}")
    time.sleep(0.2)
    print(f"Age: {age} years old")
    time.sleep(0.2)
    print(f"Height: {height} meters tall")
    time.sleep(0.2)
    print(f"Job: {job}")
    time.sleep(0.2)
    print(f"Skill Level: {skill}")
    time.sleep(0.2)
    print(f"Traits: {", ".join(traits)}.") # uses space and comma to join traits gramatically
    time.sleep(0.2)
    print(f"Magic User: {mage}")
    time.sleep(0.2)
    print("____________________________________")
    time.sleep(0.5)

# made by the magnificient shiven