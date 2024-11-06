'''
Nama: Harits Nur Allam Muhammad
NIM: 2405350
Kelas: RPL 1A
'''
def fibonacci(r):
    fibList = []
    for x in range(r):
        if x == 0:
            fibList.append(x)
        elif x == 1:
            fibList.append(x)
        else:
            nextFib = fibList[x-2] + fibList[x-1]
            fibList.append(nextFib)
    return fibList

n = int(input("\nMasukkan panjang deret fibonacci: "))

print(f"\nDeret fibonacci: {fibonacci(n)}\n")