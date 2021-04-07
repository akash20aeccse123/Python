b=int(input('enter bengali:'))
e=int(input('enter english:'))
m=int(input('enter mathematics:'))
p=int(input('enter physics:'))
c=int(input('enter chemistry:'))

tot=b+e+m+p+c
avg=tot/5
print('Total Marks=',tot)
print('Average=',avg)

if tot>=125:
    print('Pass')
else:
    print('Fail')
