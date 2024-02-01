h = int(input('Whats is ur height?'))
if h > 120:
    print('Welcome to the rollercoaster')
    age = int(input('What is ur age?'))
    if age < 12:
        bill = 5
        print('child ticket are 5$')
    elif 12 < age <= 18:
        bill = 7
        print('please pay $7')
    else:
        bill = 12
        print('please pay $12')
    a = str(input('do u want photos? Y or N '))
    if a.upper() == "Y":
        bill += 3
        print(f'Ur total bill is {bill}')
    else:
        print('your total bill is ', bill)


else:
    print('U cannot ride a ride')
