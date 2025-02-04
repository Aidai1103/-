weight = float(input("Введите свой вес: "))
height = float(input("Введите свой рост: "))

height_in_metrs = height / 100
bmi = weight / (height_in_metrs ** 2)

print("Твой bmi to:", bmi)

if bmi < 18.5:
    print("Недостаточно массы")
elif bmi >= 18.5 and bmi < 24.9:
    print("Нормальный вес")
elif bmi >= 25 and bmi < 29.9:
    print("Избыточный вес")
elif bmi >= 30 and bmi < 34.9:
    print("Ожирение 1 степени")
elif bmi >= 35 and bmi < 39.9:
    print("Ожирение 2 степени")
elif bmi >= 40:
    print("Ожирение 3 степени")