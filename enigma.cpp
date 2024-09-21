#include <iostream>
#include <string>
#include <unordered_map>
#include <locale>
#include <codecvt>

std::wstring encryptDecrypt(const std::wstring& message, const std::unordered_map<wchar_t, wchar_t>& rotors, const std::unordered_map<wchar_t, wchar_t>& reflector) {
    std::wstring result;
    for (wchar_t charIn : message) {
        if (rotors.count(charIn)) {
            result += rotors.at(charIn);
        } else if (reflector.count(charIn)) {
            result += reflector.at(charIn);
        } else {
            result += charIn; // Оставляем символ, если не найден
        }
    }
    return result;
}

std::unordered_map<wchar_t, wchar_t> invertMap(const std::unordered_map<wchar_t, wchar_t>& m) {
    std::unordered_map<wchar_t, wchar_t> inverted;
    for (const auto& pair : m) {
        inverted[pair.second] = pair.first;
    }
    return inverted;
}

int main() {
    std::unordered_map<wchar_t, wchar_t> rotors = {
        {L'A', L'D'}, {L'B', L'E'}, {L'C', L'F'}, {L'D', L'G'}, {L'E', L'H'}, {L'F', L'I'},
        {L'G', L'J'}, {L'H', L'K'}, {L'I', L'L'}, {L'J', L'M'}, {L'K', L'N'}, {L'L', L'O'},
        {L'M', L'P'}, {L'N', L'Q'}, {L'O', L'R'}, {L'P', L'S'}, {L'Q', L'T'}, {L'R', L'U'},
        {L'S', L'V'}, {L'T', L'W'}, {L'U', L'X'}, {L'V', L'Y'}, {L'W', L'Z'}, {L'X', L'A'},
        {L'Y', L'B'}, {L'Z', L'C'}, {L'А', L'Е'}, {L'Б', L'Ё'}, {L'В', L'Ж'}, {L'Г', L'З'},
        {L'Д', L'И'}, {L'Е', L'Й'}, {L'Ё', L'К'}, {L'Ж', L'Л'}, {L'З', L'М'}, {L'И', L'Н'},
        {L'Й', L'О'}, {L'К', L'П'}, {L'Л', L'Р'}, {L'М', L'С'}, {L'Н', L'Т'}, {L'О', L'У'},
        {L'П', L'Ф'}, {L'Р', L'Х'}, {L'С', L'Ц'}, {L'Т', L'Ч'}, {L'У', L'Ш'}, {L'Ф', L'Щ'},
        {L'Х', L'Ъ'}, {L'Ц', L'Ы'}, {L'Ч', L'Ь'}, {L'Ш', L'Э'}, {L'Щ', L'Ю'}, {L'Ъ', L'Я'},
        {L'Ы', L'А'}, {L'Ь', L'Б'}, {L'Э', L'В'}, {L'Ю', L'Г'}, {L'Я', L'Д'}
    };

    std::unordered_map<wchar_t, wchar_t> reflector = {
        {L'A', L'Y'}, {L'B', L'X'}, {L'C', L'W'}, {L'D', L'V'}, {L'E', L'U'}, {L'F', L'T'},
        {L'G', L'S'}, {L'H', L'R'}, {L'I', L'Q'}, {L'J', L'P'}, {L'K', L'O'}, {L'L', L'N'},
        {L'M', L'M'}, {L'N', L'L'}, {L'O', L'K'}, {L'P', L'J'}, {L'Q', L'I'}, {L'R', L'H'},
        {L'S', L'G'}, {L'T', L'F'}, {L'U', L'E'}, {L'V', L'D'}, {L'W', L'C'}, {L'X', L'B'},
        {L'Y', L'A'}, {L'Z', L'Z'}, {L'А', L'Я'}, {L'Б', L'Ю'}, {L'В', L'Э'}, {L'Г', L'Ь'},
        {L'Д', L'Ы'}, {L'Е', L'Ъ'}, {L'Ё', L'Щ'}, {L'Ж', L'Ш'}, {L'З', L'Ч'}, {L'И', L'Ц'},
        {L'Й', L'Х'}, {L'К', L'Ф'}, {L'Л', L'У'}, {L'М', L'Т'}, {L'Н', L'С'}, {L'О', L'Р'},
        {L'П', L'К'}, {L'Р', L'Й'}, {L'С', L'И'}, {L'Т', L'Г'}, {L'У', L'Е'}, {L'Ф', L'Д'},
        {L'Х', L'В'}, {L'Ц', L'Б'}, {L'Ч', L'А'}, {L'Ш', L'Г'}, {L'Щ', L'Ё'}, {L'Ъ', L'Ж'},
        {L'Ы', L'З'}, {L'Ь', L'Й'}, {L'Э', L'К'}, {L'Ю', L'Л'}, {L'Я', L'М'}
    };

    std::wcin.imbue(std::locale(""));

    while (true) {
        int choice;
        std::wcout << L"Выберите опцию (1 - шифрование, 2 - расшифровка, 0 - выход): ";
        std::wcin >> choice;

        if (choice == 0) {
            std::wcout << L"Выход из программы." << std::endl;
            break;
        }

        std::wstring message;
        std::wcout << L"Введите сообщение: ";
        std::wcin.ignore(); // Очистка буфера перед вводом строки
        std::getline(std::wcin, message);

        for (wchar_t& c : message) {
            c = std::towupper(c); // Приведение к верхнему регистру
        }

        if (choice == 1) {
            std::wstring result = encryptDecrypt(message, rotors, reflector);
            std::wcout << L"Зашифрованное сообщение: " << result << std::endl;
        } else if (choice == 2) {
            auto invertedRotors = invertMap(rotors);
            auto invertedReflector = invertMap(reflector);
            std::wstring result = encryptDecrypt(message, invertedRotors, invertedReflector);
            std::wcout << L"Расшифрованное сообщение: " << result << std::endl;
        } else {
            std::wcout << L"Неверный выбор." << std::endl;
        }
    }

    return 0;
}
