def find_shortest_word(words):
    shortest_word = ""
    
    # Initialize shortest_word with the first word in the list
    if words:
        shortest_word = words[0]
    
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
    
    return shortest_word