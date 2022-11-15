# Bmi calculator with a if else

height = float(input("What is your height in meters?:\n"))
weight = float(input("What is your weight in kg?\n"))


def BMI(height, weight):
    bmi = weight / height ** 2
    if bmi < 16:
        return 'severely underweight', bmi
    elif bmi >= 16 and bmi < 18.5:
        return 'underweight', bmi
    elif bmi >= 18.5 and bmi < 25:
        return 'health', bmi
    elif bmi >= 25 and bmi < 30:
        return 'overweight', bmi
    elif bmi >= 30:
        return 'obese', bmi

quote, bmi = BMI(height,weight)
print('your bmi is: {} and you are: {}'.format(bmi,quote))