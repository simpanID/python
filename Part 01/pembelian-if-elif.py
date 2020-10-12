#program python untuk membuat pembelian suatu buah

harga_buah = 1000 
print('Harga Buah ini adalah : Rp.'+str(harga_buah))
dompet = 5000
print('Uang dalam dompet kamu : Rp.'+str(dompet))
inputan = input('Berapa buah yang ingin kamu beli : ')
total = harga_buah * int(inputan)
print('------------------------------')
print('Total Pembelajaan Kamu Rp.'+str(total))
print('------------------------------')

if dompet > total :
    print ('Pembelian kamu Berhasil')
    print ('Sisa dompet kamu adalah Rp.'+str(dompet - total))
    print('------------------------------')
elif dompet == total :
    print ('Pembelian kamu Berhasil')
    print ('Sisa dompet kamu adalah Rp.'+str(dompet-total))
    print ('Silahkan Top Up Dompet kamu')
    print('------------------------------')
else :
    print ('Pembayaran ditolak')
    print ('Dompet kamu tidak mencukupi untuk melakukan pembelian')
    print('------------------------------')