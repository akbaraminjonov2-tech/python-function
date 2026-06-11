def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    return age 

def main():
    birth_year = int(input("Tug'ilgan yilingiz: "))
    age = calculate_age(birth_year, 2026)

    print(f" {age} yosh")

main()