# 1. מה עושה הפקודה input? איזה סוג של טיפוס היא מחזירה?
# פקודה שמכניסה קלט מהמשתמש, ומחזירה את str data type

#-------------------------------------------------------------------------------

# 2. כיצד ניתן להפוך את טיפוס המוחזר של input להיות מספר שלם? עשרוני?
# int(input('Please enter int')
# float(input('Please enter float')

#-------------------------------------------------------------------------------

# 3. מה עושה הפונקציה split ?איזה טיפוס היא מחזירה? אם רוצים שההפרדה ב split לא תהיה על ידי
# רווח, כיצד ניתן לעשות זאת?
# פונקציה שמפרידה str ומחזירה אותו כרשימה

#-------------------------------------------------------------------------------

# .4 מה עושה הפקודה format ?כיצד זה חוסך כתיבה?
# מאפשרת כתיבת משתנים ביחד עם משתנים בזמן ההדפסה

#-------------------------------------------------------------------------------

# .5 מה עושה הפעולה in) בין איבר לרשימה)?
# בודקת אם האיבר מופיע בתוך הרשימה

#-------------------------------------------------------------------------------

# .6 כיצד כותבים תנאים בפייטון? מה ההבדל בין else לבין elif?
# בelif מוסיפים התניה לעומת else שאוטומטית שולל השאר

#-------------------------------------------------------------------------------

# .7 כיצד הפייטון יודע אם שורות קוד שייכת ל if או לא?
# אם יש TAB ביניהם או לא

#-------------------------------------------------------------------------------

# .8 כתוב תוכנית פייטון הקולטת שני מספרים ומדפיסה את הגדול מבין שניהם
# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter another number: "))
# if(num1 > num2):
#     print(f'The biggest number is {num1}')
# else:
#     print(f'The biggest number is {num2}')
# # another option
# print(f'The biggest number is {max(num1,num2)}')
# # another option
# print(f'{num1 if num1 > num2 else num2}')

#-------------------------------------------------------------------------------

# .9 כתוב תוכנית פייטון הקולטת שלושה מספרים ומדפיסה את ההכי גדול
# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter another number: "))
# num3 = int(input("Please enter another number: "))
# print(max(num1, num2, num3))

#-------------------------------------------------------------------------------

# .10 *אתגר: כתוב תוכנית פייטון הקולטת תרגיל חיבור ומדפיסה אם הוא נכון או לא, לדוגמא ייקלט:
# 3 + 4 = 7
# אז יודפס TRUE) שים לב שיש רווחים בקלט בין הספרות)
# ואם ייקלט:
# 2 + 3 = 9
# אז יודפס FALSE
# form = input("Please enter the formula: ")
# form = form.split()
# print(form)
# print(int(form[0]) + int(form[2]) == int(form[4]))

#-------------------------------------------------------------------------------

# 11. **אתגר: האם תוכל לפתור את שאלה 10 עבור יותר מסימן אחד?
# form = input("Please enter the formula: ")
# form = form.split()
# if form[1] == '+':
#     print(int(form[0]) + int(form[2]) == int(form[4]))
# elif form[1] == '-':
#     print(int(form[0]) - int(form[2]) == int(form[4]))
# elif form[1] == '*':
#     print(int(form[0]) * int(form[2]) == int(form[4]))
# elif form[1] == '//':
#     print(int(form[0]) // int(form[2]) == int(form[4]))

#-------------------------------------------------------------------------------

# Class Exercises
# Exercise 1
# כתבו תוכנית בפייתון הקולטת 4 מספרים ואם ממוצע המספרים כפול 2 גדול מהמספר הגדול תדפיסו I wish!!!
# num1 = float(input("Please enter a number: "))
# num2 = float(input("Please enter a number: "))
# num3 = float(input("Please enter a number: "))
# num4 = float(input("Please enter a number: "))
# sum_nums = num1 + num2 + num3 + num4
# avg_nums = sum_nums / 4
# max_nums = max(num1, num2, num3,num4)
# if avg_nums * 2 > max_nums:
#     print("I wish!!!")
# else:
#     print("Oh no!!!")
# another option
# numbers = []
# numbers.append(float(input("Please enter a number: ")))
# numbers.append(float(input("Please enter a number: ")))
# numbers.append(float(input("Please enter a number: ")))
# numbers.append(float(input("Please enter a number: ")))
# avg = sum(numbers) / len(numbers)
# maximum = max(numbers)
# if avg * 2 > maximum:
#     print("I wish!!!")
# else:
#     print("Oh no!!!")

#-------------------------------------------------------------------------------

# כתבו תוכנית שמוסיפה את הרשימה numbers = [100, 10, 88, 56, 22, 44, 1]
# הדפיסו את הרשימה בסדר עולה
# הדפיסו את הרשימה בסדר יורד
# הדפיסו את הרשימה ללא הספרה 88
# הוסיפו לסוף הרשימה את הספרה הכי גבוהה שנמצאת ברשימה
numbers = [100, 10, 88, 56, 22, 44, 1]
numbers.sort()
print(numbers)
# print(numbers[::-1])
# another option
# numbers.sort(reverse=True)
# print(numbers)
numbers.remove(88)
print(numbers)
numbers.append(max(numbers))
print(numbers)

