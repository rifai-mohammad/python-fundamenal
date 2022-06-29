daftar_buku = ['Seven Habits', 'How To Influence People', 'First Thing First', '4DX']
print('Tampilkan semua daftar buku')
print(daftar_buku)

print('\nTampilkan semua daftar buku dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan daftar buku sesuai indeks')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan daftar buku dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nTambahkan daftar buku baru')
daftar_buku.append('Teori Akuntansi')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMengganti elemen pertama')
daftar_buku = ['Seven Habits', 'How To Influence People', 'First Thing First', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMengambil buku kedua')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMemunculkan buku yang sudah diambil')
print(buku)
