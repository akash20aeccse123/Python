qnt=int(input("Enter value of quantity:"))
price=float(input("Enter value of price:"))

if(qnt>1000):
    dis=10
else:
    dis=0
totexp=qnt*price-qnt*price*dis/100
print("Total expenses=Rs."+str(totexp))
