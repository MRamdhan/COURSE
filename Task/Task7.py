class Kendaraan:
    def __init__(self, jenis, jarak):
        self.jenis = jenis
        self.jarak = jarak

class Transportasi:
    def __init__(self):
        self.kendaraan = []

    def tambah_kendaraan(self, jenis, jarak):
        self.kendaraan.append(Kendaraan(jenis, jarak))

    def total_jarak(self):
        return sum(k.jarak for k in self.kendaraan)

def main():
    transportasi = Transportasi()
    jumlah = int(input("Jumlah kendaraan: "))
    for i in range(jumlah):
        jenis, jarak = input(f"Data kendaraan {i+1} (jenis_kendaraan jarak): ").split()
        transportasi.tambah_kendaraan(jenis, int(jarak))

    print(f"Total jarak yang ditempuh semua kendaraan : {transportasi.total_jarak()}")

if __name__ == "__main__":
    main()
