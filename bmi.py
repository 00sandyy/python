a = str(input('In what measurement do u know ur height?(ft,inch) or metre'))
if a.lower() == "ft" or a.lower() == 'inch' or a.lower() == 'feet':

    print('Enter height in foot and inch')
    feet = input('enter feet')
    inch = input('enter inch')
    height = float(feet)*0.3048+float(inch)*0.0254
else:
    height = float(input('enter height in metre'))

weight = float(input('enter your weight in kilogram'))
bmi = weight/(height*height)
if bmi < 18.5:
    print('Underweight', bmi)
elif 18.5 <= bmi <= 24.9:
    print('Normal weight  {bmi}')
elif 25 <= bmi <= 29.9:
    print('Overweight', bmi)
else:
    print("obese", bmi)
