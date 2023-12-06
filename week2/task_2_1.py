def calculate_word_lengths(words):
    word_list = words.split()
    word_lengths = []
    
    for word in word_list:
        word_lengths.append(len(word))
    
    return word_lengths

