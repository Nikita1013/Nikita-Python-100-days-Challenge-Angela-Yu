# BMI Calculator 2.0 
height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))
# --------------------------------------------

BMI = round(weight / height**2)
print(f"Your bmi is {BMI}")

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are Underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you are normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are Overweight.") 
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are Obese.")    
else : 
    print(f"Your BMI is {BMI}, you are Clinically obese.")