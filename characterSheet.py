# Author: Torin Bolander
# Program: Character Sheet and Die Manager

import random
import json

"""StatBlock parent class"""
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
        self.strength = 0
        self.dex = 0
        self.con = 0
        self.intel = 0
        self.wisdom = 0
        self.cha = 0

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

    # TODO def display() for DM's

    # Save as .json file for perpetuation after closing
    def save(self):
        stats = {"currentHealth":self.currentHealth, "maxHealth":self.maxHealth, 
                 "initiative":self.initiative, "armorClass":self.armorClass, 
                 "name":self.name, "speed":self.speed, "race":self.race, "level":self.level,
                 "strength":self.strength, "dex":self.dex, "con":self.con, "intel":self.intel,
                 "wisdom":self.wisdom, "cha":self.cha}

        file_name = input("Where do you wish to save this stat block? ")
        file = open(file_name, "w+")
        json.dump(stats, file)
        file.close()

    # Load a saved file and fill the stat block
    def load(self):
        file_name = input("Please enter the file name for the stat block: ")
        file = open(file_name, "r")
        stats = json.load(file)
        file.close()

        self.currentHealth = stats["currentHealth"]
        self.maxHealth = stats["maxHealth"]
        self.initiative = stats["initiative"]
        self.armorClass = stats["armorClass"]
        self.name = stats["name"]
        self.speed = stats["speed"]
        self.race = stats["race"]
        self.level = stats["level"]
        self.strength = stats["strength"]
        self.dex = stats["dex"]
        self.con = stats["con"]
        self.intel = stats["intel"]
        self.wisdom = stats["wisdom"]
        self.cha = stats["cha"]

"""CharacterSheet child class"""    
class CharacterSheet(StatBlock):
    def __init__(self):
        StatBlock.__init__(self)
        self.playerClass = ""
        self.profBonus = 2
    
    # Output the values for the Character Sheet in a readable form
    def display(self):
        print(f"Name: {self.name}   Class: {self.playerClass}    Race: {self.race}\n"
              f"Level: {self.level}    Armor Class: {self.armorClass}    Speed: {self.speed}\n"
              f"Current Health: {self.currentHealth}    Max Health: {self.maxHealth}    "
              f"Initiative: {self.initiative}    Proficiency Bonus: +{self.profBonus}\nStrength: "
              f"{self.strength}\nDexterity: {self.dex}\nConstitution: {self.con}\nIntelligence: "
              f"{self.intel}\nWisdom: {self.wisdom}\nCharisma: {self.cha}")  

    # Save as .json file for perpetuation after closing
    def save(self):
        stats = {"currentHealth":self.currentHealth, "maxHealth":self.maxHealth, 
                 "initiative":self.initiative, "armorClass":self.armorClass, 
                 "name":self.name, "speed":self.speed, "race":self.race, "level":self.level, 
                 "class":self.playerClass,"prof":self.profBonus, "strength":self.strength, 
                 "dex":self.dex, "con":self.con, "intel":self.intel, "wisdom":self.wisdom, 
                 "cha":self.cha}

        file_name = input("Where do you want to save this character sheet? ")
        file = open(file_name, "w+")
        json.dump(stats, file)
        file.close()

    # Load a saved file and fill the stat block
    def load(self): 
        file_name = input("Please enter the file name for the character sheet: ")
        file = open(file_name, "r")
        stats = json.load(file)
        file.close()

        self.currentHealth = stats["currentHealth"]
        self.maxHealth = stats["maxHealth"]
        self.initiative = stats["initiative"]
        self.armorClass = stats["armorClass"]
        self.name = stats["name"]
        self.speed = stats["speed"]
        self.race = stats["race"]
        self.level = stats["level"] 
        self.playerClass = stats["class"]
        self.profBonus = stats["prof"]
        self.strength = stats["strength"]
        self.dex = stats["dex"]
        self.con = stats["con"]
        self.intel = stats["intel"]
        self.wisdom = stats["wisdom"]
        self.cha = stats["cha"]

""" Roll function for "rolling" die"""
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

def main():
    # List of available commands for the help action to print
    commands = ["Available commands:", "cp - Fill Character Sheet",
                "roll - Roll dice", "display - Print out Character Sheet information",
                "heal - Heal your character", "hurt - Apply damage to character",
                "fight - Update initiative", "help - Print out available commands", 
                "quit - Close Program"]
    quit = False
    changed = False
    myChar = CharacterSheet()        
    # Opening message
    print ("Welcome to the Character Sheet and Die Manager!\n Type 'help' to see list of commands")

    # For future file management the step to load a saved CharacterSheet goes here.
    # For now however we will be filling a CharacterSheet object every launch
    # TODO fill in input system once 
    if input("Do you have a saved character sheet to load (y/n)? ") == 'y':
        myChar.load()
    else:
        print ("Please fill out a Character Sheet with the 'cp' command.")

    # Main program loop
    while not quit:
        action = input("> ")
        if action == "quit":
            # Set the quit condition of the loop to exit program
            if changed:
                if input("Changes have been made since last saving, would you like to save before quitting (y/n)? ") == 'y':
                    myChar.save()
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
            myChar.name = input("Enter character name: ")
            myChar.playerClass = input("Enter character class: ")
            myChar.race = input("Enter character race: ")
            myChar.level = int(input("Enter character level: "))
            myChar.profBonus = int(input("Enter character proficiency bonus: "))
            myChar.armorClass = int(input("Enter character Armor Class: "))
            myChar.speed = int(input("Enter character movement speed: "))
            myChar.maxHealth = int(input("Enter Max Health: "))
            myChar.currentHealth = int(input("Enter Current Health: "))
            myChar.initiative = int(input("Enter current initiative (If not applicable, set to 10): "))
            myChar.strength = int(input("Enter character Strength: "))
            myChar.dex = int(input("Enter character Dexterity: "))
            myChar.con = int(input("Enter character Constitution: "))
            myChar.intel = int(input("Enter character Intelligence: "))
            myChar.wisdom = int(input("Enter character Wisdom: "))
            myChar.cha = int(input("Enter character Charisma: "))
            changed = True
        #elif action == "csb":
            # TODO Fill stat block object
            # Dungeon Master features are not yet designed
        elif action == "display":
            # Print out Character sheet
            myChar.display()
        elif action == "heal":
            # Heal Character
            myChar.changeCurrent(int(input("Heal by how much? ")), 1)
            changed = True
        elif action == "hurt":
            # Damage Character
            myChar.changeCurrent(int(input("How much damage? ")), 0)
            changed = True
        elif action == "fight":
            # Update initiative
            myChar.initiative = int(input("Enter current initiative: "))
            changed = True
        elif action == "help":
            # Output list of available commands
            for x in range(len(commands)):
                print(commands[x])
        elif action == "save":
            # Save the values of the sheet
            myChar.save()
            changed = False
        else:
            # Error case for nonexistent commands, typos, etc.
            print ("Input not recognized please try again")

if __name__ == "__main__":
    main()