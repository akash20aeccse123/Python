#4. Pgrogram to calculate the factorial of a number.

#n=int(input("Enter number to calculate:"))    #taking input from user
n=3
fact=1
while n>=1:
    fact=n*fact
    n=n-1
print("Factorial of the given number is=",fact)

