def ask_question(question: str, correct_answer: str):
    print(question)
    user_answer = input("Javobingiz: ")
    
    if check_answer(user_answer, correct_answer):
        print("To'g'ri javob!")
    else:
        print("Noto'g'ri javob!")

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

ask_question("O'zbekiston poytaxti qaysi shahar?", "Toshkent")