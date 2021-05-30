'''3. Program that inputs three numbers and calculates 
two sums as per this:
Sum1 as the sum of all input numbers
Sum2 as the sum of non-duplicate numbers; if 
there are duplicate numbers in the input ignores 
them.'''
sum1=sum2=0
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))
sum1=(n1+n2+n3)
if n1!=n2 and n1 !=n3:
    sum2+=n1
if n2!=n1 and n2!=n3:
    sum2+=n2
if n3!=n1 and n3!=n2:
    sum2+=n3
print("Numbers are",n1,n2,n3)
print("Sum of Given three numbers=",sum1)
print("Sum of Non-duplicate numbers=",sum2)
