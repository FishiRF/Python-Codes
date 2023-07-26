# 1.
# מהי פונקציה?
# function is a code that does a specific task as a seperate unit and helps
# to organize your main code and makes it more readable
# -----------------------------------------------------------------------
# 2.
# כיצד מגדירים פונקציה בפייטון?
# def function(parameter):
#     the code that the function does
#     return value
# -----------------------------------------------------------------------
# 3.
# כיצד מוסיפים פרמטרים לפונקציה? מה מטרת הפרמטרים? כיצד ניתן לתת ערך ברירת מחדל
# לפרמטרים בפייטון? מה הכלל לגבי השמת ברירת מחדל )בהקשר של יישור(?
# def function(parameters)
# the parameters allow you to pass values from outside the function into the main code that you are working on
# def welcome(name = 'friend')
#     print(f'Welcome',{name})
# if I will provide and argument for this parameter it will override the default value in entered
# the rule is that when you are setting the default value you don't use spaces when you write '='
# -----------------------------------------------------------------------
# 4.
# כיצד ניתן להעביר ערך לפרמטר ספציפי בפונקציה בפייטון?
# def numbersMultiplication(num1, num2):
#     result = num1 * num2
#     return result
# number1 = 5
# number2 = 6
# multi = numbersMultiplication(number1, number2)    # this line is how you pass a value into a specific parameter
# print(multi)
# -----------------------------------------------------------------------
# 5.
# מדוע כדאי שפונקציות יוכלו להחזיר ערך? כיצד פונקציה בפייטון מחזירה ערך?
# functions that return values can be used more than once in the maid code
# def numbersMultiplication(num1, num2):
#     result = num1 * num2
#     return result    # this is how you return a value in a function
# -----------------------------------------------------------------------
# 6.
# בפייטון? מתי הוא בא לידי ביטוי בפונקציות? Empty מה משמעות
# in python Empty means the lack of value
# in functions it can be returning nothing or using an empty data structure
# -----------------------------------------------------------------------
# 7.
# כיצד מייצרים מספר אקראי בפייטון? באיזה ספרייה נשתמש? כיצד נזמין את הספרייה לקוד?
# in order to create a random number in python we need to use the function random from the library
# import random    # this is the name of the library that we need to import
# random_num = random.randint(1, 50)   # randint is the function that generates random integers from 1 to 50
# -----------------------------------------------------------------------
# 8.
# כתוב פונקציה המקבלת רדיוס מעגל ומחזירה את היקף המעגל
# circumference = 2 * PI * radius
import math    # in order to calculate pi we need to import the math library
def circleCircumference(radius):
    circumference = 2 * math.pi * radius   # calculating the circle circumference
    return circumference
# -----------------------------------------------------------------------
# 9.
# כל .x, y פונקציות אלו צריכות לקבל שני פרמטרים add, sub, mul, div : ייצר את הפונקציות הבאות
# add אחת מהן צריכה לחשב את הפעולה המתמטית שהיא מייצגת ולהחזיר את התוצאה )לדוגמא
# מחברת את שני המספרים ומחזירה את הסכום שלהם(.
# קרא לארבעת הפונקציות שכתבת והדפס ,)input כעת קלוט שני מספרים מהמשתמש )באמצעות
# את מה שהן החזירו
# אשר הוא אפס x, y - ל default הוסף ערך
def add(x=5, y=5):
    result = x + y
    return result
# the function adds the 2 values and returns the result
def sub(x=5, y=5):
    result = x - y
    return result
# the function subtracts the 2 values and returns the result
def mul(x=5, y=5):
    result = x * y
    return result
# the function multiplies the 2 values and returns the result
def div(x=5, y=5):
    result = x / y
    return result
# the function divides the 2 values and returns the result
# Input
number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number: "))
# Processing
add_result = add(number1, number2)  # using the addition function
sub_result = sub(number1, number2)  # using the subtraction function
mul_result = mul(number1, number2)  # using the multiplication function
div_result = div(number1, number2)  # using the division function
# Output
print(f"addition result: {add_result}\n"
      f"subtraction result: {sub_result}\n"
      f"Multiplication result: {mul_result}\n"
      f"division result: {div_result}")
# -----------------------------------------------------------------------
# 10.
# הפונקציה אמורה לקלוט .min, max : אשר מקבלת שני פרמטרים getInRange כתוב פונקציה בשם
# מספר מהמשתמש בלולאה, עד אשר המספר שייקלט יהיה בטווח שנשלח. לדוגמא אם יישלח
# אז הפונקציה תקלוט מספרים מהמשתמש עד אשר המספר שנקלט יהיה בין max=100 - ו min=10
# את )return 10 לבין 100 )כולל(. אחרי שהפונקציה קיבלה קלט "חוקי" היא מחזירה )באמצעות
# המספר "החוקי" שהמשתמש הקליד
def getInRange(min=0, max=100):
    while True:
        number = int(input(f"Please enter a number between {min} and {max}: "))
        if min <= number <= max:
            return number
        else:
            print("The number is not in range please try again")
# The function gets a minimum and maximum numbers and takes from the user a number
# in the range of the parameters and returns the number if it's valid
# Input
number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))
# Processing
if number1 < number2:
    valid_num = getInRange(number1, number2)    # getting the valid number from the function we built
else:
    valid_num = getInRange(number2, number1)
# Output
print(f'The number {valid_num} is valid')
# -----------------------------------------------------------------------
# 11.
# כתוב פונקציה המקבלת שלושה מספרים ומחזירה את הקטן מביניהם
def lowestNum(num1, num2, num3):
    if num2 > num1 < num3:
        return num1
    elif num2 < num3:
        return num2
    else:
        return num3
# the function gets 3 numbers and returns the lowest number
# Input
number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a second number: "))
number3 = int(input("Please enter a third number: "))
# Processing
low_num = lowestNum(number1, number2, number3)
# Output
print(f'The lowest number is: {low_num}')
