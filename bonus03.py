def calculate_tax(salary):
    if salary > 5_000_000:
        return salary * 0.2
    return salary * 0.13

def calculate_net_salary(salary):
    return salary - calculate_tax(salary)

def main():
    salary = float(input("Oyligingiz: "))

    tax = calculate_tax(salary)
    net_salary = calculate_net_salary(salary)

    print(f"soliq: {tax:,.2f}, daromad: {net_salary:,.2f}")

main()