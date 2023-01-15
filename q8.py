"""Input 10 integer values from the user. Write a python program to find and print the following:
a. positive numbers
b. negative numbers
c. odd numbers
d. even numbers
e. Number of times each number occurs in the List"""

lst=[]
for i in range(1,11):
    lst.append(int(input("Enter a number")))
lst2=list(set(lst))
positive_number=[]
negative_number=[]
odd_number=[]
even_number=[]
for j in lst2:
    if j>0:
        positive_number.append(j)
    else:
        negative_number.append(j)
    if j%2==0:
        even_number.append(j)
    else:
        odd_number.append(j)
    print(j,"appears",lst.count(j),"times")


    

print("Number of positive number:",positive_number)
print("Number of nagative number:",negative_number)
print("Number of even number:",even_number)
print("Number of odd number:",odd_number)