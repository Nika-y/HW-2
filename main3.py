import random

number = random.randint(1, 10)

for attempt in range(3):
    guess = int(input("Введіть ваше число (від 1 до 10): "))

    if guess > number:
        print("Менше")
    elif guess < number:
        print("Більше")
    else:
        print("Вітаю! Ви вгадали число!")
        break
else:
    print(f"На жаль, ви не вгадали. Загадане число: {number}")
