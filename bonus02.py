def is_strong_password(password: str):
    return len(password) >= 8

password = input("parolni kiriting: ")

if is_strong_password(password):
    print("kuchli parol: ")

else: 
    print("kuchsiz parol: ")