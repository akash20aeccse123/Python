'''5. Program to find the multiply of a number(the 
divisor) out of given five numbers.'''

n1=float(input("Enter number 1:"))
n2=float(input("Enter number 2:"))
n3=float(input("Enter number 3:"))
n4=float(input("Enter number 4:"))
n5=float(input("Enter number 5:"))
div=float(input("Enter divisor number:"))
count=0

rem=n1%div
if rem==0:
    print(n1,sep='')
    count+=1
rem=n2%div
if rem==0:
    print(n2,sep='')
    count+=1
rem=n3%div
if rem==0:
    print(n3,sep='')
    count+=1
rem=n4%div
if rem==0:
    print(n4,sep='')
    count+=1
rem=n5%div
if rem==0:
    print(n5,sep='')
    count+=1
print()
print(count,'multiply of',div,'found')
