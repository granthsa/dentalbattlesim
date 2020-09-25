#dentalbattlesim
#created by: Sam Grantham
#version: 1.0

#define constants

starting_health = 100

#define variables and lists

weapons = ["The Dental Floss", "The Toothbrush", "The Electric Toothbrush", "The Mouth Wash"]
weather_conditions = ["Mild", "Wind Storm", "Sunny Day", "Cyclone", "Snow Storm"]
weather_type = ""
player_health = 1
computer_health = 0
player_weapon = ""
computer_weapon = ""
player_name = ""
select_weapom = ""
player_damage = 1
computer_damage = 1
funfacts = ["Don't go to bed without brushing your teeth. Sleep is the perfect time for bacteria to develop", "Use a toothpaste with fluoride, to help prevent against tooth decay", "See the dentist at least twice a year to prevent needing cavities filled in the future"]

#import random

import random

#define player "setupplayer"

def setupplayer():
    global player_name
    global player_health
    global player_weapon
    player_weapon = input("Please select one of the following weapons\nThe Dental Flosss - Damage: 8\nThe Toothbrush - Damage: 10\nThe Electric Toothbrush - Damage: 12\nThe Mouth Wash - Damage: 6: ")
    if player_weapon in weapons:
        print("Weapon Selected")
    else:
        while player_weapon not in weapons:
            player_weapon = input("Please select one of the following weapons\nThe Dental Floss\nThe Toothbrush\nThe Electric Toothbrush\nThe Mouth Wash: ")
            print("Weapon Selected")
    player_health = starting_health
    print("player_health " + str(player_health))

#define computer "setupcomputer"
            
def setupcomputer():
    global player_name
    global player_health
    global player_weapon
    global computer_weapon
    global computer_health
    computer_weapon = random.choice(weapons)
    computer_health = starting_health

    
    



#define "player_attack"

