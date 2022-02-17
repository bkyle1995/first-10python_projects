#Write one line of Python that takes this list a
# and makes a new list that has only the even elements of this list in it.


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list2=[], list1=[],
for n in a: if n%2 == 0: list2.append(n) else: list1.append(n)
print(list2)
