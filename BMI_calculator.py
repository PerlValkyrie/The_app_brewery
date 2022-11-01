# BMI Calculator

height = input("What is your height in meters?:\n")
weight = input("What is your weight in kg?\n")
height_float = float(height)
weight_int = float(weight)

bmi = weight_int / height_float ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)