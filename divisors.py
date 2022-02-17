#Create a program that asks the user for a number and then prints out a list of all the divisors of that number

def divisors(i):
    allnum= range(1,i+1)

    yes_divide=[]
    no_divide = []




    for num in allnum:
        if i % num == 0:
            yes_divide.append(num)
        else:
            no_divide.append(num)

    return yes_divide,no_divide

    
if __name__ == "__main__":
    i = input('give a number')
    i = int(i)
    yes_divide,no_divide = divisors(i)
    print(yes_divide)
    print(no_divide)