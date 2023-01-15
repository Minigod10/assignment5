"""Write a python program to print the prime numbers for a user input range."""

lower_limit=int(input("Enter the lower limit:"))
upper_limit=int(input("Enter the upper limit:"))
for num in range(lower_limit,upper_limit+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

        