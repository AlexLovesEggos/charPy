import csv

classes = {
    'Artificer':[8,'int',['int'],'half'],
    'Barbarian':[12,'str',['str','con'],'non'],
    'Bard':[8,'cha',['cha'],'full'],
    'Cleric':[8,'wis',['wis'],'full'],
    'Druid':[8,'wis',['wis'],'full'],
    'Fighter':[10,'int',['int'],'non'],
    'Monk':[8,'wis'],
    'Paladin':[10,'cha'],
    'Ranger':[10,'wis'],
    'Rogue':[8,'int'],
    'Sorcerer':[6,'cha'],
    'Warlock':[8,'cha'],
    'Wizard:':[6,'int'],
    }

def readCsv(filepath,rowHeaders = False,colNames = False):
        rows = []
        try:
            with open(f'{filepath}', mode ='r')as file:
                csvFile = csv.reader(file)
                for line in csvFile:
                    try:
                        b = line.index('')
                        a = line[0:b]
                    except:
                        a = line[0:]
                        #print(a)
                        #print(a[0])
                        if len(a) == 1:
                            a = a[0]
                            #Convert to int if possible!
                            try:
                                a = int(a)
                                #print('Integered')
                            except:
                                #print('CANT INT IT')
                                a = a
                                if a == '[]':
                                    a = []
                            #print(line[0],a)
                    rows.append(a)
            return rows
        except:
            return -1
        
