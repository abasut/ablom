from random import randint
def coin_simulator():
    coin = randint(0,1)
    if coin == 0:
        print("Орёл")
    else:
        print("Решка")
coin_simulator()


