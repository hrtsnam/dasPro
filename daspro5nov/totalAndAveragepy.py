'''
Nama: Harits Nur Allam Muhammad
Kelas: RPL 1A
NIM: 2405350
'''

def totalAndAverage(*num):
    total = 0
    for x in list(num):
        total += x
    average = total / len(num)

    return print(f"\nTotalnya adalah {total} dan rata-ratanya adalah {int(average)}\n")

userAskList = []

while True:
    userAsk = int(input("\nMasukkan angka: "))
    userAskList.append(userAsk)
    askIfDone = input("Ada lagi? (y or n) ").lower()
    if askIfDone == "n":
        break
    elif askIfDone == "y":
        continue
    else:
        print("\n>> Invalid choice <<")

totalAndAverage(*userAskList)