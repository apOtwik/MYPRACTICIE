
print("""
 ********  **      **   **   **  **
    **     **      **   **   ** ** 
    **     **  **  **   **   ****  
    **      ** ** **    **   ** ** 
    **       **  **     **   **  **
""")
alpha = [
    "   ***     **      ******   **  **     ***  ",
    " **   **   **      **   **  **  **   **   ** ",
    " *******   **      ******   ******   *******",
    " **   **   **      **       **  **   **   ** ",
    " **   **   ******  **       **  **   **   ** "
]
for line in alpha:
    print(line)
print()
print('PRODUCED BY TWIK')



#WORK PLACE DONE!
#CALCULATOR
while True:
    print("-" * 30)
    print("Для выхода введи 'exit' вместо числа")

    try:
        user_input1 = input("Введи первое число: ")
        if user_input1.lower() == 'exit':
            break
        n1 = int(user_input1)

        n2 = int(input("Введи второе число: "))
    except ValueError:
        print("Ошибка: Нужно вводить только целые числа!")
        continue

    print("Выбери операцию: +, -, *, /, **, //, %")
    symba = input("Операция: ")

    # Логика калькулятора
    if symba == '+':
        print(f"Результат: {n1 + n2}")

    elif symba == '-':
        print(f"Результат: {n1 - n2}")

    elif symba == '*':
        print(f"Результат: {n1 * n2}")

    elif symba == '/':
        if n2 != 0:
            print(f"Результат: {n1 / n2}")
        else:
            print("Ошибка: На ноль делить нельзя!")

    elif symba == '**':
        print(f"Результат: {n1 ** n2}")

    elif symba == '//':
        if n2 != 0:
            print(f"Результат: {n1 // n2}")
        else:
            print("Ошибка: Деление на ноль!")

    elif symba == '%':
        if n2 != 0:
            print(f"Результат: {n1 % n2}")
        else:
            print("Ошибка: Деление на ноль!")

    else:
        # Вот тут магия: печатаем твою фразу и возвращаемся в начало цикла
        print('\nТЫ ШО ЕБЛАН? Выбери нормальный символ из списка!\n')
        continue  # Переход на начало цикла while

    # Спрашиваем, продолжаем ли работу
    choice = input("\nХочешь посчитать еще раз? (да/нет): ").lower()
    if choice != 'да' and choice != 'д' and choice != 'y':
        print("Hell yeah!")
        break
