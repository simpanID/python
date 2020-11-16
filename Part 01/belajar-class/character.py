class Character():
    def __init__(self,name,healt,power):
        self.name = name
        self.healt = healt
        self.power = power

    def print(self):
        print('-----------------')
        return 'Name : '+self.name+'\nHealt : '+str(self.healt)+'\nPower : '+str(self.power)

    def spesial(self,count):
        total_spesial = self.power * count
        return total_spesial

    