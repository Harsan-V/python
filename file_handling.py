'''
#example 1:

file = open("bigsmoke.txt","w")
file.write("hi my name is bigsmoke enemy of Carl Johnson and now iam ghost searching him ! ")
file.close()
print("File added Successfully")

'''

#example 2 :

file = open("bigsmoke.txt","r")
data = file.readlines()
for i in data:
    word = i.split()
    print(word)

