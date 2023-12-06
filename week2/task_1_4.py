from collections import Counter

def freq_word_des(text):
    words = text.split()
    word_counts = Counter(words)
    frequencies = word_counts.most_common()
    
    for word, count in frequencies:
        print(f"Word: {word}, Count: {count}")

text = input("Enter the text: ")
freq_word_des(text)

