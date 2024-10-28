# Запит у користувача числа n
n = int(input("Введіть число n: "))

for num in range(n, 0, -1):
    if num % 2 == 0:
        print(num, end=' ')