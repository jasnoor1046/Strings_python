# funtion here is initialized to reverse the alternative words
def reverse_alternate_words(sentence):

    # in the particular string it will split the words
    words = sentence.split()

    # a separate list has also been intialized for it
    result = []

    # this will itterate over the words of sentence for odd indices
    for i in range(len(words)):
        if i % 2 == 1:

            # if it get odd index then it will reverse that word then add to new list
            result.append(words[i][::-1])
        else:

            # if its even then it will remain unchanged
            result.append(words[i])

            # join the words in the new list
    return ' '.join(result)

sentence = input("Enter a sentence: ")
result = reverse_alternate_words(sentence)
print(result)

