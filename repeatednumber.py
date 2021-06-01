'''8. Program to input some numbers repeatedly and 
print their sum.The program ends when the users 
say no more enter(normal terminator) or program 
aborts when the number entered is less than zero.'''
count=sum=0
ans='y'
while ans=='y':
    num=int(input("Enter Number:"))
    if num<0:
        print("Number entered is below zero.Aborting!")
        break
    sum=sum+num
    count=count+1
    ans=input( "Want to enter more numbers? (y/n):")
else:
    print("You entered",count,"numbers so far")
print("sum of numbers entered is",sum)

