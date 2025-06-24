# TCS PROBLEM 2 :
name = ["A","B","C","D","E","F","G","H","I","J"]
memo = [0,1,1,1,2,2,1,2,1,2]
salary = [1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]

data = list(zip(name,memo,salary))
print(data)
remove = [i for i in data if i[2]>4000]
print(remove)
remaining = [i for i in data if i[2]<4000]
print(remaining)
remaining.sort(key = lambda x:x[2],reverse=True)
final = []
for i in remaining:
    if(i[1]>1):
        final.append(i)
    if(len(final) == 3 ):
        break
print("The Details are as Follows : ")
res = remove + final
pos = 1
for  i in res:
    print("{}. MR.{} has {} memos with salary  {} has been removed from the company".format(pos,i[0],i[1],i[2]))
    pos = pos+1
