import random

def get_random_word():
    words = ["оптика", "решетка", "свет", "закон", "отражение", "преломление", "дифракция", "линза", "глаз", "источник"]
    return random.choice(words).lower()

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head only
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def play():
    print("Добро пожаловать в игру Виселица по теме оптика!")
    word = get_random_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    while tries > 0 and len(word_letters) > 0:
        print(display_hangman(tries))
        print("Угаданные буквы: ", " ".join(sorted(guessed_letters)))
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Слово: ", " ".join(word_display))

        guess = input("Введите букву: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue
        if guess in guessed_letters:
            print("Вы уже угадывали эту букву.")
            continue

        guessed_letters.add(guess)
        if guess in word_letters:
            word_letters.remove(guess)
            print("Верно!")
        else:
            tries -= 1
            print("Неверно!")

    if len(word_letters) == 0:
        print(f"Поздравляем! Вы угадали слово: {word}")
    else:
        print(display_hangman(tries))
        print(f"Вы проиграли. Загаданное слово было: {word}")

if __name__ == "__main__":
    play()