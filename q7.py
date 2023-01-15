"""Write a python program to find the numbers which are multiple of 7 and divisible by 11 in the range
1-500."""
list1=[]
for i in range(1,501):
    if i%7==0 and i%5==0:
        list1.append(i)
print(list1)
    
