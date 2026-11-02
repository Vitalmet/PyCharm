"""
Задача: найти слова, которые встречаются в тексте больше 2 раз,
и подходят под условия:
  - длина не меньше 5 символов,
  - не меньше 4 УНИКАЛЬНЫХ символов (например, 'green' -> g,r,e,n = 4),
  - встречаются больше 2 раз (то есть 3 и более).

Порядок действий важен: сначала чистим слово от пунктуации и приводим
к нижнему регистру, и только ПОТОМ считаем частоты. Иначе 'spathe' и
'spathe,' считались бы разными словами.

Результат выводится по одному слову в строке, в алфавитном порядке.
"""

PUNCT = "!,.?;:#$%^&*()"  # знаки, которые нужно убрать из слов


def clean_word(raw):
    """Убирает пунктуацию и приводит слово к нижнему регистру."""
    result = ''
    for char in raw:
        # '\'' в PUNCT нет, поэтому кавычки и апострофы останутся в слове — так и требует условие
        if char not in PUNCT:
            result += char
    return result.lower()


def count_unique_chars(word):
    """Сколько РАЗНЫХ символов в слове: 'green' -> 4 (g, r, e, n)."""
    unique = ''
    for char in word:
        if char not in unique:
            unique += char
    return len(unique)


def main():
    text = input()          # читаем всю строку целиком
    words = text.split()    # split() без аргумента режет по любым пробелам и убирает пустые куски

    # Шаг 1: чистим каждое слово
    cleaned = []
    for raw in words:
        word = clean_word(raw)
        if word != '':          # слово могло состоять только из пунктуации, например '('
            cleaned.append(word)

    # Шаг 2: считаем частоты двумя параллельными списками:
    # unique_words[i] встретилось counts[i] раз
    unique_words = []
    counts = []
    for word in cleaned:
        if word in unique_words:
            counts[unique_words.index(word)] += 1
        else:
            unique_words.append(word)
            counts.append(1)

    # Шаг 3: отбираем слова, подходящие под все три условия сразу
    result = []
    for i in range(len(unique_words)):
        word = unique_words[i]
        if len(word) >= 5 and count_unique_chars(word) >= 4 and counts[i] > 2:
            result.append(word)

    # Шаг 4: алфавитный порядок и вывод по одному слову в строке
    for word in sorted(result):
        print(word)


if __name__ == '__main__':
    main()
