#dentalbattlesim
#created by: Sam Grantham
#version: 2.0

#define constants

starting_health = 100

#define variables and lists

weapons = ["The Dental Floss - Damage: 8", "The Toothbrush - Damage: 10", "The Electric Toothbrush - Damage: 12", "The Mouth Wash - Damage: 6"]
weather_conditions = ["Mild", "Wind Storm", "Sunny Day", "Cyclone", "Snow Storm"]
player_health = 0
computer_health = 0
player_weapon = ""
computer_weapon = ""

#import random

import random

#define player "set up player"

def setupplayer():
    player_name = input("What is your name, soldier?: ")
    select_weapon = input("Please select one of the following weapons/nThe Dental Floss/nThe Toothbrush/nThe Electric Toothbrush/nThe Mouth Wash: ")
    if select_weapon in weapons:
        print("Weapon Selected")
    else:
        while select_weapon not in weapons:
            select_weapon = input("Please select one of the following weapons/nThe Dental Floss/nThe Toothbrush/nThe Electric Toothbrush/nThe Mouth Wash: ")
    player_health = starting_health
    return(player_weapon, player_health)

#define computer "set up computer"
            
def setupcomputer():
    computer_weapon = random.choice(weapons)
    computer_health = starting_health
    return(computer_weapon, computer_health)

    
    



#define "player attack"

def player_attack:
    if player_weapon == "The Dental Floss":
        player_damage = 8
        attack = input("Are you ready to attack? :")
        if attack == "yes":
            generate_attack()
        else:
            print("Back to main menu")
    if player_weapon == "The Toothbrush":
        player_damage = 10
        attack = input("Are you ready to attack? :")
        if attack == "yes":
            generate_attack()
        else:
            print("Back to main menu")
    if player_weapon == "The Electric Toothbrush":
        player_damage = 12
        attack = input("Are you ready to attack? :")
        if attack == "yes":
            generate_attack()
        else:
            print("Back to main menu")
    if player_weapon == "The Mouth Wash":
        player_damage = 6
        attack = input("Are you ready to attack? :")
        if attack == "yes":
            generate_attack()
        else:
            print("Back to main menu")
    

#define "computer attack

def computer_attack
    

#run program


setupplayer()

