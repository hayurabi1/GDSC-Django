def find_longest_word(text):
    words = text.split()
    longest_word = ""
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

text = input("Enter the text: ")
longest_word = find_longest_word(text)

if longest_word:
    print(f"Longest Word: {longest_word}, Length: {len(longest_word)}")
else:
    print("No words found in the text.")