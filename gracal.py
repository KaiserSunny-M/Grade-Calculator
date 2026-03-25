name = input("Enter Name: ")
english = float(input("Enter English Grade: "))
science = float(input("Enter Science Grade: "))
math = float(input("Enter Math Grade: "))

grade = (english + science + math) / 3

print("Hello,", name + "!")
print("Your grade is", round(grade, 2))

if grade >= 75:
    print("You passed!")
else:
    print("You failed.")

if grade >= 98:
    print("You achieved: Highest Honors")
elif grade >= 95:
    print("You achieved: With High Honors")
elif grade >= 90:
    print("You achieved: With Honors")
elif grade >= 85:
    print("You achieved: Achiever")
else:
    print("You achieved: No award")