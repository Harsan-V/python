def fact(num):
    if (num == 1):
        return 1
    i = 2
    while (num%i != 0):
        i = i + 1
    print(i, end=" ")
    fact(num//i)
num = int(input("Enter a number: "))
fact(num)