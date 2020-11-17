from character import Character

class Ability(Character):
        def __init__ (self,name,age,location,attack,defence):
            super().__init__(name,age,location)
            self.attack = attack
            self.defence = defence

        def print(self):
            return 'Name : '+self.name+'\nAge : '+str(self.age)+'\nLocation : '+self.location+'\nAttack : '+str(self.attack)+'\nDefence : '+str(self.defence)+'\n-----------------------------------'
