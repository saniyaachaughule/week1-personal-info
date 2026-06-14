#Name: Saniya Choughule
# Personal Information Manager

print("="*50)
print("Personal Information Manager")
print("="*50)
print()

#Static Information
name="Saniya Choghule"   #storing personal information 
age=21
city="Mumbai"
hobby="Dancing"

#User Input
favorite_food=input("Enter your favorite food:").strip()
#validation for favorite food
while favorite_food=="":
    print("Food cannot be empty!")
    favorite_food=input("Enter your favorite_food:").strip()

favorite_color=input("Enter your favorite color:").strip()
#validation for favorite color
while favorite_color=="":
    print("Color cannot be empty!")
    favorite_color=input("Enter your favorite color:").strip()

#age calculation
age_in_months=age*12

#Display Info
print("\n" + "=" * 40)
print("Your Information")
print("=" * 40)

print(f"Name          :{name.title()}")
print(f"Age           :{age}years")
print(f"Age in months :{age_in_months}")
print(f"City          :{city.title()}")
print(f"Hobby         :{hobby.title()}")
print(f"Favorite Food :{favorite_food.title()}")
print(f"Favorite Color:{favorite_color.title()}")

#Good Bye message
print("\n" + "=" * 40)
print("Thank you for using this program!")
print("=" * 40)

