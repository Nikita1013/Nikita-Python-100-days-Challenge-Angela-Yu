#  BMI =  weight / Height ** 2
height = input("Enter your height in m : ")
weight = input("Enter your weight in kg : ")
# ----------------------------------------

BMI = int(weight) / float(height) ** 2
bmi_as_int = int(BMI)
print(bmi_as_int)

