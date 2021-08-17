weight = input("Enter your weight in pounds:")
height = input("Enter your height in inche:")

weight_int = int(weight)
height_int = int(height)

weight_double = weight_per_pounds = 0.453592
height_double = height_per_meter = 0.0254

bmi = weight_double / height_double * height_double
print("BMI is:", bmi)
