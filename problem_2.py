bs=int(input("Enter Basic Salary:"))
if bs>1000:
    hra=bs*15/100
    da=bs*95/100
    ca=bs*10/100
else:
    hra=bs*10/100
    da=bs*90/100
    ca=bs*5/100
gs=bs+da+hra+ca
print("Gross Salary=Rs."+str(gs))
