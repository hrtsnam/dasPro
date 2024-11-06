'''
Nama: Harits Nur Allam Muhammad
NIM: 2405350
Kelas: RPL 1A
'''

def countTime(hour1,minute1,second1,hour2,minute2,second2):
    hour = hour2 - hour1
    if hour1 > hour2:
        hour = hour + 12
    minute = minute2 - minute1
    if minute1 > minute2:
        minute = minute + 60
    second = second2 - second1
    if second1 > second2:
        second = second + 60

    return f"\nSelisih waktu: {hour} jam - {minute} menit - {second} detik\n"

print("\n!!! NOTE: Format waktu 12 jam !!!")
print("\n>> Waktu mulai <<")
startH = int(input("Jam: "))
startM = int(input("Menit: "))
startS = int(input("Detik: "))

print("\n>> Waktu selesai <<")
finH = int(input("Jam: "))
finM = int(input("Menit: "))
finS = int(input("Detik: "))

print(countTime(startH,startM,startS,finH,finM,finS))