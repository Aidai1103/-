import random 
print("Угадайте число от 1 до 100, удачи!")

number = random.randint(1,100)
attempts=0

while True:
    guess=int(input("Ваш вариант:"))
    attempts +=1
    difference = abs(number-guess)

    if guess==number:
        print("Поздравляю! Вы угадали число! ")
        break 
    elif difference>30:
        print("Холодно!")
    elif difference>20:
        print("Прохладно!")
    elif difference>10:
        print("Тепло!")
    else:
        print("Жарко!")
