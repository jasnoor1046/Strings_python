sentence = input("Enter a string: ")
words = sentence.split()

# Initialize variables to track the longest word and its length
longest_word = ""
max_length = 0

# Loop through each word in the list
for word in words: 
    # here word is defined and takes each word from the 'words' list one by one
    # if the current word found is longer than the longest word so far:
    
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

print(f"The longest word is: {longest_word}")
