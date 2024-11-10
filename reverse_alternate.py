s= input("Enter a string: ")
# i take a string "How are you"

words= s.split()

reversed_words= []
for i, word in enumerate(words):  # this function provides the index(i) and the word itself (word) in each iteration
    
    if i%2==0:

        reversed_words.append(word[::-1]) # reverses the word then appends
    else:
        reversed_words.append(word) # appends the word without reversing

        reverse= ' '.join(reversed_words)
        print("After reversing string of alternative word:")
        print(reverse)