a = input("what does player one choose? ")
b = input("what does player two choose? ")

a=str(a)
b=str(b)
#why do these first if statments not work? they always activate even when
#the correct term is put in

# if a != "rock" or "paper" or "scissors":
#     print("that is not an option")
#     exit()
# if b != "rock" or "paper" or "scissors":
#     print("that is not an option")
#     exit()


if a == "rock" and b == "paper":
    print("Player two wins")
elif a == "rock" and b == "scissors":
    print("player one wins")
elif a =="rock" and b == "rock":
    print("its a draw")
elif a == "paper" and b == "scissors":
    print("player two wins")
elif a =="paper" and b == "rock":
    print("player one wins")
elif a =="paper" and b == "paper":
    print("its a draw")

elif a == "scissors" and b == "rock":
    print("player two wins")
elif a =="scissors" and b == "paper":
    print("player one wins")
elif a =="scissors" and b == "scissors":
    print("its a draw")
else:
    print("wtf")

