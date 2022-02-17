# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.


list = [1,2,3,4,5,6,1,2,3,4,5,6]
list2 = [2,4,6,8,10,]
def listnd(x):
    L =[]
    L=set(x)
    print(L)

listnd(list)

def twoLoverlap(a,b):
    yeslist = []
    nolist = []
    for num in a:
        if num in b:
            yeslist.append(num)
        else:
            nolist.append(num)

    noduplicate = []

    [noduplicate.append(x) for x in yeslist if x not in noduplicate]
    # found this online, why do i need index brackets outside of the entire statement?
    print(yeslist)
    print(noduplicate)

twoLoverlap(list,list2)