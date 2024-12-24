a= input("Enter a string: ") # take a string 
start_index= int(input("Enter the starting index: "))
end_index= int(input("Enter the ending index: "))
 
#Extracting the indices and reversing the substring
substring= a[start_index:end_index] [::-1]
# when indices will be extracted the elements in between them will be printed in reverse order

#result printing
print("The reversed substring is:",substring)
