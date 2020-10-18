dompet = 20 # ini adalah isi  dompet kamu
barang = {
    'samsung' : 4,
    'apple' : 6,
    'xiomi' : 2,
}

for barang_key in barang :
    print('--------------------------')
    print('Anda Mempunyai Dompet '+str(dompet)+' Dollar')
    print(barang_key+' seharga '+str(barang[barang_key]) +' dollar')
    jumlah_beli = input('kamu ingin membeli berapa '+barang_key+' :?')
    print('kamu membeli '+barang_key+' '+jumlah_beli+' pcs')
    total = int(jumlah_beli) * barang[barang_key]
    print('Total pembelian kamu '+str(total)+' dollar')
    if dompet >= total:
        print('Pembelian Berhasil')
        dompet -= total
        if dompet == 0:
            print('Dompet kamu sudah kosong')
            break;
    else:
        print('Dompet tidak mencukupi')
        print('Anda tidak dapat membeli '+barang_key+' Sebanyak '+jumlah_beli+' pcs')
print('--------------------------')
print('Sisa uang di dompet '+str(dompet)+' Dollar')