# FALSE ( - )
# TRUE ( + )

inputan = float(input('masukan dulu angka nya ='))
print('kamu menginput angka',inputan)
IsKurangDariNol = inputan < 0
IsLebihDariNol = inputan > 0
IsKurangDariLima = inputan < 5
IsLebihDariLima = inputan > 5
IsKurangDariDelapan = inputan < 8
IsLebihDariDelapan = inputan > 8
IsKurangDariSebelas = inputan < 11
IsLebihDariSebelas = inputan > 11
Hasil1 = IsLebihDariNol and IsKurangDariLima or IsLebihDariDelapan and IsKurangDariSebelas
print('------- 0 ++++++++++ 5 --------- 8 ++++++++++ 11 --------') 
print('Hasilnya',Hasil1)
print('---------------------------------------------------------')
print ('++++++ 0 -------- 5 +++++++++ 8 -------- 11 +++++++')
hasil2 = IsKurangDariNol or IsLebihDariLima and IsKurangDariDelapan or IsLebihDariSebelas
print('Hasilnya', hasil2)
