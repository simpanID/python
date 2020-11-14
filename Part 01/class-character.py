class Character():
    def __init__(self,name,power,healt):
        self.name = name
        self.power = power
        self.healt = healt
    
    def info(self):
        return 'Name : '+self.name+'\nPower : '+str(self.power)+'\nHealt : '+str(self.healt)
    
    def spesial(self,count):
        power_spesial = self.power * count
        return power_spesial

character_pertama = Character('Son Goku',89,100)
print(character_pertama.info())

total_spesial = character_pertama.spesial(3)
print('Power Spesial : '+str(total_spesial))
