name= "Astronomy Space" # taking a string

# now applying slicing
print(name[0:3])
# here 0 is the first index, in slicing always first index is included not the last one

print(name[-4:-1])
# negative slicing can be converted into positive, by taking corresponding positive index :
print(name[11:14])

print(name[6:14])

print(name[:4])
print(name[1:]) # it will simply print from index 1

#SLICING WITH SKIP VALUE
print(name[1:7:3]) # here it will take the jump of 3 elements

#ADVACED SLICING
print(name[:7]) # it will go till 7th index

print(name[0:]) # here sting will be printed as it is