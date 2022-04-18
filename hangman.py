import  random
from kata import kata_kata
import string

def dapatkan_kata(kata_kata):
    kata = random.choice(kata_kata)
    while '-' in kata or ' ' in kata:
        kata = random.choice(kata_kata)

    return kata.upper()

def hangman():
    nyawa = 6
    kata = dapatkan_kata(kata_kata) #kata yang digunakan
    huruf_kata = set(kata) #huruf dalam kata
    huruf_digunakan = set()  # kata yang ditebak
    alfabet = set(string.ascii_uppercase)

    while len(huruf_kata) > 0 and nyawa > 0 :

        print("kamu telah menggunakan huruf ini :", ' '.join(huruf_digunakan))

        list_kata = [huruf if huruf in huruf_digunakan else '-' for huruf in kata]
        print('huruf baru : ', ' '.join(list_kata))
        print(f"nyawa : {nyawa}")
        huruf_tebakan = input("masukan huruf : ").upper()
        if huruf_tebakan in alfabet - huruf_digunakan :
            huruf_digunakan.add(huruf_tebakan)
            #print(huruf_digunakan)
            #print(huruf_kata)
            if huruf_tebakan in huruf_kata:
                huruf_kata.remove(huruf_tebakan)
                #print(huruf_kata)
            else :
                nyawa = nyawa - 1

        elif huruf_tebakan in huruf_digunakan:
            print("Kamu telah menggunkan huruf ini")
        else:
            print("Masukan huruf jangna karakter lain")

    if nyawa == 0:
        print(f"Maaf anda gagal, kata : {kata}")
    else:
        print(f"YES KAMU MENEBAKNYA {kata}")


hangman()
