print('Welcome to Tip Calculator')
total = float(input('What was the total bill?'))
split = float(input('How many people to split the bill'))
per = float(input('What percentage u want to give?'))

pay = per*total/100
each = (total+pay)/split
ans = round(each, 2)
print('Each person should pay', ans)
