# List
list = ["a", 1, 2.5, True]

print(f"Ini list item pertama s.d. ke-3, yaitu: {list[:3]} (index-nya :3)")
print(f"Ini list item ke-3 s.d. terakhir, yaitu: {list[1:]} (index-nya 1:)")
print(f"Ini list item ke-4, yaitu: {list[3]} (index-nya 3)")
print(f"Ini list item ke-4, yaitu: {list[-1]} (index-nya -1)")

list.append("hero")
print(f"List setelah di append: {list} (.append) (ditambahkan di index terakhir)")

list.insert(2, "b")
print(f"menambahkan item list ke index-2: {list} (.insert)")

new = [6, 89, 400]
list.extend(new)
print(f"List item (list) ditambahkan dari list lainnya (new) dari index terakhir: {list} (.extend)")

list.remove("hero")
print(f"Menghilangkan \"hero\" dari list: {list} (.remove)")

list.pop(1)
print(f"Menghapus index-1 di list: {list} (.pop)")

if "a" in list:
    print("a in list")

list.sort()
print(f"List setelah di sort: {list} (.sort())")

del list # Menghapus list

# Tuple
tuple = ("a", 1, 2.5, True)

tupleToList = list(tuple)

print(f"Merubah tuple: {tuple} ke list: {tupleToList}")

# Set
set = {"a", 1, 2.5, True}

# Dictionary
dict = {
    "name": "Harits",
    "grade": "1A",
    "NIM": "2405350",
    "live": True
}

# Looping
for i in range(8):
    print(f"test {i}")

for i in range(0, 8, 1):
    print(f"test {i}")

x = [1, 3, 6, 8, 13, 50]
for y in x:
    print(y)