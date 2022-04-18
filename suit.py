import  random
import string

def main():
    user = ''
    komputer = ''
    while user == komputer:
        user = input("[k] kertas, [g] gunting, [b] batu : ")
        komputer = random.choice(['k','g','b'])

        if user == komputer:
            print(f"kamu {user} dan komputer {komputer}: SERI")

    if menang(user, komputer):
        return f"kamu {user} dan komputer {komputer}: Kamu MENANG"

    return f"kamu {user} dan komputer {komputer} Kamu KALAH"

def menang(user, lawan):
    if (user == 'g' and lawan == 'k') or (user == 'k' and lawan == 'b') or (user == 'b' and lawan == 'g'):
        return True


print(main())