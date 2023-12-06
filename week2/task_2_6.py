def display_word_length_distribution(word_length_frequencies):
    sorted_lengths = sorted(word_length_frequencies.keys())
    
    for length in sorted_lengths:
        frequency = word_length_frequencies[length]
        print("Word Length:", length, "Frequency:", frequency)