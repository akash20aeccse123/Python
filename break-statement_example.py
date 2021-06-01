#break statement example

a=b=c=0
for i in range(1,21):
    a=int(input("Enter number 1:"))
    b=int(input("Enter number 2:"))

    if b==0:
        print("Division by Zero Error!!""Aborting")
        break
    else:
        c=a//b
        print("Quotient is  =",c)
print("Program is Over !!")
