#is the number even or odd?

print("please input a number")
x = input()
x = int(x)


if y % 2 == 0 and y % 4 == 0:
    print('that is an even number and divisible by 4!')
elif y % 2 == 0:
       print('that is an even number')
elif y % 2 != 0:
        print('that is an odd number')
else:
        exit()