class Character:
    #Factories?
    def updateAll(self):
        print('ooga')
        rows = [
            ['name',self.name],
            ['characterClass',self.charclass],
            ['subclass',self.subclass],
            ['background',self.background],
            ['race',self.race],
            ['allignment',self.allignment],
            ['exp',self.exp],
            ['level',self.level],
            ['strength',self.strength],
            ['dexterity',self.dexterity],
            ['constitution',self.constitution],
            ['intelligence',self.intelligence],
            ['wisdom',self.wisdom],
            ['charisma',self.charisma],
            ['expertise',*self.expertise],
            ['proficient',*self.proficient],
            ['joat',self.joat],
            ['currentHP',self.currentHP],
            ['tempHP',self.tempHP],
            ['money',*self.money],
            ['spellSlots',*self.spellSlots],
            ['spells',*self.spells]]
        #print(rows)
        with open(f'./Characters/{self.name}_char.csv', 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile,lineterminator ='\n')
            # writing the data rows
            csvwriter.writerows(rows)            
        print('updated stats')

    def readAll(self):
        print(self)

    @staticmethod
    def createCharacter(       
        name,
        charclass = 'NA',
        subclass = 'NA',
        background = 'NA',
        race = 'NA',
        allignment = 'NA',
        exp = 0,
        level = 1,
        strength = 0,
        dexterity = 0,
        constitution = 0,
        intelligence = 0,
        wisdom = 0,
        charisma = 0,
        expertise = [],
        proficient = [],
        joat = 0,
        currentHP = 0,
        tempHP = 0,
        money = [0,0,0,0,0],
        spellSlots = [0,0,0,0,0,0,0,0,0],
        spels = []):

        print(f'Created new blank character')

        #Save character csv
        open(f'./Characters/{name}_char.csv', 'w', newline='')
        #probably some update character function
        #init with the variables VV
        character = Character(name,
        charclass,
        subclass,
        background,
        race,
        allignment,
        exp,
        level,
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma,
        expertise,
        proficient,
        joat,
        currentHP,
        tempHP,
        money,
        spellSlots,
        spells)

        
        character.updateAll()
        
        return character

        
    def loadCharacter(name):
        print('Loading Character')
        charstats = []
        try:
            with open(f'./Characters/{name}_char.csv', mode ='r')as file:
                csvFile = csv.reader(file)
                #print(csvFile)
                for line in csvFile:
                    #print(line)
                    #print(line)
                    try:
                        b = line.index('')
                        a = line[1:b]
                    except:
                        a = line[1:]
                    #print(a)
                    #print(a[0])
                    if len(a) == 1:
                        a = a[0]
                        #Convert to int if possible!
                        try:
                            a = int(a)
                            #print('Integered')
                        except:
                            #print('CANT INT IT')
                            a = a
                            if a == '[]':
                                a = []
                    #print(line[0],a)
                    charstats.append(a)
            print(charstats)
            character = Character(*charstats)
            return character
        except:
            return -1

    
    def __init__(self,
        name,
        charclass,
        subclass,
        background,
        race,
        allignment,
        exp,
        level,
        strength,
        dexterity,
        constitution,
        intelligence,
        wisdom,
        charisma,
        expertise,
        proficient,
        joat,
        currentHP,
        tempHP,
        money,
        spellSlots,
        spells):
        
        #===== Self Input Stats =====
        #Qualitative Traits
        self.name = name
        self.charclass = charclass
        self.subclass = subclass
        self.background = background
        self.race = race
        self.allignment = allignment
        self.exp = exp
        #Level
        self.level = level
        #Ability Scores
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.abilityScores = []
        #Expertise and Proficiency
        self.expertise = expertise
        self.proficient = proficient
        self.joat = joat
        #Health and HP
        self.currentHP = currentHP
        self.tempHP = tempHP
        
        self.money = money #DICT
        #self.inventory = inventory #maybe dictionary
        #self.weaponProficiencies = weaponProficiencies
        #self.otherProficiencies = otherProficiencies
        #self.weapons = weapons #DICT DIC DMG PROF ETC FINNESE
        self.spellSlots = spellSlots
        self.spells = spells
        print(self.spells)
        
        #==== Calculated Values =====
        self.proficiencyBonus = 2 + int((self.level-1)/4)
        #Modifiers dictionary
        self.modifiers = {
            "str":(-5 + int(self.strength/2)),
            "dex":(-5 + int(self.dexterity/2)),
            "con":(-5 + int(self.constitution/2)),
            "int":(-5 + int(self.intelligence/2)),
            "wis":(-5 + int(self.wisdom/2)),
            "cha":(-5 + int(self.charisma/2))
            }
        #Skills dictionary
        self.skills = {
            "Acrobatics":(self.modifiers["dex"]),
            "Animal Handling":(self.modifiers["wis"]),
            "Arcana":(self.modifiers["int"]),
            "Athletics":(self.modifiers["str"]),
            "Deception":(self.modifiers["cha"]),
            "History":(self.modifiers["int"]),
            "Insight":(self.modifiers["wis"]),
            "Intimidation":(self.modifiers["cha"]),
            "Investigation":(self.modifiers["int"]),
            "Medicine":(self.modifiers["wis"]),
            "Nature":(self.modifiers["int"]),
            "Perception":(self.modifiers["wis"]),
            "Performance":(self.modifiers["cha"]),
            "Persuasion":(self.modifiers["cha"]),
            "Religion":(self.modifiers["int"]),
            "Sleight of Hand":(self.modifiers["dex"]),
            "Stealth":(self.modifiers["dex"]),
            "Survival":(self.modifiers["wis"]),
            }
        skillsList = list(self.skills.keys())
        #Add expertise and proficiency bonuses
        if(len(self.proficient)>0):
            for proficiency in self.proficient:
                self.skills[proficiency] = self.skills[proficiency] + self.proficiencyBonus
        if self.joat > 0:
            #print('JOAT')
            nonProficient = [x for x in skillsList if x not in self.proficient]
            for proficiency in nonProficient:
                self.skills[proficiency] = self.skills[proficiency] + int(self.proficiencyBonus*.5)       
        if(len(self.expertise)>0):       
            for expertise in self.expertise:
                self.skills[expertise] = self.skills[expertise] + self.proficiencyBonus
        #Initiative
        self.initiative = self.modifiers["dex"]
        #Hitpoints and Hitdie
        if self.charclass != 'NA':
            self.hitdie = classes[self.charclass][0]
            print('e')
            self.hitpointMax = (self.hitdie + self.modifiers["con"]) + ((self.level-1) * (int(.5 * self.hitdie)+self.modifiers["con"]+1))
        else:
            self.hitdie = 0
            self.hitpointMax = 0
        self.passivePerception = 10 + self.proficiencyBonus + self.skills['Perception']

        #SPELL HELL SPELL HELL SPELL HELLLLLLLLLLLLL
        if classes[self.charclass][3] == 'full':
            self.totalSlots = readCsv('./Stats/FullCaster.csv')[self.level]
            #print(self.totalSlots)

            
    def getModifier(self,modifier):
        return(self.modifiers[modifier])
    def getSkill(self,skill):
        return(self.skills[skill])
    def pay(self,amount,type,strict=False):
        return 0
    def recieve(self,amount,type,strict=False):
        return 0
def getSpellSlots(level,castType):
    spellSlots = [0,0,0,0,0,0,0,0,0]
    if castType == 'Full':
        print('hella')
        
        
#pyper = Character.createCharacter('Pyper')
#pyper = Character.loadCharacter('Pyper')
#print(toad.level,toad.dexterity)
#print(list(pyper.skills.keys())
