#7. Program to illustrate the difference between break 
#and continue statements.

print("The loop with 'break' produces output as:")
for i in range(1,11):
    if i%3==0:
        break
    else:
        print(i)
print("--------------------------------")        
print("The loop with 'continue' produces output as:")
for i in range(1,11):
    if i%3==0:
        continue
    else:
        print(i)

    