nama_buah = input("Nama Buah :")
if " " in nama_buah:
    print("Nama Buah Tidak Boleh Menggunakan Spasi!")
elif len(nama_buah) > 20:
    print("Nama buah terlalu panjang!")
else:    
    harga_jual = float(input("Masukan harga jual per kilo :  "))
    kg_terjual = int(input("Masukan jumlah kilogram yang terjual :"))
    total_keuntungan = harga_jual * kg_terjual

    print(f"Buah {nama_buah} menghasilkan keuntungan: {total_keuntungan:.2f}")