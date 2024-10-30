# let us take a string and initialize it.
string= "Hello World"

odd_chars= "" # initializing an empty string to store extracted odd characters.

for i in range(len(string)): # inside this loop it will check if the current index is odd,
# if the index is odd it will append the character at that index to odd_chars    
    if i % 2 != 0:
        odd_chars += string[i] 
        # string[i] is the current character we are looking at 
        # odd_chars += take the current character and add it to the end of the odd_chars.

        print(odd_chars)
