def find_word(text, word):
    count = 0
    word_list = text.split()

    for w in word_list:
        if w == word:
            count += 1

    return count

text = input("Enter the text: ")
search_word = input("Enter the word to search: ")

count = find_word(text, search_word)

if count > 0:
    print(f"Word: {search_word}, Count: {count}")
else:
    print("Your word is not present in the text.")