#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)



#list[<start>:<stop>:<step>]
#need to practice this
w = input('please type out a word ')

w = str(w)

rw = w[::-1]

if w == rw:
    print("this is a palindrome")
else:print("this is not a palidrome")