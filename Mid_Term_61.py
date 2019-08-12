import random
print("+++++ Welcome to c++ Midterm test +++++")
name = input("Please Enter your first-name : ")
lname = input("Please Enter your last-name : ")
print()
print("+++++++++++++++++++++++++++++++")
print("Please Enter your Birthday.")
while True :
    day = int(input("Input Birth-day (1-31): "))
    if day >= 1 and day <= 31 :
        break
while True :
    month = input("Input Birth-month (1-12): ")
    if int(month) >= 1 and int(month) <= 12 :
        break
while True :
    year = int(input("Input Birth-year (1950-2019) (Like 2018): "))
    if year >= 1950 and year <= 2019 :
        break
print()
print("+++++++++++++++++++++++++++++++")
while True :
    Gender = input("Please Enter your Gender (f = female , m = male) : ")
    if Gender == "f" or Gender == "F" or Gender == "m" or Gender == "M" :
        if Gender == "f" or Gender == "F" :
            Gender = "Mr. "
        else :
            Gender = "Ms. "
        break
print()
print("+++++++++++++++++++++++++++++++")
print(f"Hello {Gender}{name} {lname}")
print()
if int(month) == 1 :
    month = "Jan"
elif int(month) == 2 :
    month = "Feb"
elif int(month) == 3 :
    month = "Mar"
elif int(month) == 4 :
    month = "Apr"
elif int(month) == 5 :
    month = "May"
elif int(month) == 6 :
    month = "Jun"
elif int(month) == 7 :
    month = "Jul"
elif int(month) == 8 :
    month = "Aug"
elif int(month) == 9 :
    month = "Sep"
elif int(month) == 10 :
    month = "Oct"
elif int(month) == 11 :
    month = "Nov"
elif int(month) == 12 :
    month = "Dec"
print(f"Your Birth day is : {month} {day} {year}")
print(f"And now you have : {2019-year} year old.")
print("+++++++++++++++++++++++++++++++")
r = random.randint(1,9)
if r == 1:
    colortext = "Red"
elif r == 2:
    colortext = "Pink"
elif r == 3:
    colortext = "Green"
elif r == 4:
    colortext = "Yellow"
elif r == 5:
    colortext = "Blue"
elif r == 6:
    colortext = "Violet"
elif r == 7:
    colortext = "Brown"
elif r == 8:
    colortext = "Silver"
elif r == 9:
    colortext = "Black"
print(r)
print("Your Luckey Color is : ","*"*r ,colortext)
print()


    
    












    

