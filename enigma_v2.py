import string
import random
import json
import os

# Создаем наборы алфавитов
english_alphabet = string.ascii_uppercase
russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

ROTORS_FILE = 'rotors.json'

def create_rotor(alphabet):
    """Создаем ротор в виде перемешанного алфавита"""
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

def reverse_rotor(rotor):
    """Создаем обратную карту для ротора"""
    return {v: k for k, v in rotor.items()}

def save_rotors(rotors):
    """Сохраняем роторы в файл"""
    with open(ROTORS_FILE, 'w') as file:
        json.dump(rotors, file)

def load_rotors():
    """Загружаем роторы из файла, если он существует"""
    if os.path.exists(ROTORS_FILE):
        with open(ROTORS_FILE, 'r') as file:
            return json.load(file)
    return None

def generate_rotors(alphabet):
    """Генерация новых роторов"""
    rotor1 = create_rotor(alphabet)
    rotor2 = create_rotor(alphabet)
    rotor3 = create_rotor(alphabet)
    return [rotor1, rotor2, rotor3]

def encrypt_decrypt(message, rotors, reverse=False):
    """Функция для шифрования и расшифровки сообщения"""
    result = []
    message = message.upper()

    if reverse:
        rotors = [reverse_rotor(rotor) for rotor in reversed(rotors)]
    
    for char in message:
        if char in rotors[0]:  # Только символы из алфавита проходят через роторы
            for rotor in rotors:
                char = rotor[char]  # Преобразуем символ с каждым ротором
        result.append(char)

    return ''.join(result)

def main():
    print("Выберите язык: 1 - Английский, 2 - Русский")
    language_choice = input()

    if language_choice == '1':
        alphabet = english_alphabet
    elif language_choice == '2':
        alphabet = russian_alphabet
    else:
        print("Неверный выбор языка!")
        return

    # Загружаем роторы из файла, если они уже существуют
    rotors = load_rotors()

    if rotors is None:
        print("Роторы не найдены, создаем новые...")
        rotors = generate_rotors(alphabet)
        save_rotors(rotors)
        print("Роторы сохранены!")

    else:
        print("Роторы загружены из файла.", rotors)

    while True:
        print("Выберите действие: 1 - шифрование, 2 - расшифровка, 3 - сброс роторов, 4 - выход")
        choice = input()
        
        if choice == '4':
            print("Выход!")
            break

        if choice == '3':
            print("Генерация новых роторов...")
            rotors = generate_rotors(alphabet)
            save_rotors(rotors)
            print("Новые роторы сгенерированы и сохранены.")
            continue

        if choice not in ['1', '2']:
            print("Неверный выбор!")
            continue

        print("Введите последовательность роторов (например: 1 2 3):")
        rotor_order = input()

        try:
            rotor_indices = list(map(int, rotor_order.split()))
            selected_rotors = [rotors[i - 1] for i in rotor_indices]  # Выбираем роторы по порядку
        except (ValueError, IndexError):
            print("Неверный ввод последовательности роторов!")
            continue

        if choice == '1':
            message = input("Введите сообщение для шифрования: ")
            encrypted_message = encrypt_decrypt(message, selected_rotors, reverse=False)
            print("Зашифрованное сообщение:", encrypted_message)
        
        elif choice == '2':
            message = input("Введите сообщение для расшифровки: ")
            decrypted_message = encrypt_decrypt(message, selected_rotors, reverse=True)
            print("Расшифрованный текст:", decrypted_message)

if __name__ == "__main__":
    main()
