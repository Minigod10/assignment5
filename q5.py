"""Write a python program to print a triangular pattern of the alphabet (user input the number of rows).
Example: Input the number of rows = 5, then the pattern should come out as given below.
If the count of the alphabet gets exhausted, repeat the alphabet from A.
A
BC
DEF
GHIJ
KLMNO"""

rows=int(input("enter number of rows"))
count=0
for i in range(rows+1):
    for j in range(i):
        if count>=26:
            count=0
        print(chr(65+count),end="")
        count+=1
    print()