def player_attack():
    global player_name
    global player_health
    global player_weapon
    global computer_weapon
    global computer_health
    global weather_type
    global player_damage
    if player_weapon == "The Dental Floss":
        player_damage = 8
        print("NOTE: This is only a game, designed to teach about dental hygiene. Do not attempt to replicate anything attakcs in this game in your own life")
        attack = input("Are you ready to attack?: ")
        weather_type = random.choice(weather_conditions)
        if attack == "yes" or attack == "Yes":
            if weather_type == "mild":
                print("Your dental floss was successful, and caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
            if weather_type == "Wind Storm":
                player_damage = 0
                print("The wind blew away your dental floss and you caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                      
            if weather_type == "Sunny Day":
                player_damage = (player_damage - 2)
                print("The sun melted your dental floss slightly, and you only caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                      
            if weather_type == "Cyclone":
                player_damage = (player_damage - 3)
                print("The cyclone caused the dental floss to wrap around your feet and you lost 3 damage points")
                computer_health = (computer_health - player_damage)
                
            if weather_type == "Snow Storm":
                player_damage = (player_damage + 4)
                print("The snow storm froze your dental floss, making it stronger and more effective. You caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
            
        
        
    if player_weapon == "The Toothbrush":
        player_damage = 10
        weather_type = random.choice(weather_conditions)
        print("NOTE: This is only a game, designed to teach about dental hygiene. Do not attempt to replicate anything attakcs in this game in your own life")
        attack = input("Are you ready to attack?: ")
        if attack == "yes" or attack == "Yes":
            if weather_type == "mild":
                print("Your tootbrush was successful, and caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                
            if weather_type == "Wind Storm":
                print("The wind storm did not affect your dental floss and you caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                      
            if weather_type == "Sunny Day":
                player_damage = (player_damage + 4)
                print("The sun gave you a vitamin D boost, and you were able to cause {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                      
            if weather_type == "Cyclone":
                player_health = 0
                print("The cyclone took away your toothbrush and you caused no damage")
                
            if weather_type == "Snow Storm":
                player_damage = (player_damage - 5)
                print("The snow storm froze your bristles off. You caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)

        
    if player_weapon == "The Electric Toothbrush":
        player_damage = 12
        weather_type = random.choice(weather_conditions)
        print("NOTE: This is only a game, designed to teach about dental hygiene. Do not attempt to replicate anything attakcs in this game in your own life")
        attack = input("Are you ready to attack?: ")
        if attack == "yes" or attack == "Yes":
            if weather_type == "mild":
                print("Your electric tootbrush was successful, and caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                
            if weather_type == "Wind Storm":
                player_damage = (player_damage - 1)
                print("The wind storm made it hard for you to fight effectively and you caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                      
            if weather_type == "Sunny Day":
                print("The sun fried your electric toothbrush, and you caused no damage")
                      
            if weather_type == "Cyclone":
                print("The cyclone took away your toothbrush and you caused no damage")
                
            if weather_type == "Snow Storm":
                player_damage = (player_damage + 5)
                print("The snow storm made your electric toothbrush extra hard. You caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
        
    if player_weapon == "The Mouth Wash":
        player_damage = 6
        weather_type = random.choice(weather_conditions)
        print("NOTE: This is only a game, designed to teach about dental hygiene. Do not attempt to replicate anything attakcs in this game in your own life")
        attack = input("Are you ready to attack?: ")
        if attack == "yes" or attack == "Yes":
            if weather_type == "mild":
                print("The mouth wash was effective, and caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                
            if weather_type == "Wind Storm":
                print("The wind storm made no impact on your mouth wash and you caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                      
            if weather_type == "Sunny Day":
                player_damage = (player_damage + 7)
                print("The sun boiled your mouth wash, and you caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)
                
                      
            if weather_type == "Cyclone":
                player_damage = (player_damage + 9)
                print("The cyclone charged your mouth wash with magical powers and you ended up causing {} damage points".format(player_damage))
            
            if weather_type == "Snow Storm":
                player_damage = (player_damage + 5)
                print("The snow storm made your electric toothbrush extra hard. Therefor you caused {} damage points".format(player_damage))
                computer_health = (computer_health - player_damage)

#define "computer_attack"

def computer_attack():
    global player_name
    global player_health
    global player_weapon
    global computer_weapon
    global computer_health
    global computer_damage
    global player_damage
    print("computer_weapon ="+ computer_weapon)
    if computer_weapon == "The Dental Floss":
        computer_damage = 8
        weather_type = random.choice(weather_conditions)
        if weather_type == "mild":
            print("Your opponents dental floss was successful, and caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
        if weather_type == "Wind Storm":
            computer_damage = 0
            print("The wind blew away your opponents dental floss and caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
                  
        if weather_type == "Sunny Day":
            computer_damage = (computer_damage - 2)
            print("The sun melted your dental floss slightly, and they only caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
                  
        if weather_type == "Cyclone":
            computer_damage = (computer_damage - 3)
            print("The cyclone caused the dental floss to wrap around your oppoments feet and they lost 3 damage points")
            player_health = (player_health - computer_damage)
            
        if weather_type == "Snow Storm":
            computer_damage = (computer_damage + 4)
            print("The snow storm froze your opponents dental floss, making it stronger and more effective. They caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)

    if computer_weapon == "The Toothbrush":
        computer_damage = 10
        weather_type = random.choice(weather_conditions)
        if weather_type == "mild":
            print("Your opponents tootbrush was successful, and caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
            
        if weather_type == "Wind Storm":
            print("The wind storm did not affect your opponents dental floss and they caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
                  
        if weather_type == "Sunny Day":
            player_damage = (player_damage + 4)
            print("The sun gave your opponents a vitamin D boost, and they were able to cause {} damage points".format(computer_damage))
            computer_health = (computer_health - computer_damage)
                  
        if weather_type == "Cyclone":
            print("The cyclone took away your opponents toothbrush and you caused no damage")
            
        if weather_type == "Snow Storm":
            computer_damage = (computer_damage - 5)
            print("The snow storm froze your opponents bristles off. They caused {} damage points".format(computer_damage))
        
    if computer_weapon == "The Electric Toothbrush":
        computer_damage = 12
        weather_type = random.choice(weather_conditions)
        if weather_type == "mild":
            print("Your opponents electric tootbrush was successful, and they caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
            
        if weather_type == "Wind Storm":
            computer_damage = (computer_damage - 1)
            print("The wind storm made it hard for your opponent to fight effectively and they caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
                  
        if weather_type == "Sunny Day":
            print("The sun fried your opponents electric toothbrush, and they caused no damage")
                  
        if weather_type == "Cyclone":
            print("The cyclone took away your opponents toothbrush and they caused no damage")
            
        if weather_type == "Snow Storm":
            computer_damage = (computer_damage + 5)
            print("The snow storm made your opponents electric toothbrush extra hard. They caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
        
    if computer_weapon == "The Mouth Wash":
        computer_damage = 6
        weather_type = random.choice(weather_conditions)
        if weather_type == "mild":
            print("The mouth wash was effective, and your opponent caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
            
        if weather_type == "Wind Storm":
            print("The wind storm made no impact on your opponents mouth wash and they caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
                  
        if weather_type == "Sunny Day":
            player_damage = (player_damage + 7)
            print("The sun boiled your opponents mouth wash, and they caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
            
                  
        if weather_type == "Cyclone":
            player_damage = (player_damage + 9)
            print("The cyclone charged your opponents mouth wash with magical powers and they ended up causing {} damage points".format(computer_damage))
        
        if weather_type == "Snow Storm":
            player_damage = (player_damage + 5)
            print("The snow storm made your opponents toothbrush extra hard. They therefor caused {} damage points".format(computer_damage))
            player_health = (player_health - computer_damage)
        

#run all the functions in the program

player_name = input("What is your name, soldier?: ")
while player_name == "":
       player_name = input("What is your name, soldier?: ") 

setupplayer()

setupcomputer()

player_attack()

computer_attack()

funfact = random.choice(funfacts)
print("Fun Fact: {}".format(funfact))
print("\n Thank you for playing the dental hygiene game. Restart the program to play again.")


