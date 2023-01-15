"""Python Program to Print all Numbers in a Range Divisible by a Given Number. (user inputs the range
and the number)"""
number=int(input("enter a number:"))
n=int(input("enter the range:"))
lists=[]
for i in range(1,n+1):
    if i%number==0:
        lists.append(i)
print(lists)
        
        