# taking the string as an input from the user
a= input("Enter a string: ")

for word in a.split(): #here each and every word will be splited

   print(word[::-1],end=" ") # here [::-1] will reverse each and every word of the string
