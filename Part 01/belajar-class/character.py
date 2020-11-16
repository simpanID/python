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
        if total_spesial < 250:
            print('Character ini akan kalah, karena power anda kurang : '+str(boss-total_spesial))
        else:
            print('Character ini akan menang dan sisa power anda adalah :'+str(total_spesial-boss))
        return total_spesial
     