package main

import (
	"fmt"
	"strings"
)

func encryptDecrypt(message string, rotors, reflector map[rune]rune) string {
	var result strings.Builder
	for _, char := range message {
		if newChar, exists := rotors[char]; exists {
			result.WriteRune(newChar)
		} else if newChar, exists := reflector[char]; exists {
			result.WriteRune(newChar)
		} else {
			result.WriteRune(char) // Оставляем символ, если не найден
		}
	}
	return result.String()
}

func main() {
	rotors := map[rune]rune{
		'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J',
		'H': 'K', 'I': 'L', 'J': 'M', 'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q',
		'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W', 'U': 'X',
		'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C',
		'А': 'Е', 'Б': 'Ё', 'В': 'Ж', 'Г': 'З', 'Д': 'И', 'Е': 'Й', 'Ё': 'К',
		'Ж': 'Л', 'З': 'М', 'И': 'Н', 'Й': 'О', 'К': 'П', 'Л': 'Р', 'М': 'С',
		'Н': 'Т', 'О': 'У', 'П': 'Ф', 'Р': 'Х', 'С': 'Ц', 'Т': 'Ч', 'У': 'Ш',
		'Ф': 'Щ', 'Х': 'Ъ', 'Ц': 'Ы', 'Ч': 'Ь', 'Ш': 'Э', 'Щ': 'Ю', 'Ъ': 'Я',
		'Ы': 'А', 'Ь': 'Б', 'Э': 'В', 'Ю': 'Г', 'Я': 'Д',
	}

	reflector := map[rune]rune{
		'A': 'Y', 'B': 'X', 'C': 'W', 'D': 'V', 'E': 'U', 'F': 'T', 'G': 'S',
		'H': 'R', 'I': 'Q', 'J': 'P', 'K': 'O', 'L': 'N', 'M': 'M', 'N': 'L',
		'O': 'K', 'P': 'J', 'Q': 'I', 'R': 'H', 'S': 'G', 'T': 'F', 'U': 'E',
		'V': 'D', 'W': 'C', 'X': 'B', 'Y': 'A', 'Z': 'Z',
		'А': 'Я', 'Б': 'Ю', 'В': 'Э', 'Г': 'Ь', 'Д': 'Ы', 'Е': 'Ъ', 'Ё': 'Щ',
		'Ж': 'Ш', 'З': 'Ч', 'И': 'Ц', 'Й': 'Х', 'К': 'Ф', 'Л': 'У', 'М': 'Т',
		'Н': 'С', 'О': 'Р', 'П': 'К', 'Р': 'Й', 'С': 'И', 'Т': 'Г', 'У': 'Е',
		'Ф': 'Д', 'Х': 'В', 'Ц': 'Б', 'Ч': 'А', 'Ш': 'Г', 'Щ': 'Ё', 'Ъ': 'Ж',
		'Ы': 'З', 'Ь': 'Й', 'Э': 'К', 'Ю': 'Л', 'Я': 'М',
	}

	for {
		var choice int
		fmt.Print("Выберите опцию (1 - шифрование, 2 - расшифровка, 0 - выход): ")
		fmt.Scan(&choice)

		if choice == 0 {
			fmt.Println("Выход из программы.")
			break
		}

		var message string
		fmt.Print("Введите сообщение: ")
		fmt.Scanln(&message) // Изменено на Scanln для считывания строки

		// Ввод может содержать пробелы, добавим считывание всей строки
		reader := bufio.NewReader(os.Stdin)
		message, _ = reader.ReadString('\n')
		message = strings.TrimSpace(message)

		message = strings.ToUpper(message)

		if choice == 1 {
			result := encryptDecrypt(message, rotors, reflector)
			fmt.Println("Зашифрованное сообщение:", result)
		} else if choice == 2 {
			invertedRotors := invertMap(rotors)
			invertedReflector := invertMap(reflector)
			result := encryptDecrypt(message, invertedRotors, invertedReflector)
			fmt.Println("Расшифрованное сообщение:", result)
		} else {
			fmt.Println("Неверный выбор.")
		}
	}
}

func invertMap(m map[rune]rune) map[rune]rune {
	inverted := make(map[rune]rune)
	for k, v := range m {
		inverted[v] = k
	}
	return inverted
}
