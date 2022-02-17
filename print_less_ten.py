a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less = []
greater =[]

i = input('request a number')
i = int(i)

for n in a:
    if n < i:
        less.append(n)
    else:
        greater.append(n)

print(less)


#how would you write this in one line??? you need an if statement?