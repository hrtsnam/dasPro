'''
Nama: Harits Nur Allam Muhammad
NIM: 2405350
Kelas: RPL/1A
'''

# Tuple buah
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")
print("Tuple awal:", buah)

# Nomor 6
print("Mengambil tuple items ke-2 s.d. ke-5:", buah[1:5])

# Nomor 7
manipulate = list(buah)
manipulate.pop(3)
buah = tuple(manipulate)
print("Menghapus item \'durian\' dari tuple buah:", buah)

# Nomor 8
manipulate = list(buah)
manipulate.insert(2, "manggis")
buah = tuple(manipulate)
print("Menambah item \'manggis\' diantara item \'jeruk\' dan \'ceri\':", buah)