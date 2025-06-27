class rec:
    def set_dimension(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
l=[]
ch = int(input("Enter the no of Rectangle : "))
for i in range(ch):
    r=rec()
    length=int(input("Enter the length of Rectangle : "))
    breadth=int(input("Enter the breadth of Rectangle : "))
    r.set_dimension(length,breadth)
    l.append(r)
print("---------------------------------------------------")
pos = 1
for i in l:

    print("The Area of The Rectangle {} is : {}".format(pos,i.area()))
    pos = pos + 1
    print("-------------------------------------------------")