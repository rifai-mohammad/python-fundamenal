# main
print('Budi pergi ke toko')

stock_botol_susu = 50
stock_butir_telur = 100

print(f'stok susu di toko adalah {stock_botol_susu} botol')
print(f'stok telur di toko adalah {stock_butir_telur} butir')

if stock_botol_susu > 0:
    print('budi mengecek harganya')
    if stock_butir_telur >= 0:
     print ('Budi membeli 1 botol susu')
    else:
     print('budi membeli 6 botol susu')
    if stock_butir_telur >= 0:
        print('Budi juga membeli 6 butir telur')
else:
    print('Budi tidak jadi membeli susu')