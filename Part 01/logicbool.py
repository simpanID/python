#logika boolean
#operasi logika boolean meliputi
# NOT,OR,AND,XOR(^)

#operasi (NOT) adalah kebalikannya jika TRUE maka hasilnya FALSE
#jika FALSE maka hasilnya TRUE
a = True
c = not a
print('data a =',a)
print('data c =',c)

#operasi (OR)
#jika ada suatu data ada TRUE maka hasilnya akan diambil TRUE
# atau mudah nya OR itu adalah penjumlahan dari BINER
# FALSE = 0 dan TRUE = 1, TRUE mencangkup contoh : 1,2,3,4,dst
print('-----------OR------------')
a = True #1
b = False #0
c = a or b # 1 + 0
print('data a =',a)
print('data b =',b)
print(a,'OR',b,'adalah',c)
a = False
b = True
c = a or b # 0 + 1 
print(a,'OR',b,'adalah',c)
a = True
b = True
c = a or b # 1 + 1
print(a,'OR',b,'adalah',c)
a = False
b = False
c = a or b # 0 + 0
print(a,'OR',b,'adalah',c)

# operasi (AND)
# jika ada suatu data ada FALSE maka hasilnya akan diambil FALSE
# atau mudahnya AND adalah perkalian dari BINER
# FALSE =  0 dan TRUE = 1
print('-----------AND-----------')
a = True
b = False
c = a and b # 1 * 0
print('data a adalah =',a)
print('data b adalah =',b)
print(a,'and',b,'adalah',c)
a = False
b = True
c = a and b # 0 * 1
print(a,'and',b,'adalah',c)
a = False
b = False
c = a and b # 0 * 0
print(a,'and',b,'adalah',c)
a = True
b = True
c = a and b # 1 * 1
print(a,'and',b,'adalah',c)

# operasi XOR 
# akan TRUE jika ada salah satu data TRUE
# tidak berlaku untuk 2 data TRUE
# contoh jika a = TRUE, B = TRUE maka hasilnya FALSE
print('-----------XOR-----------')
a = True
b = False
c = a ^ b
print('data a adalah =',a)
print('data b adalah =',b)
print(a,'XOR',b,'adalah',c)
a = False
b = True
c = a ^ b # 0 * 1
print(a,'XOR',b,'adalah',c)
a = False
b = False
c = a ^ b # 0 * 0
print(a,'XOR',b,'adalah',c)
a = True
b = True
c = a ^ b # 1 * 1
print(a,'XOR',b,'adalah',c)
