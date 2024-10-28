def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Ділення на нуль"
        else:
            return a / b
    else:
        return "Невідома операція"

a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
operation = input("Введіть операцію (+, -, *, /): ")

result = calculator(a, b, operation)
print("Результат:", result)
