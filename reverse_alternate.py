s= input("Enter a string: ") #input of the string

words= s.split() # it splits the input string
split_length = len(words) # calculates the length of the words list

result_words= [] # initialized an empty list to store the processed words

for i in range(split_length):
    if i % 2 == 1: # it checks if the index is odd
        result_words.append(words[i] [::-1]) # reverses the word at that index, appends the reversed words to result_words
    else:
        result_words.append(words[i]) # appends the words as it is

        #joining the words into a single string
        result= ' '.join(result_words)

        #printing the result
        print(result)        
