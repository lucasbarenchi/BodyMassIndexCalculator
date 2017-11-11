# Calculadora de indice de masa corporal

print('Body Mass Index calculator')

weight = raw_input('Type your weight (in kilograms): ')
height = raw_input('Now, your height (in centimeters): ')

BMI = float(float(weight)/((float(height)/100)**2))
todoOk = True

if BMI < 0:
    todoOk = False
elif BMI <= 18.5:
    message = 'infrapeso'
elif BMI < 25:
    message = 'normal'
elif BMI < 30:
    message = 'sobrepeso'
elif BMI < 100:
    message = 'obeso'
else:
    todoOk = False

if todoOk:
    print('Your BMI is: {0:.2f} and you are in category {other}'.format(BMI, other=message))
else:
    print('Your data is wrong. Please try again.')
