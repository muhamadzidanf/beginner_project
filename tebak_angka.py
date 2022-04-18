import random

def tebak(x):
    angka_random = random.randint(1, x)
    angka = 0
    while angka_random != angka:
        angka = int(input('masukan tebakan : '))
        print(f"tebakan kamu : {angka}")
        if angka > angka_random:
            print("angka kamu terlalu besar")
        elif angka < angka_random:
            print("angka kamu telalu kecil")
    print(f"tebakan kamu benar : {angka}")

def komputer_tebak(x):
    low  = 1
    high = x
    tanggapan = ''
    while tanggapan != 'b':
        angka = int(random.randint(low, high))

        if low == high:
            angka = low  # mau high/low sama aja karena disini posisinya low=high
            break
        tanggapan = input(f"-> {angka} : [B] untuk benar [T] untuk terlalu tinggi [R] terlalu rendah : ").lower()
        if tanggapan == 't':
            high = angka - 1
        elif tanggapan == 'r':
            low = angka + 1
        print(f"low :{low}, high{high}")
    print(f"yes angka ditebak komputer : {angka}")





komputer_tebak(1000)
tebak(10)