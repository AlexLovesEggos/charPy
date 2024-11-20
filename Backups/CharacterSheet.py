import os
#import subprocess
import os.path
import sys
import csv
import time
import charPy as cp
print('WAAAAAAAAAAAAAAAAAAA')


#SETUP STUFF
#check if libraries are installed
try:
    import numpy as np
except:
    print('Installing package: numpy')
    print(os.popen('py -m pip install "numpy"').read())
    import numpy as np
    print('All Prerequisites Installed')

#check if directories are created and files are all where they should be
#--==|[ For Windows ]|==--#
if os.name == 'nt':
    if not os.path.isdir('./Characters'):
        print('The folder does not exist so i will make it')
        os.makedirs('./Characters')
        print('Folder good now')
    else:
        print('folder good')

def ss(val,num=2,bf=True):
    if bf == False:
        l = len(str(val))
        v = str(val)+(' '*(num-l))
    else:  
        l = len(str(val))
        v = (' '*(num-l))+str(val)
    return v

def it(head,val,totsp = 20, buffer = True, lftbuf = True):
    ret = ""
    val = str(val)
    head = str(head)
    vallen = len(val)
    headlen = len(head)
    if buffer == True:
        ret = ' ' + head + (' ' * (totsp-headlen-vallen-1)) + val + ' '
    else:
        ret = head + (' ' * (totsp-headlen-vallen+1))+val
    if lftbuf == True:
        ret = "#"+ret
    return ret


def pos(val):
    if val > 0:
        val = "+"+str(val)
        return val
    else:
        return val
def clearScreen():
    pass
    #For Windows
    #if os.name == 'nt':
    #    _ = os.system('cls')
    # For macOS and Linux
    #else:
    #    _ = os.system('clear')
def showClassic():
    print(f'''
 CLASSIC CHARACTER SHEET
#=====================#=======================#=====================#
# {ss(character.name,19,False)} # {ss("Proficiency Bonus",18,False)}{ss(pos(character.proficiencyBonus),3)} # Armor Class         #
# Level {ss(ss(character.level,2),14,False)}# {ss("Inspiration",21,False)} # Max HP          {ss(character.hitpointMax,3)} #
# {ss(character.charclass,20,False)}# {ss("Initiative",21,False)} # Current HP      {ss(character.currentHP,3)} #
# {ss(character.subclass,20,False)}#=======================# Temp HP         {ss(character.tempHP,3)} #
#=====================# {ss("SAVING THROWS",21,False)} # Hitdie              # 
# Strength      {ss(character.strength)} {ss(pos(character.modifiers['str']))} # {ss("Strength",18,False)}{ss(pos(character.proficiencyBonus+character.modifiers['str']),3)} #=====================# 
# Dexterity     {ss(character.dexterity)} {ss(pos(character.modifiers['dex']))} # {ss("Dexterity",18,False)}{ss(pos(character.proficiencyBonus+character.modifiers['dex']),3)} # DEATH SAVES         #
# Constitution  {ss(character.constitution)} {ss(pos(character.modifiers['con']))} # {ss("Constitution",18,False)}{ss(pos(character.proficiencyBonus+character.modifiers['con']),3)} # Successes [ ][ ][ ] #
# Intelligence  {ss(character.intelligence)} {ss(pos(character.modifiers['int']))} # {ss("Intelligence",18,False)}{ss(pos(character.proficiencyBonus+character.modifiers['int']),3)} # Failures  [ ][ ][ ] #
# Wisdom        {ss(character.wisdom)} {ss(pos(character.modifiers['wis']))} # {ss("Wisdom",18,False)}{ss(pos(character.proficiencyBonus+character.modifiers['wis']),3)} #=====================# 
# Charisma      {ss(character.charisma)} {ss(pos(character.modifiers['cha']))} # {ss("Charisma",18,False)}{ss(pos(character.proficiencyBonus+character.modifiers['cha']),3)} #
#=====================#=======================#=====================#
# Passive       {ss(character.passivePerception,2)}    # {ss("SKILLS",21,False)} #                     #
# Perception          # {ss("Acrobatics",18,False)}{ss(pos(character.skills["Acrobatics"]),3)} #                     #
#=====================# {ss("Animal Handling",18,False)}{ss(pos(character.skills["Animal Handling"]),3)} #                     #
# {ss("MONEY",19,False)} # {ss("Arcana",18,False)}{ss(pos(character.skills["Arcana"]),3)} #                     #
# {ss("Copper(cp)",12,False)} {ss("0",6)} # {ss("Athletics",18,False)}{ss(pos(character.skills["Athletics"]),3)} #                     #
# {ss("Silver(sp)",12,False)} {ss("0",6)} # {ss("Deception",18,False)}{ss(pos(character.skills["Deception"]),3)} #                     #
# {ss("Electrum(ep)",12,False)} {ss("0",6)} # {ss("History",18,False)}{ss(pos(character.skills["History"]),3)} #                     #
# {ss("Gold(gp)",12,False)} {ss("0",6)} # {ss("Insight",18,False)}{ss(pos(character.skills["Insight"]),3)} #                     #
# {ss("Platinum(pp)",12,False)} {ss("0",6)} # {ss("Intimidation",18,False)}{ss(pos(character.skills["Intimidation"]),3)} #                     #
#=====================# {ss("Investigation",18,False)}{ss(pos(character.skills["Investigation"]),3)} #                     #
# {ss("",19)} # {ss("Medicine",18,False)}{ss(pos(character.skills["Medicine"]),3)} #                     #
# {ss("",19)} # {ss("Nature",18,False)}{ss(pos(character.skills["Nature"]),3)} #                     #
# {ss("",19)} # {ss("Perception",18,False)}{ss(pos(character.skills["Perception"]),3)} #                     #
# {ss("",19)} # {ss("Performance",18,False)}{ss(pos(character.skills["Performance"]),3)} #                     #
# {ss("",19)} # {ss("Persuasion",18,False)}{ss(pos(character.skills["Persuasion"]),3)} #                     #
# {ss("",19)} # {ss("Religion",18,False)}{ss(pos(character.skills["Religion"]),3)} #                     #
# {ss("",19)} # {ss("Sleight of Hand",18,False)}{ss(pos(character.skills["Sleight of Hand"]),3)} #                     #
# {ss("",19)} # {ss("Stealth",18,False)}{ss(pos(character.skills["Stealth"]),3)} #                     #
# {ss("",19)} # {ss("Survival",18,False)}{ss(pos(character.skills["Survival"]),3)} #                     #
#=====================#=====================#=====================#
# Total Spell Slots
# {character.totalSlots}
# Available Spell Slots
# {character.spellSlots}
#=====================#=====================#=====================#
#{character.hitdie}
#{character.hitpointMax}
              ''')
