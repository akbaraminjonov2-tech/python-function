def calculate_bmi(weight: float, height: float):
    return weight / (height ** 2)

def bmi_status(bmi: float):
    if bmi < 18.5:
        return "Kam vazn"
    elif bmi < 25:
        return "Normal vazn"
    elif bmi < 30:
        return "Ortiqcha vazn"
    else:
        return "Semizlik"

weight = float(input("Vazningizni kiriting (kg): "))
height = float(input("Bo'yingizni kiriting (m): "))

bmi = calculate_bmi(weight, height)

print("BMI =", round(bmi, 2))
print("Holati:", bmi_status(bmi))