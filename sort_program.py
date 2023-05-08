import os
import sys


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
    # Створюю словник для зберігання розширень файлів і відповідних каталогів
    extensions = {
        "images": {"JPEG", "PNG", "JPG", "SVG"},
        "videos": {"AVI", "MP4", "MOV", "MKV"},
        "documents": {"DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"},
        "music": {"MP3", "OGG", "WAV", "AMR"},
        "archives": {"ZIP", "GZ", "TAR"},
        "unknown": set(),
    }
    directories = {category: f"{directory}/{category}" for category in extensions}

    # Рекурсивно викликаємо функцію для всіх підкаталогів
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if os.path.isdir(full_path) and not filename.startswith("."):
            sort_files(full_path)
        else:
            # Інакше, якщо це файл, то сортую його відповідно до розширення
            extension = os.path.splitext(filename)[-1].lower()
            category = extensions.get(extension, "unknown")

            # Нормалізую назву файлу
            normalized_name = normalize(filename)

            # Створюю папку для цієї категорії, якщо вона ще не існує
            category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

            # Переміщую файл у відповідну категорію
            new_path = os.path.join(category_path, normalized_name)
            os.rename(full_path, new_path)


if __name__ == "__main__":
    # Розбираю аргументи командного рядка
    # if len(sys.argv) != 2:
    #     print(f"Usage: python {sys.argv[0]} <directory>")
    #     sys.exit(1)
    # directory = sys.argv[1]

    directory = "D:/trash"

    # Сортую файли у вказаному каталозі
    sort_files(directory)
