print('ibu menyuruh membaca buku')
jumlah_buku = 10
jumlah_paham = 0
jumlah_baca = 0
baca_maksimal = 5

while jumlah_baca < jumlah_buku + 5:
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 9:
        print(f'buku ke {jumlah_paham + 1} belum dipahami ')
    else:
        jumlah_paham = jumlah_paham + 1
        print(f'buku ke {jumlah_paham} sudah dipahami')

print(f'jumlah buku yang selesai dibaca dan dipahami {jumlah_paham}')
if jumlah_paham == jumlah_buku:
    print('Semua buku bisa dipahami')
else:
    print('Tidak semua buku bisa dipahami')