'''
Nama: Harits Nur Allam Muhammad
NIM: 2405350
Kelas: RPL 1A
'''
# fungsi login
def login(username,password):
    if password == "Latihan":
        print("Status: Login berhasil, anda masuk ke halaman utama.\n")
        print(f"Selamat datang, {username}!")
        print("\n----------------------------------------------------")
        result = 1
        return result
    elif chanceCheck < 3:
        if chanceLeft != 0:
            print(f"Password salah. Kesempatan: {chanceLeft} kali lagi\n")
        else:
            print("Status: Login gagal, anda telah dikeluarkan.")
            print("\n----------------------------------------------------")

chanceGiven = 3
chanceCheck = 0
chanceLeft = 2

print("\nL   O   G   I   N")
while chanceCheck < chanceGiven:
    print("----------------------------------------------------\n")
    uN = input("Username: ")
    pW = input("Password: ")
    print("\n----------------------------------------------------\n")
    log = login(uN,pW)
    if log == 1:
        break
    chanceCheck+=1
    chanceLeft-=1