'''
Nama: Harits Nur Allam Muhammad
Kelas: RPL 1A
NIM: 2405350
'''

def tubeVolume(range,height):
    phi = 22/7
    volume = phi * range**2 * height
    result = f"Volume tabung adalah {volume:.2f} cm"
    return result

r = int(input("\nMasukkan jari-jari alas tabung: "))
tinggi = int(input("Masukkan tinggi tabung: "))

print(F"\n{tubeVolume(r,tinggi)}\n")