def calculate_average_word_length(words):
    total_length = sum(words)
    word_count = len(words)
    
    if word_count == 0:
        return 0  # To avoid division by zero
    
    average_length = total_length / word_count
    return average_length

words = input("enter the words please\n")
x = calculate_average_word_length(words)
print(x)