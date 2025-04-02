#function defination 
def is_pallindrome(s):

    #removes the spaces from the  the string
    s= s.replace(" ","").lower()
    # check if the string is equal to its reverse
    return s== s[::-1] 

# testing the function by taking the input
s = input("Enter a string to check if it's pallindrome: ")

# applying conditions to check
if is_pallindrome(s):
    print(f"{s} is pallindrome.")

else:
    print(f"{s} is not pallindrome.")    
