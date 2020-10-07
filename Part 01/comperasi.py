#inputan dan casting
pertama = int(input('silahkan isi inputan angka disini ='))
kedua = int(input('silahkan isi inputan kedua disini ='))
print ('inputan pertama',pertama,)
print ('inputan kedua',kedua)

# symbol ==,>,<,>=,<=,!=,is,is not

# komperesi sama dengan ( == )
print('++++SAMA DENGAN++++')
sama_dengan = pertama == kedua
print(pertama,'=',kedua,'=',sama_dengan)

# komperasi lebih besar ( > )
print('++++LEBIH BESAR++++')
lebih_besar = pertama > kedua
print(pertama,'>',kedua,'=',lebih_besar)

# komperasi lebih kecil ( < )
print('++++LEBIH KECIL++++')
lebih_kecil = pertama < kedua
print(pertama,'<',kedua,'=',lebih_kecil)

#komperasi lebih besar sama dengan ( >= )
print('++++LEBIH BESAR SAMADENGAN++++')
lebih_besar_samadengan = pertama >= kedua
print(pertama,'>=',kedua,'=',lebih_besar_samadengan)

#komperasi lebih kecil sama dengan ( <= )
print('++++LEBIH KECIL SAMADENGAN++++')
lebih_kecil_samadengan = pertama <= kedua
print(pertama,'<=',kedua,'=',lebih_kecil_samadengan)

#komperasi tidak sama dengan ( != )
print('++++TIDAK SAMADENGAN++++')
tidak_samadengan = pertama != kedua
print(pertama,'!=',kedua,'=',tidak_samadengan)

#komperasi is ( is ) 
#is ini mencocokan hex yang  ada di dalam memory_id
print('++++IS++++')
this_is = pertama is kedua
print(pertama,'is',kedua,'=',this_is)

#komperasi is not  ( is not )
print('++++IS NOT++++')
this_is_not = pertama is not kedua
print(pertama,'is not',kedua,'=',this_is_not)









