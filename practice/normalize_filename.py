def normalize_filename(name_file: str) -> str:
    """Заменяет все пробелы в имени файла на подчёркивания."""
    result = ''  # сюда собираем новую строку

    for char in name_file:
        if char == ' ':
            result += '_'   # пробел заменяем на подчёркивание
        else:
            result += char  # остальные символы оставляем как есть

    return result


print(normalize_filename('my photo.png'))