#1. Program to print table of a number, says 5.

n=int(input("Enter Number:")) #taking the input from user
#n=5
for i in range(1,11):
    tb=(n*i)
    print(n,"X",i,"=",tb)
