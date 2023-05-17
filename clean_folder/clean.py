import os
import sys
import shutil


def normalize(filename):
    # Визначаю словник для зіставлення кириличних символів із латинськими
    translit_map = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "H",
        "Ґ": "G",
        "Д": "D",
        "Е": "E",
        "Є": "Ye",
        "Ж": "Zh",
        "З": "Z",
        "И": "Y",
        "І": "I",
        "Ї": "Yi",
        "Й": "Y",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "Kh",
        "Ц": "Ts",
        "Ч": "Ch",
        "Ш": "Sh",
        "Щ": "Shch",
        "Ь": "",
        "Ю": "Yu",
        "Я": "Ya",
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "h",
        "ґ": "g",
        "д": "d",
        "е": "e",
        "є": "ie",
        "ж": "zh",
        "з": "z",
        "и": "y",
        "і": "i",
        "ї": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ь": "",
        "ю": "iu",
        "я": "ia",
    }

    # Перебираю кожен символ в назві файлу
    normalized_name = ""
    for char in filename:
        # Перетворення кирилиці на латиницю
        if char in translit_map:
            normalized_name += translit_map[char]
        # Заміняю не буквено-цифрові символи на підкреслення
        elif not char.isalnum():
            normalized_name += "_"
        else:
            normalized_name += char
    return normalized_name


def sort_files(directory):
    extensions = {
        "images": {"JPEG", "PNG", "JPG", "SVG"},
        "videos": {"AVI", "MP4", "MOV", "MKV"},
        "documents": {"DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"},
        "music": {"MP3", "OGG", "WAV", "AMR"},
        "archives": {"ZIP", "GZ", "TAR"},
        "unknown": set(),
    }
    directories = {
        category: os.path.join(directory, category) for category in extensions
    }

    for filename in os.listdir(directory):
        source_path = os.path.join(directory, filename)
        if os.path.isdir(source_path):
            sort_files(source_path)
        elif os.path.isfile(source_path):
            extension = filename.split(".")[-1].upper()
            found = False
            for category, extensions_set in extensions.items():
                if extension in extensions_set:
                    found = True
                    break

            if not found:
                category = "unknown"

            normalized_name = normalize(filename)
            target_directory = directories[category]
            target_path = os.path.join(target_directory, normalized_name)
            shutil.move(source_path, target_path)


# Отримую шлях до папки від користувача через консоль
directory = input("Введіть шлях до папки, яку потрібно відсортувати: ")

# Виклик функції для сортування файлів
sort_files(directory)


if __name__ == "__main__":
    sort_files()
    normalize()
