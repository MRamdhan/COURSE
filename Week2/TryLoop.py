nama = input("Masukan nama : ")
while True:
    try:
        nim = int(input("Masukan nim anda : "))
        
    except ValueError:
        print("Terdapat kesalahan input, nim harus berupa angka.")
print(f"Hallo {nama}, nim kamua adalah {nim}")  