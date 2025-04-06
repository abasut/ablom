number = input("Введите номер квартиры:")


if not number.isdigit():
    print ("ВВЕДИТЕ ЦИФРУ!!!")
elif number.isdigit():
    entrance = (int(number)-1) // 20 + 1 
    etazh = (int(number)-1)% 20 // 4 + 1
    print (f"Подъезд: {entrance}")
    print (f"Этаж: {etazh}")