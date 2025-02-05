#Programmer: Timothy Pickering
#Date: 2/4/2025
#Title: Age classifier

age = float(input("Enter the person's age: ")) #user input age
def categorize_age(age): #define age category
    if age <= 1:
        ageCategory = "Infant"
    elif 1 < age < 13:
        ageCategory = "Child"
    elif 13 <= age < 20:
        ageCategory = "Teenager"
    else:
        ageCategory = "Adult"
    return ageCategory
ageBucket = categorize_age(age) #assign variable to categorized age
print (ageBucket) #display age
