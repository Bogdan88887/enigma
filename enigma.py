def encrypt_decrypt(message, rotors, reflector):
    result = []
    for char in message:
        if char in rotors:
            char = rotors[char]
        elif char in reflector:
            char = reflector[char]
        result.append(char)
    return ''.join(result)

def main():
    rotors = {
        'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J',
        'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q',
        'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W', 'U': 'X',
        'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C',
        'А': 'Е', 'Б': 'Ё', 'В': 'Ж', 'Г': 'З', 'Д': 'И', 'Е': 'Й', 'Ё': 'К',
        'Ж': 'Л', 'З': 'М', 'И': 'Н', 'Й': 'О', 'К': 'П', 'Л': 'Р', 'М': 'С',
        'Н': 'Т', 'О': 'У', 'П': 'Ф', 'Р': 'Х', 'С': 'Ц', 'Т': 'Ч', 'У': 'Ш',
        'Ф': 'Щ', 'Х': 'Ъ', 'Ц': 'Ы', 'Ч': 'Ь', 'Ш': 'Э', 'Щ': 'Ю', 'Ъ': 'Я',
        'Ы': 'А', 'Ь': 'Б', 'Э': 'В', 'Ю': 'Г', 'Я': 'Д'
    }

    reflector = {
        'A': 'Y', 'B': 'X', 'C': 'W', 'D': 'V', 'E': 'U', 'F': 'T', 'G': 'S',
        'H': 'R', 'I': 'Q', 'J': 'P', 'K': 'O', 'L': 'N', 'M': 'M', 'N': 'L',
        'O': 'K', 'P': 'J', 'Q': 'I', 'R': 'H', 'S': 'G', 'T': 'F', 'U': 'E',
        'V': 'D', 'W': 'C', 'X': 'B', 'Y': 'A', 'Z': 'Z',
        'А': 'Я', 'Б': 'Ю', 'В': 'Э', 'Г': 'Ь', 'Д': 'Ы', 'Е': 'Ъ', 'Ё': 'Щ',
        'Ж': 'Ш', 'З': 'Ч', 'И': 'Ц', 'Й': 'Х', 'К': 'Ф', 'Л': 'У', 'М': 'Т',
        'Н': 'С', 'О': 'Р', 'П': 'К', 'Р': 'Й', 'С': 'И', 'Т': 'Г', 'У': 'Е',
        'Ф': 'Д', 'Х': 'В', 'Ц': 'Б', 'Ч': 'А', 'Ш': 'Г', 'Щ': 'Ё', 'Ъ': 'Ж',
        'Ы': 'З', 'Ь': 'Й', 'Э': 'К', 'Ю': 'Л', 'Я': 'М'
    }

    while True:
        choice = int(input("Выберите опцию (1 - шифрование, 2 - расшифровка, 0 - выход): "))
        if choice == 0:
            print("Выход из программы.")
            break

        message = input("Введите сообщение: ").upper()

        if choice == 1:
            result = encrypt_decrypt(message, rotors, reflector)
            print("Зашифрованное сообщение:", result)
        elif choice == 2:
            inverted_rotors = {v: k for k, v in rotors.items()}
            inverted_reflector = {v: k for k, v in reflector.items()}
            result = encrypt_decrypt(message, inverted_rotors, inverted_reflector)
            print("Расшифрованное сообщение:", result)
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
