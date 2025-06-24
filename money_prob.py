# print the number of cash combinations needed:

amt = int(input("Enter the Amount in rupees : "))

change = [500,200,100,50,20,10,5,2,1]

dict = {}

for i in change:
    if amt>=i:
        count = amt//i
        dict[i]=count
        amt-= count*i
print(dict)