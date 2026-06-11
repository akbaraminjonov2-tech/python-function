def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To'g'ri topdingiz!")
    else:
        print("Xato, qayta urinib ko'ring.")

secret = 7  # sirli son
guess = int(input("Taxminingizni kiriting: "))

result = check_guess(secret, guess)
print_result(result)