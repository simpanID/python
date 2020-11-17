from character import Character

character1 = Character('Son Goku',100,90)
print(character1.print())
character2 = Character('Son Goten',100,80)
print(character2.print())
character3 = Character('Son Gohan',100,82)
print(character3.print())

characters = [character1,character2,character3]
index = 0
for character in characters:
    print(str(index)+'.\n'+character.print())
    index +=1
print('----------------------------------')
select = int(input('pilih character anda : '))
selected_item = characters[select]

print('Anda memilih :'+str(selected_item.name))
plus_spesial = int(input('Tambahkan [1-3] Attack Spesial Character : '))
spesial_character = character.spesial(plus_spesial)
print('Power yang berhasil ditambahkan sebesar :'+str(spesial_character))
