# Функція для додавання двох чисел
def додавання(a, b):
    сума = a + b
    return сума

# Введення чисел від користувача
число1 = float(input("Введіть перше число: "))
число2 = float(input("Введіть друге число: "))

# Виклик функції для додавання та виведення результату
результат = додавання(число1, число2)
print("Сума:", результат)