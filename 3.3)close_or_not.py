print('Enter two numbers')
num1=float(input('Enter num1: '))
num2=float(input('Enter num2: '))
if(num1+0.001==num2)or(num2+0.001==num1):
    print('Numbers are close')
else:
    print('Numbers are not close')
