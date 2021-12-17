# Adventure
#
# By: Conner Skoumal
# Scrum: Spider-Scrum
# Professor: Eric Pogue
# Idea: Mark Hampton
#
# All rights reserved.

from tkinter import *
import tkinter as tk
import random

window = Tk()

output = Text(window)
window.geometry('640x450+0+0')
scrollbar = Scrollbar(window)
output.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = output.yview)
output.pack()
scrollbar.pack(side = RIGHT, fill = Y)
healingCap = 0
pushed = False

class Character:
    def __init__(char, attackMin, attackMax, type):
        char.health = random.randrange(1,100)
        char.attack = random.randrange(attackMin, attackMax)
        char.alive = True

        knightName = ["Sir Lancelot", "King Arthur", "Raiimond the Eager", "Rannulfus the Hero", "Salaman the Sentinel", 
        "Gilebin the Ugly", "Simmond the Dragonheart", "Arnould the Fearless", "Betyn the Poor", "Ernoldus of the South", 
        "Arabella of the Night", "Amalone the Truthful", "Maleta the Caring", "Marioth the Honorable", "Wander the Dragonheart", 
        "Ymanie the Yellow", "Angmar the Bold", "Ysabelle the Vigilant", "Issabella the Bold", "Albreda the Gladiator"]
        if (type == "Knight"):
            char.name = random.choice(knightName)

        archerName = ["Legolas", "Nob the Righteous", "Geroldus the Clever", "Guernon of the Ice", "Jemmy the Illuminator", 
        "Huffie the Patriot", "Hew the Warden", "Ludovicus the Cute", "Rex of the Night", "Ausout of the Sea", "Jessimond the Patroller", 
        "Susan the Rude", "Adhelina the Faithful", "Haueis the Timid", "Rikild of the Night", "Ganor the Young", "Miriella the Champ", "Mathildis the Noble", 
        "Ahelissa the Gracious", "Grizzel of the Night"]
        if (type == "Archer"):
            char.name = random.choice(archerName)

        wizardName = ["Merlin", "Gandalf", "Albus Dumbledore", "Harry Potter", "Hermoine Granger", "Ron Weasley",
        "Thistrum", "Itrix", "Ulritaz", "Eshan", "Rhekhealis", "Uhenaxis", "Aloharith", "Axone", "Alyn", "Anikon", 
        "Aholune", "Owyn", "Uzibaris", "Innerihann"]
        if (type == "Wizard"):
            char.name = random.choice(wizardName)


class Knight:
    charType = "Knight"
    k1 = Character(53, 89, charType)
    healthPoints = k1.health
    attackPoints = k1.attack
    alive = k1.alive
    name = k1.name

class Archer:
    charType = "Archer"
    a1 = Character(53, 89, charType)
    healthPoints = a1.health
    attackPoints = a1.attack
    alive = a1.alive
    name = a1.name

class Wizard:
    charType = "Wizard"
    w1 = Character(25, 52, charType)
    healthPoints = w1.health
    attackPoints = w1.attack
    alive = w1.alive
    name = w1.name

class Squad:
    def __init__(mySquad, squadNumber):
        randomCharacter = [Knight, Archer, Wizard]
        i = 1
        mySquad.group = []
        while i < (squadNumber + 1):
            char = random.choice(randomCharacter)
            myCharacter = [char.charType, char.name, char.healthPoints, char.attackPoints, char.alive]
            mySquad.group.append(myCharacter)
            i = i + 1  

def attack(attacker, attacked, damage):
    attackerSquad = attacker
    attackedSquad = attacked
    char = attackedSquad[2]
    charDamage = char - damage
    attackedSquad[2] = charDamage
    output.insert(INSERT, attackerSquad[1] + " attacks " + attackedSquad[1] + " for " + str(damage) + " damage!\n\n")
#    if attackedSquad[2] <= 0:
#        print("Dead")
#        s2.group.pop(attacked)
#        print(s2.group)
    global pushed
    pushed = True

healButton = Button(window, text='Heal', command = lambda: heal(s1.group[0]))

def heal(healer):
    healed = random.randrange(1, 30)
    healer[2] = healer[2] + healed
    output.insert(INSERT, str(healer[1]) + " has healed themselves for +" + str(healed) + " health points!\n\n")
    global healingCap
    healingCap += 1
    if healingCap >= 5:
        healButton["state"] = DISABLED
        output.insert(INSERT, "You ran out of healing potions!\n\n")
    global pushed
    pushed = True
        

def speak(speaker):
    if (speaker[0] == "Knight"):
        output.insert(INSERT, speaker[1] + " is ready to fight on a horse!\n\n")
    elif (speaker[0] == "Archer"):
        output.insert(INSERT, speaker[1] + " is ready to launch some arrows!\n\n")
    elif (speaker[0] == "Wizard"):
        output.insert(INSERT, speaker[1] + " is ready to cast a spell!\n\n")
    global pushed
    pushed = True

def stat(whichSquad, align):
    output.insert(INSERT, align + " Squad:\n\n")
    character = 0
    while character < len(whichSquad):
        output.insert(INSERT, "Name: " + whichSquad[character][1])
        output.insert(INSERT, "\nType: " + whichSquad[character][0])
        output.insert(INSERT, "\nHealth Points: " + str(whichSquad[character][2]))
        output.insert(INSERT, "\nAttack Damage: " + str(whichSquad[character][3]) + "\n\n")
        character = character + 1

heroSquad = []
enemySquad = []

s1 = Squad(3)
stat(s1.group, "Your")
s2 = Squad(3)
stat(s2.group, "Enemy")

attackButton = Button(window, text='Attack', command = lambda: attack(s1.group[0], s2.group[0], s1.group[0][3]))
healButton = Button(window, text='Heal', command = lambda: heal(s1.group[0]))
speakButton = Button(window, text='Speak', command = lambda: speak(s1.group[0]))
userStatButton = Button(window, text='User Stats', command = lambda: stat(s1.group, "Your"))
enemyStatButton = Button(window, text='Enemy Stats', command = lambda: stat(s2.group, "Enemy"))

attackButton.pack(side = LEFT, padx = 5, anchor = N, pady=4)
healButton.pack(side = LEFT, padx = 5, anchor = N, pady = 4)
speakButton.pack(side = LEFT, padx = 5, anchor = N, pady=4)
userStatButton.pack(side = LEFT, padx = 5, anchor = N, pady=4)
enemyStatButton.pack(side = LEFT, padx = 5, anchor = N, pady=4)

status = False
round = 2

window.mainloop()

#while status == False:
#    if (round % 2) == 0:
#        attackButton["state"] = NORMAL
#        healButton["state"] = NORMAL
#        speakButton["state"] = NORMAL
#        if pushed == True:
#            round += 1
#    else:
#        if (random.randint(0, 1) == 0):
#            randAttacker = s2.group[random.randint(0, len(s2))]
#            randAttacked = s1.group[random.randint(0, len(s1))]
#            attack(randAttacker, randAttacked, randAttacker[3])
#
#        else:
#            randHealed = s2.group[random.randint(0, len(s2))]
#            heal(randHealed)
#    print("Hello")
#    for x in s1.group:
#        if s1.group[x][4] == False:
#            s1.group.pop(x)