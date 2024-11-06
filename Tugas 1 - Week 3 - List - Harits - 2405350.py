'''
Nama: Harits Nur Allam Muhammad
NIM: 2405350
Kelas: RPL/1A
'''

# List buah
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print("List awal:", buah)

# Nomor 1
print("Mengambil list items ke-2 s.d. ke-5:", buah[1:5])

# Nomor 2
buah.pop(4)
print("Menghapus item \'apel\' ke-2 di list buah:", buah)

# Nomor 3
buah[2] = "cherry"
print("Mengganti item \'ceri\' menjadi \'cherry\':", buah)

# Nomor 4
buah.insert(3, "strawberry")
print("Menambahkan item \'strawberry\' ke dalam index ke-3:", buah)

# Nomor 5
buah.sort()
print("Mengurutkan list buah sesuai abjad:", buah)
