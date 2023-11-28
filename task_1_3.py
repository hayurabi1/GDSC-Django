def freq_word(text, word):
    count = 0 
    words = text.split()
  
    for w in words:
        if w == word:
            count += 1
    
    return count

text = input("Enter the text: ")
word = input("Enter the word: ") 
x = freq_word(text, word)

print("THE WORD FREQUENCY:", x)

