#Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions,

print("please input a number")
x = input()
x = int(x)
list = []

y: y =1
while y < x:
    list.append(y)
    y = y+1

list.pop(0)
# print(list)

for y in list:
    if x % y != 0:
        continue
    elif x%y == 0:
        print("this is not a prime number")
        exit()

print("this is a prime number")

