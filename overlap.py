#and write a program that returns a list that contains only the elements that are common between the two lists
# (without duplicates).
# Make sure your program works on two lists of different sizes


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

yeslist=[]
nolist = []


for num in a:
    if num in b:
        yeslist.append(num)
    else:nolist.append(num)

noduplicate = []

[noduplicate.append(x) for x in yeslist if x not in noduplicate]
# found this online, why do i need index brackets outside of the entire statement?
print(yeslist)
print(noduplicate)