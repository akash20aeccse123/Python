'''7. Program that’s reads two numbers and an 
arithmetic operator and display the computed 
results'''

n1=int(input("Enter Number 1:"))
n2=int(input("Enter Number 2:"))
ch=input("Enter Operator[+ - * / %]: ")
result=0
if ch=="+":
    result=n1+n2
if ch=="-":
    result=n1-n2
if ch=="*":
    result=n1*n2
if ch=="/":
    result=n1/n2
if ch=="%":
    result=n1%n2
else:
    print("Invalid Operator! try again!!")
print(n1,ch,n2,"=",result)
