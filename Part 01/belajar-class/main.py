from character import Character

character1 = Character('Son Goku',100,90)
print(character1.print())
spesial = character1.spesial(3)
print('Spesial : '+str(spesial))

character2 = Character('Son Goten',100,80)
print(character2.print())

character3 = Character('Son Gohan',100,82)
print(character3.print())

characters = [character1,character2,character3]
index = 0
for character in characters:
    print(str(index)+'.'+character.print())
    index +=1

