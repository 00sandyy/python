print('Welcome to the pizza SHop')
print('Here are the pizza list:/n1.Small Pizza(S) ::5$/n2.Medium Pizza(M) ::10$/n3.Large Pizza(L) ::15$')
a = str(input("Which pizza do u need?"))
b = str(input('Do u need Peproni??(Y or N)'))
c = str(input('do u need extra cheese??(Y or N)'))
if a.lower() == 's':
    bill = 15
    if b.upper() == 'Y':
        bill += 3
    if c.upper() == 'Y':
        bill += 1

elif a.lower() == 'm':
    bill = 20
    if b.upper() == 'Y':
        bill += 5
    if c.upper() == 'Y':
        bill += 1

else:
    bill = 25
    if b.upper() == 'Y':
        bill += 5
    if c.upper() == 'Y':
        bill += 1
