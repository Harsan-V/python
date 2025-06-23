import random
import time
name1 = input("Enter the player1 : ")
name2 = input("Enter the player2 : ")
num = []
while(len(num) <5):
    d = random.randint(1,10)
    if(d in num):
        continue
    else:
        num.append(d)
player1 = []
player2 = []
s1 =0
s2 = 0
for i in range(3):
    print("Turn{}".format(i+1))
    a = int(input("hi {} turn{} predict:".format(name1,(i+1))))
    player1.append(a)
    if(a in num):
        print("CORRECT")
        s1 = s1+1
    else:
        print("WRONG")
    b= int(input("hi {} turn{} predict : ".format(name2,(i+1))))
    player2.append(b)
    if(b in num):
        print("CORRECT")
        s2 = s2+1
    else:
        print("Wrong")
print("-------------------------------")
print("Summary")
print("comp has fixed ",num)
print("Player 1 has choosen : ",player1)
print("Player 1 score is : ",s1)
print("Player 2 has chosoen : ",player2)
print("Player 2 score is : ",s2)
print("-------------------------------")
print()
time.sleep(2)
if(s1>s2):
    print("{} is the Winner ! ".format(name1))
    print()
elif(s2>s1):
    print("{} is the Winner !".format(name2))
    print()
else:
    print("DRAW")
    print()