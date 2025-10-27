import random
import time
import math

usernames = []

for i in range(10):
    usernames.append(input("Gimmie Names:"))

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

for names in usernames:
    traits = random.sample(personality, 4)

trades = [
    "blacksmith", "baker", "carpenter", "farmer", "merchant",
    "soldier", "hunter", "healer", "priest", "miner",
    "tailor", "cook", "innkeeper", "scribe", "teacher",
    "alchemist", "guard", "ranger", "bard", "fisher"
]

for jobs in usernames:
    profressions = random.choice(trades)








