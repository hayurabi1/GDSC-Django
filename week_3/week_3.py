#second task
onsonant = input("please enter patern to be printed: ")
x = consonant
if x == 'a' or x=='e' or x=='i' or x=='o' or x =='u':
    print("Vowels are not allowed in the input")
elif len(x)>1:
    print ("The lenght of charachter should be one")
elif x !="a" or x !='e' or x !="i" or x !='o' or x !='u':
    print (x)
    print(x,x,x)
    print(x,x,x,x,x)
    print(x,x,x,x,x,x,x)
    print(x,x,x,x,x,x,x,x,x)

else:
    print("NOt correct ")

#third task
word = input("Enter the word :")
if word [:: -1] == word:
    print("the word is palindrome")
else:
    print('They are not equal')

#fourth task
even_sum = 0
count_three = 0
count_five = 0

for num in range(1, 51):
    if num % 2 == 0:
        even_sum += num

        if num % 3 == 0:
            print("Three")
            count_three += 1
        elif num % 5 == 0:
            print("Five")
            count_five += 1
        else:
            print(num)
    else:
        continue

print("Sum of even numbers:", even_sum)
print("Count of 'Three':", count_three)
print("Count of 'Five':", count_five)
