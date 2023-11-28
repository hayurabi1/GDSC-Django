def count_word_length_frequencies(words):
    word_length_frequencies = {}
    
    for word in words:
        length = len(word)
        if length in word_length_frequencies:
            word_length_frequencies[length] += 1
        else:
            word_length_frequencies[length] = 1
    
    return word_length_frequencies
