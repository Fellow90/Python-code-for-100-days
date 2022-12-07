#calculating your age left assuming you will live for exact 90 years
age = int(input("What is your current age?"))
print("Your current age is: " +str(age))
age_left = 90 - age
age_in_days = age_left * 365
age_left_in_months = age_in_days // 12
age_left_in_weeks = (age_in_days - (12 * age_left_in_months)) // 7
age_left_in_days = age_in_days - 12 * age_left_in_months - 7 * age_left_in_weeks
print(f"You have {age_left_in_months} months, {age_left_in_weeks} weeks and {age_left_in_days} days left in total::"
)