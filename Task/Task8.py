def huruf_awal_vokal(nama):
    return nama[0].lower() in 'aeiou'

def filter_nama_kucing(nama_kucing):
    nama_valid = []
    for nama in nama_kucing:
        if len(nama) > 4 and huruf_awal_vokal(nama):
            nama_valid.append(nama)
    return nama_valid

def main():
    n = int(input("Masukkan jumlah nama kucing: "))
    nama_kucing = []
    for i in range(n):
        nama = input(f"Masukkan nama kucing ke {i+1}: ")
        nama_kucing.append(nama)

    nama_valid = filter_nama_kucing(nama_kucing)

    print("Nama kucing yang valid:")
    for nama in nama_valid:
        print(nama)

if __name__ == "__main__":
    main()
