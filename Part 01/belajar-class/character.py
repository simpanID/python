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
        boss = 250
        final = boss - total_spesial
        if total_spesial < 250:
            print('Character ini akan kalah, karena power anda kurang : '+str(final))
        else:
            print('Character ini akan menang')
        return total_spesial
     