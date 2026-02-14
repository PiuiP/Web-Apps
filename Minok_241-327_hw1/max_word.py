import string
with open('example.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    words = text.split()
    
    clean_words = []
    for word in words:
        clean_word = word.strip(string.punctuation + '«»„“”‘’—–…')
        if clean_word:
            clean_words.append(clean_word)
    
    answer = []
    MaxWord = 0
    for word in clean_words:
        if len(word) > MaxWord:
            answer.clear()
            answer.append(word)
            MaxWord = len(word)
        elif len(word) == MaxWord:
            answer.append(word)
    print(" ".join(answer))
