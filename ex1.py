from datetime import date


print("Enter your name")
name = input()
print("Enter your age")
age = int(input())
year_today = int(date.today().strftime("%Y"))
year_in_100 = year_today + (100 - age)
print(name + " you will be 100 years in the year " + str(year_in_100))
