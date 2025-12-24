import math

def read_value():
    x = float(input("Введите число x: "))
    dx = float(input("Введите его абсолютную погрешность Δx: "))
    return x, dx

def show(x, dx):
    print(f"Результат: {x} ± {dx}")

def add(a, da, b, db):
    return a + b, da + db          # Δ(a+b) = Δa + Δb

def sub(a, da, b, db):
    return a - b, da + db          # Δ(a-b) = Δa + Δb 

def mul(a, da, b, db):
    # Δ(ab) ≈ |b|Δa + |a|Δb
    return a * b, abs(b) * da + abs(a) * db

def div(a, da, b, db):
    # Δ(a/b) ≈ (Δa/|b|) + (|a|Δb/|b|²)
    value = a / b
    d = da / abs(b) + abs(a) * db / (abs(b) ** 2)
    return value, d

def power(a, da, n):
    # Δ(a^n) ≈ |n * a^(n-1)| Δa
    value = a ** n
    d = abs(n * (a ** (n - 1))) * da
    return value, d

def root(a, da):
    # y = sqrt(a), dy ≈ Δa / (2*sqrt(a))
    value = math.sqrt(a)
    d = da / (2 * value)
    return value, d

def main():
    print("Калькулятор с погрешностями.")
    x, dx = read_value()
    while True:
        print("\nТекущее значение: ", end="")
        show(x, dx)
        print("Операции:")
        print("1 — сложить")
        print("2 — вычесть")
        print("3 — умножить")
        print("4 — разделить")
        print("5 — возвести в степень")
        print("6 — извлечь корень")
        print("0 — выход")

        cmd = input("Выберите операцию: ")

        if cmd == "0":
            break
        elif cmd in ("1", "2", "3", "4"):
            print("Введите второе число:")
            y, dy = read_value()
            if cmd == "1":
                x, dx = add(x, dx, y, dy)
            elif cmd == "2":
                x, dx = sub(x, dx, y, dy)
            elif cmd == "3":
                x, dx = mul(x, dx, y, dy)
            elif cmd == "4":
                x, dx = div(x, dx, y, dy)
        elif cmd == "5":
            n = float(input("Степень n: "))
            x, dx = power(x, dx, n)
        elif cmd == "6":
            x, dx = root(x, dx)
        else:
            print("Неизвестная команда")

    print("\nИтоговый результат:")
    show(x, dx)

if __name__ == "__main__":
    main()