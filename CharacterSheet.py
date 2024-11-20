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
    cp.Character.classicConsole
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

spellsList = cp.readCsv('./Stats/Spells.csv')
print(np.shape(spellsList))
spellNames = [i[0] for i in spellsList]
spells = ['Mage Hand','Light']
spellStats = [i for i in [spellsList in spells]]
print(spellStats)


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

print('''
use "show" to show the classic character sheet,
other helpful commands can be found by using "help"''')
active = True
show = False
spells = False
while active == True:
    response = input('> ')
    if response == 'show':
        show = True
        spells = False
    elif response.lower() == 'spells':
        spells = True
        show = False
        
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
    elif response.lower() == 'test':
        print('Charisma'+character.pS('cha'))
    if show == True:
        clearScreen()
        character.classicConsole()
    if spells == True:
        clearScreen()
        character.showSpells()   
        
#sys.exit("Exiting")

#cp.Character.loadCharacter('Pyper')
#Set all ability score Classes



#Select your character to open


#clearScreen()

print('Hella')

#sys.exit("Exiting")
        
time.sleep(1)
