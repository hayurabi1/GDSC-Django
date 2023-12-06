def tokination_word (sentence):
   words = sentence.split()
   return words
        
sentence = input("Enter the sentence ")
tokens = tokination_word(sentence)
print(tokens)

