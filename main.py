import math


def calculate_error():
    print("Калькулятор погрешностей")
    print("=" * 30)
    print("Операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (^)")
    print("6. Квадратный корень (√)")
    print("=" * 30)


    while True:
        try:
            choice = int(input("Выберите операцию (1-6): "))
            if 1 <= choice <= 6:
                break
            else:
                print("Пожалуйста, введите число от 1 до 6")
        except ValueError:
            print("Пожалуйста, введите целое число")


    if choice == 6:
        print("\nИзвлечение квадратного корня")
        while True:
            try:
                x = float(input("Введите число: "))
                dx = float(input("Введите абсолютную погрешность числа: "))
                if x < 0:
                    print("Нельзя извлечь корень из отрицательного числа")
                    continue
                if dx < 0:
                    print("Погрешность не может быть отрицательной")
                    continue
                break
            except ValueError:
                print("Пожалуйста, введите числа")


        result = math.sqrt(x)

        error = (1 / (2 * math.sqrt(x))) * dx if x > 0 else 0

        print("\nРезультат:")
        print(f"√({x} ± {dx}) = {result:.6f} ± {error:.6f}")

    else:
        print("\nБинарная операция")
        while True:
            try:
                x = float(input("Введите первое число: "))
                dx = float(input("Введите абсолютную погрешность первого числа: "))
                y = float(input("Введите второе число: "))
                dy = float(input("Введите абсолютную погрешность второго числа: "))

                if choice == 4 and y == 0:
                    print("Деление на ноль невозможно")
                    continue
                if dx < 0 or dy < 0:
                    print("Погрешность не может быть отрицательной")
                    continue
                break
            except ValueError:
                print("Пожалуйста, введите числа")

        if choice == 1:
            result = x + y
            error = dx + dy
            operation = "+"

        elif choice == 2:
            result = x - y
            error = dx + dy
            operation = "-"

        elif choice == 3:
            result = x * y
            if x != 0 and y != 0:
                rel_error_x = dx / abs(x)
                rel_error_y = dy / abs(y)
                error = abs(result) * (rel_error_x + rel_error_y)
            else:
                error = 0
            operation = "*"

        elif choice == 4:
            result = x / y
            if x != 0 and y != 0:
                rel_error_x = dx / abs(x)
                rel_error_y = dy / abs(y)
                error = abs(result) * (rel_error_x + rel_error_y)
            else:
                error = 0
            operation = "/"

        elif choice == 5:
            result = x ** y
            if x > 0:
                if x != 0:
                    rel_error_x = dx / abs(x)
                else:rel_error_x = 0
                error = abs(result) * (abs(y) * rel_error_x + abs(math.log(abs(x))) * dy)
            else:
                error = 0
            operation = "^"

        print("\nРезультат:")
        print(f"({x} ± {dx}) {operation} ({y} ± {dy}) = {result:.6f} ± {error:.6f}")

    print(f"\nИтог: {result:.6f} ± {error:.6f}")

    if error > 0:

        error_order = 10 ** math.floor(math.log10(error))

        if error / error_order < 3:
            rounded_error = round(error / error_order, 1) * error_order
        else:
            rounded_error = round(error / error_order) * error_order
        if error_order >= 1:
            decimals = 0
        else:
            decimals = -int(math.floor(math.log10(error_order)))

        rounded_result = round(result, decimals)

        print(f"\nРекомендуемое округление:")
        print(f"{rounded_result} ± {rounded_error}")

print("ПРОГРАММА ЗАПУЩЕНА ")

while True:
    calculate_error()
    print("\n" + "=" * 30)

    again = input("Хотите выполнить еще расчет? (да/нет): ").lower()
    if again not in ['да', 'д', 'yes', 'y']:
        print("До свидания!")
        break

print("ПРОГРАММА ЗАВЕРШЕНА")