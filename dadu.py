import random

def ambil():
    i = 0
    hasil = []
    while i < 2:
        # print('no : ', i)
        angka_random = random.randint(1, 6)
        hasil.append(angka_random)
        # print(angka_random)
        i += 1
    tup = tuple(hasil)
    return tup

print("dadu yang kamu dapatkan :")
for item in ambil():
    print(f"-> [{item}]")
