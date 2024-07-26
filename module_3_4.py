
def single_root_words (root_word, *other_words):
    same_words = []  # Список из тех слов списка other_words, которые содержат root_word
    root_word_lower = root_word.lower()  # Приводим root_word к нижнему регистру

    for words in other_words:
        words_lower = words.lower()  # Приводим word к нижнему регистру

        if root_word_lower in words_lower:  # and word_lower.count(root_word_lower) == 1:
            same_words.append(words)
        elif words_lower in root_word_lower:
            same_words.append(words)


    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
