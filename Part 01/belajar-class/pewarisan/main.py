from ability import Ability

character1=Ability('Son Goku',55,'World',89,80)
character2=Ability('Bezita',57,'Vegeta / Saiya',85,81)

list=0
characters = [character1,character2]
for character in characters:
    print('No : '+str(list)+'\n'+str(character.print()))
    list+=1

data = int(input('Please Input Character Number : '))
load_data = characters[data]
print('Character Name : '+str(load_data.name)+'\nPower : '+str(load_data.attack))
if load_data.attack > 88:
    print('Your Character is Winner')
else:
    print('Your Character is Loses')

    