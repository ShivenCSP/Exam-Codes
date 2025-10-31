NPC Generator
(MIT lisence)

## Highlights
- Automatically generates ten unique non-player characters (NPCs).  
- Randomly make attributes such as personality traits, age, height, and job.  
- Includes additional randomized details like magic ability and skill level.  
- Simple, Python script using only the math, time and random libraries.  
- Made for open-world games as per requested by client.  

## Overview
The NPC Generator is a lightweight Python script created by me,Shiven, to help developers in creating npcs  quickly. Each NPC has some attributes including name, profession, personality traits, age, height and if they are a magic user or not.

For example:


    # variables for the npc's traits, job and age

    for name in usernames:
    traits = random.sample(personality, 2)
    job = random.choice(trades)
    age = random.randint(18, 65)

    # attempt to add bool and floats

    mage = bool(random.randint(0, 1))
    skill = round(random.uniform(0.0, 10.0), 2)
    height = round(random.uniform(1.7, 2.0), 2)



The program shows subtle differences between npcs by random sampling, making every character different than others and unique for a better experience and meeting new personalities of people. The goal of this project is to give an easy and simple way to add people to worlds, without having to spend grueling hours to make it yourself. It was made so it gives all the information about the npc in organized and detailed form.

For example:


    # prints everything in 0.2 second intrevals for smoothness

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

    
## Author
Author: Shiven  
GitHub: https://github.com/ShivenCSP

## Usage
Run the script in any terminal or Python IDE. You will be have to enter ten names. Then, the generator will then make 10 NPC profiles with some specific attributes in the terminal.

Example output:


    ____________________________________
    Name: john
    Age: 64 years old
    Height: 1.8 meters tall
    Job: alchemist  
    Skill Level: 5.4
    Traits: forgiving, funny.
    Magic User: True
    ____________________________________


## Python
python npc_generator.py