#Get characters
characterList = os.listdir('./Characters')
#Create a character or quit the program    
if characterList == []:
    print('There are no Characters in the character folder. Would you like to set one up now?')
#Read in the characters plain names
characterNames = []
for character in characterList:
    characterNames.append(character[0:-4].replace('_',' ')[:-5])
print('Type your character name or "new" to create a new character')
print(characterNames)
#Test Area



#Back to everythn else
active = True
while active == True:
    response = input('> ')
    if response == 'new':
        active = False
        print('Enter character name!')
        response = input('> ')
        character = cp.Character.createCharacter(response)
        print(f'Character "{character.name}" created!')
        name=response
    else:
        character = cp.Character.loadCharacter(response)
        name = response
        if character == -1:
            print('There is no character with that name, type "new" to create one.')
        else:
            active = False
            print(f'Character "{character.name}" loaded!')

active = True
show = False
while active == True:
    response = input('> ')
    if response == 'show':
        show = True
    if response[0:8] == 'hit for ':
        if (character.currentHP - int(response[8:])) < 0:
            character.currentHP = 0
        else:
            character.currentHP = character.currentHP - int(response[8:])
        character.updateAll()
        character = cp.Character.loadCharacter(name)
        print(f'You took {response[8:]} points of damage')
    if response[0:11] == 'healed for ':
        if (character.currentHP + int(response[11:])) > character.hitpointMax:
            character.currentHP = character.hitpointMax
        else:
            character.currentHP = character.currentHP + int(response[11:])
        character.updateAll()
        character = cp.Character.loadCharacter(name)
        print(f'You healed {response[8:]} points of damage')
        print('You were healed i guess')
    if response[0:3] == 'set':
        response = response[4:].split()
        if response[0].lower() == 'level':
            character.level = int(response[1])
        character.updateAll()
        character = cp.Character.loadCharacter(name)
        print(response)
    elif response.lower() == 'healed to max':
        character.currentHP = character.hitpointMax
        character.updateAll()
        character = cp.Character.loadCharacter(name)
    elif response.lower()[0:11] == 'cast level ':
        response = response[11:].split()
        i = int(response[0])-1
        if int(character.spellSlots[i]) <= 0:
            print("You don't have any more slots of this level")
        else:
            character.spellSlots[i] = int(character.spellSlots[i])-1
        character.updateAll()
        character = cp.Character.loadCharacter(name)
    elif response.lower()[0:13] == 'regain level ':
        response = response[13:].split()
        i = int(response[0])-1
        if int(character.spellSlots[i]) == character.totalSlots[i]:
            print("You can't have more slots than this")
        else:
            character.spellSlots[i] = int(character.spellSlots[i])+1
        print('updating slots')
        character.updateAll()
        character = cp.Character.loadCharacter(name)
    elif response.lower() == 'regain all slots':
        character.spellSlots = character.totalSlots  
        character.updateAll()
        character = cp.Character.loadCharacter(name)
    elif response.lower() == 'long rest':
        character.spellSlots = character.totalSlots
        character.currentHP = character.hitpointMax
        character.tempHP = 0
        character.updateAll()
    if show == True:
        clearScreen()
        showClassic()
        
        
#sys.exit("Exiting")

#cp.Character.loadCharacter('Pyper')
#Set all ability score Classes



#Select your character to open


#clearScreen()

print('Hella')

#sys.exit("Exiting")
        
time.sleep(1)
