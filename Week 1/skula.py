# siswas = ["Aldi","Gijen","Rapi","Rapa","Anwar"]

# for siswa in siswas:
#     print(siswa)

# siswas =  {
#     "Aldi": "Semea",
#     "Gijen": "Semea",
#     "Rapi": "Semea",
#     "Rapa": "Smansa",
#     "Anwar": "Nonim",
# }

# for siswa in siswas:
#     print(siswa, siswas[siswa], sep=",Sekolah ")

skolah  = [
    {"Name" : "Adli", "Alamat" : "Cipoho", "Satpam" : "Bang Satria"},
    {"Name" : "Gijen", "Alamat" : "Cidahu","Satpam" : "Bang Kendi"}
]

for i in skolah:
    print(i['Name'],i['Alamat'],i['Satpam'], sep=", ")