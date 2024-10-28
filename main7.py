def determine_grade(score):
    if 0 <= score <= 49:
        return "Незадовільно"
    elif 50 <= score <= 69:
        return "Задовільно"
    elif 70 <= score <= 89:
        return "Добре"
    elif 90 <= score <= 100:
        return "Відмінно"
    else:
        return "Неправильний бал"

score = int(input("Введіть кількість балів студента: "))
print("Оцінка студента:", determine_grade(score))
