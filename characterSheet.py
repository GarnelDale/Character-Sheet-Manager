# Author: Torin Bolander
# Program: Character Sheet and die manager

import random

# StatBlock parent class
class StatBlock:
    def __init__(self):
        self.currentHealth = 0
        self.maxHealth = 0
        self.initiative = 0
        self.armorClass = 0
        self.name = ""
        self.speed = 0
        self.race = ""
        self.level = 0
    
    # Retrieval methods for each instance value
    def getCurrent(self): return self.currentHealth
    def getMax(self): return self.maxHealth
    def getInitiative(self): return self.initiative
    def getAC(self): return self.armorClass
    def getName(self): return self.name
    def getSpeed(self): return self.speed
    def getRace(self): return self.race
    def getLevel(self): return self.level

    # Updating methods for each instance value
    # changeCurrent handles both positive and negative change 
    def changeCurrent(self, change, difference):
        if difference == 0:
            if change > self.currentHealth:
                self.currentHealth = 0
            else:
                self.currentHealth -= change
        elif difference == 1:
            if change >= (self.maxHealth - self.currentHealth):
                self.currentHealth = self.maxHealth
            else:
                self.currentHealth += change

    def setMax(self, health): 
        self.maxHealth = health 
        self.currentHealth = health
    def setInitiative(self, start): self.initiative = start
    def setAC(self, ac): self.armorClass = ac
    def setName(self, word): self.name = word
    def setSpeed(self, zoom): self.speed = zoom
    def setRace(self, kin): self.race = kin
    def setLevel(self, lvl): self.level = lvl

    #def display()

# CharacterSheet child class    
class CharacterSheet(StatBlock):
    def __init__(self):
        StatBlock.__init__(self)
        self.playerClass = ""
    
    # CharacterSheet specific getter and setter
    def getClass(self): return self.playerClass
    def setClass(self, skill): self.playerClass = skill 

    # Output the values for the Character Sheet in a readable form
    def display(self):
        print(f"Name: {self.getName()}   Class: {self.getClass()}    Race: {self.getRace()}\n"
              f"Level: {self.getLevel()}    Armor Class: {self.getAC()}    Speed: {self.getSpeed()}\n"
              f"Current Health: {self.getCurrent()}    Max Health: {self.getMax()}    "
              f"Initiative: {self.getInitiative()}")    

# List of available commands for the help action to print
commands = ["Available commands:", "cp - Fill Character Sheet",
            "roll - Roll dice", "display - Print out Character Sheet information",
            "heal - Heal your character", "hurt - Apply damage to character",
            "fight - Update initiative", "help - Print out available commands", 
            "quit - Close Program"]
            
# Opening message
print ("Initializing Character Sheet manager...\n Type 'help' to see list of commands")

# For future file management the step to load a saved CharacterSheet goes here.
# For now however we will be filling a CharacterSheet object every launch
# TODO fill in input system once 

# Roll function for "rolling" die
def roll (amount, sides):
    total = 0
    originalAmt = amount
    print ("Rolling dice...")
    # Sum the die "rolls"
    while amount > 0:
        total += random.randint(1, sides)
        amount -= 1
    # Print the final result of total rolls
    print (f"{originalAmt}d{sides}: {total}")

# Main program loop
quit = False
myChar = CharacterSheet()
while not quit:
    action = input("> ")
    if action == "quit":
        # Set the quit condition of the loop to exit program
        quit = True
        print ("Thank you for using our Character sheet and die roller!")
    elif action == "roll":
        # Take in user input in a standard notation (ex. 1d20) and pass to roll 
        # function for "rolling"
        dice = input("Input dice to roll using #d# notation: ")
        kinds = dice.split('d')
        amount = int(kinds[0])
        sides = int(kinds[1])
        roll (amount, sides)
    elif action == "cp":
        # Fill Character Sheet
        myChar.setName(input("Enter character name: "))
        myChar.setClass(input("Enter character class: "))
        myChar.setRace(input("Enter character race: "))
        myChar.setLevel(int(input("Enter character level: ")))
        myChar.setAC(int(input("Enter character Armor Class: ")))
        myChar.setSpeed(int(input("Enter character movement speed: ")))
        myChar.setMax(int(input("Enter Max Health (Warning: Current health is set"
                                " to max during setup):  ")))
        myChar.setInitiative(int(input("Enter current initiative (If not applicable, set to 10): ")))
    #elif action == "csb":
        # TODO Fill stat block object
        # This feature is not yet designed
    elif action == "display":
        # Print out Character sheet
        myChar.display()
    elif action == "heal":
        # Heal Character
        myChar.changeCurrent(int(input("Heal by how much? ")), 1)
    elif action == "hurt":
        # Damage Character
        myChar.changeCurrent(int(input("How much damage? ")), 0)
    elif action == "fight":
        # Update initiative
        myChar.setInitiative(int(input("Enter current initiative: ")))
    elif action == "help":
        # Output list of available commands
        for x in range(len(commands)):
            print(commands[x])
    else:
        # Error case for nonexistent commands, typos, etc.
        print ("Input not recognized please try again")