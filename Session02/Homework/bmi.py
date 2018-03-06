height = int(input('Enter your height: '))
print('Your height(cm): ' , height)
#covert cm to m
height_m = height / 100
print('So your height(m): ' , height_m)

weight = int(input('Enter your weight: '))
print('Your weigth(kg): ' , weight)

#Body Mass Index
BMI = weight / (height_m * height_m)
print('Your Body Mass Index: ', BMI)

#IF
if BMI <= 16:
    print('Severely underweight')
elif BMI > 16 and BMI <= 18.5:
    print('Underweight')
elif BMI > 18.5 and BMI <= 25:
    print('Normal')
elif BMI > 25 and BMI < 30:
    print('Overweight')
else:
    print('Obese')
