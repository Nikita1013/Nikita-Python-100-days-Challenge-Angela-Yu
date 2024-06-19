# Calculate the Total months, weeks and days left based on the age
age = input("What is your current age ? \n")
# -----------------------------------------
# Converta age to int as it is in string
age_int = int(age) 
# Years
years_remianing = 90 -  age_int
days_remaining =  years_remianing * 365
weeks_remaining =  years_remianing * 52
months_remianing = years_remianing * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remianing} months left.")