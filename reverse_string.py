# taking the string as an input from the user
a= input("Enter a string: ")

for word in a.split(): # this line will iterate over the entered string and break the string into words.

   print(word[::-1],end=" ") # here [::-1] is a slicing notation that will reverse each word of string.
   # end= " " will print the words  with spaces instead of a new line  character.
