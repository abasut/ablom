import math

def calculate_error():
    print("Калькулятор погрешностей")
    print("=" * 40)
    print("Операции:")
    print("1. Сложение (a + b)")
    print("2. Вычитание (a - b)")
    print("3. Умножение (a × b)")
    print("4. Деление (a / b)")
    print("5. Возведение в степень (a^n)")
    print("6. Квадратный корень (√a)")
    print("=" * 40)
    
    while True:
        try:
            choice = int(input("Выберите операцию (1-6): "))
            if 1 <= choice <= 6:
                break
            else:
                print("Пожалуйста, введите число от 1 до 6")
        except ValueError:
            print("Пожалуйста, введите целое число")
    
    if choice == 5:  
        print("\n--- Возведение в степень a^n ---")
        while True:
            try:
                a = float(input("Введите число a: "))
                da = float(input("Введите абсолютную погрешность Δa: "))
                n = float(input("Введите степень n: "))
                
                if da < 0:
                    print("Погрешность не может быть отрицательной")
                    continue
                break
            except ValueError:
                print("Пожалуйста, введите числа")
        
        result = a ** n
        
        if n != 0:
            error_abs = abs(n) * (abs(a) ** (n - 1)) * da
        else:
            error_abs = 0 
        
        if a != 0:
            error_rel = abs(n) * (da / abs(a))
        else:
            error_rel = 0
        
        print(f"a = {a} ± {da}")
        print(f"n = {n}")
        print(f"a^{n} = {result:.6f}")
        print(f"Абсолютная погрешность  = {error_abs:.6f}")
        print(f"Относительная погрешность  = {error_rel:.6f}")
        print(f"Итог: {result:.6f} ± {error_abs:.6f}")
        
    elif choice == 6: 
        print("\n--- Извлечение квадратного корня √a ---")
        while True:
            try:
                a = float(input("Введите число a: "))
                da = float(input("Введите абсолютную погрешность Δa: "))
                
                if a < 0:
                    print("Нельзя извлечь корень из отрицательного числа")
                    continue
                if da < 0:
                    print("Погрешность не может быть отрицательной")
                    continue
                break
            except ValueError:
                print("Пожалуйста, введите числа")
        
        n = 2 
        result = math.sqrt(a)
        
        if a > 0:
            error_abs = da / (n * (a ** ((n - 1) / n)))
        else:
            error_abs = 0
        
        if a != 0:
            error_rel = (da / abs(a)) / n
        else:
            error_rel = 0
        
        print("\nРезультат по формулам из таблицы:")
        print(f"a = {a} ± {da}")
        print(f"√a = {result:.6f}")
        print(f"Абсолютная погрешность Δ = {error_abs:.6f}")
        print(f"Относительная погрешность δ = {error_rel:.6f}")
        print(f"Итог: {result:.6f} ± {error_abs:.6f}")
        
    else:  
        print("\n--- Операция с двумя числами ---")
        while True:
            try:
                a = float(input("Введите число a: "))
                da = float(input("Введите абсолютную погрешность Δa: "))
                b = float(input("Введите число b: "))
                db = float(input("Введите абсолютную погрешность Δb: "))
                
                if choice == 4 and b == 0:  
                    print("Деление на ноль невозможно")
                    continue
                if da < 0 or db < 0:
                    print("Погрешность не может быть отрицательной")
                    continue
                break
            except ValueError:
                print("Пожалуйста, введите числа")
        
        if choice == 1:  # Сложение
            result = a + b         
            error_abs = da + db
            operation = "+"
            
        elif choice == 2:  # Вычитание
            result = a - b
            error_abs = da + db
            operation = "-"
            
        elif choice == 3:  # Умножение
            result = a * b
            error_abs = abs(a) * db + abs(b) * da
            if a != 0 and b != 0:
                error_rel = (da / abs(a)) + (db / abs(b))
            else:
                error_rel = 0
            operation = "×"
            
        elif choice == 4:  # Деление
            result = a / b
            error_abs = (abs(b) * da + abs(a) * db) / (b ** 2)
            if a != 0 and b != 0:
                error_rel = (da / abs(a)) + (db / abs(b))
            else:
                error_rel = 0
            operation = "/"
        
        print("\nРезультат по формулам из таблицы:")
        print(f"a = {a} ± {da}")
        print(f"b = {b} ± {db}")
        
        if choice == 1 or choice == 2:
            print(f"a {operation} b = {result:.6f}")
            print(f"Абсолютная погрешность Δ = {error_abs:.6f}")
            print(f"Итог: {result:.6f} ± {error_abs:.6f}")
        else:
            print(f"a {operation} b = {result:.6f}")
            print(f"Абсолютная погрешность Δ = {error_abs:.6f}")
            print(f"Относительная погрешность δ = {error_rel:.6f}")
            print(f"Итог: {result:.6f} ± {error_abs:.6f}")
    
    if error_abs > 0:
        error_order = 10 ** math.floor(math.log10(error_abs))
        
        if error_abs / error_order < 3:
            rounded_error = round(error_abs / error_order, 1) * error_order
        else:
            rounded_error = round(error_abs / error_order) * error_order
        
        if error_order >= 1:
            decimals = 0
        else:
            decimals = -int(math.floor(math.log10(error_order)))
        
        rounded_result = round(result, decimals)
        
        print(f"\nРекомендуемое округление:")
        print(f"{rounded_result} ± {rounded_error}")
        
        result_str = f"{rounded_result:.{max(decimals, 0)}f}"
        error_str = f"{rounded_error:.{max(decimals, 0)}f}"
        print(f"Проверка: {result_str} ± {error_str}")

while True:
    calculate_error()
    print("\n" + "=" * 40)
    
    again = input("Выполнить еще расчет? (да/нет): ").lower()
    if again not in ['да', 'д', 'yes', 'y']:
        print("Работа завершена. До свидания!")
        break

print("=" * 40)