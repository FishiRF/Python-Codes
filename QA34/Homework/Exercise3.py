# .1
# מתי כדאי להשתמש ב range בלולאת for?
# when you need to write a code more than once when we know the range
# ---------------------------------------------------------------------------------
# .2
# כיצד אפשר להגדיר range עם קפיצות? כיצד אפשר להגדיר range עם מספרים בסדר יורד?
# for i in range(0, 10, 2)    # range loop in jumps 2
# for i in range(10,0,-1)   # descending loop
# ---------------------------------------------------------------------------------
# .3
# כיצד אפשר לייצר list מתוך range?
# names = [1,2,3,4,5,6,7]
# for name in names:
# ---------------------------------------------------------------------------------
# .4
# מדוע יש צורך בלולאות מסוג while ו- while-do?
# to add a condition to the loop and when we dont have a range
# ---------------------------------------------------------------------------------
# .5
# מה ההבדל בין לולאת while לבין לולאת while-do?
# do-while is a loop that evaluates the code after executed at least once
# and while is a loops that evaluates the code before execution
# ---------------------------------------------------------------------------------
# .6
# כיצד אפשר בפייטון לממש לולאת while-do?
# num = 0
# while True:
#     print(num)
#     num += 1
#     if num >= 5:
#         break
# ---------------------------------------------------------------------------------
# .7
# מה ההבדל בין break לבין continue ?מדוע כדאי להשתמש ב- continue?
# when you use break the loop will stop and you will continue the code outside the loop
# when you use continue the loop will start again immediately and not continue further
# you want to use continue when you dont want to exit the loop but only
# to return to the beginning of the loop
# ---------------------------------------------------------------------------------
# .8
# כתוב תוכנית המדפיסה את כל המספרים השלמים מ- 200 ועד 2 בסדר יורד
for num in range(200, 1, -1):
    print(num)
# ---------------------------------------------------------------------------------
# .9
# כתוב תוכנית המדפיסה את כל הכפולות של ,7 בטווח שבין 1 ל- 100 )נסה לכתוב בצורה יעילה(
for num in range(1, 100, 7):
    print(num-1)
# ---------------------------------------------------------------------------------
# .10
# כתוב תוכנית הקולטת מספרים עד אשר נקלט מספר שלילי. הדפס את סכום המספרים שנקלט )ללא
# המספר השלילי(
sum1 = 0
while True:
    number = int(input("Please enter a number: "))
    if number < 0:
        break
    sum1 += number
print(f'Sum: {sum1}')
# ---------------------------------------------------------------------------------
# .11
# כתוב תוכנית הקולטת מספר ומדפיסה את העצרת שלו.
# עצרת היא מכפלת המספרים מ 1 ועד המספר
# לדוגמא עצרת של 5 )המסומנת 5!( = 1 * 2 * 3 * 4 * 5 = 120
# עצרת של 3 = 1 * 2 * 3 = 6
assembly = 1
number = int(input("Please enter a number: "))
while True:
    if number > 0:    # the loop will work as long as the user picks a number higher than 0
        for i in range(1, number+1):  # loop from number 1 to user's input included
            assembly *= i    # assembly becomes the multi of itself and the i number in the loop
            if i != number:   # if i is not the last number
                print(i, '*', end=' ')    # prints 'i *' end allows me to stay on the same line in the print
            else:    # if i is the last number
                print(i, '=', assembly)   # prints 'the last number =' assembly
        break    # when the for loop ends completely break the while loop also
    else:     # if the user's input is 0 or less
        number = int(input("Invalid number please try again: "))
# ---------------------------------------------------------------------------------
# .12
# יצר רשימת מספרים ובה חמישה מספרי מזל )ללא כפילויות(.
# כעת תן למשתמש לנחש מספרים, עד אשר הוא יינחש את כל חמשת מספרי המזל. בכל פעם
# שהמשתמש "פגע" במספר מזל, הסר אותו מהרשימה. הלולאה תימשך עד אשר הרשימה תהיה
# ריקה )כלומר, המשתמש ניחש נכון את כל המספרים(. טווח מספרי המזל הוא בין .2-49 אם
# המשתמש הזין מספר לא בטווח הזה, דלג לאיטרציה הבאה )continue).
# בסוף, אחרי שהמשתמש ניחש את נכון כל מספרי המזל )והלולאה הסתיימה(- הדפס למשתמש כמה
# נסיונות לקח לו לנחש את כל המספרים.
# ** אתגר: אם המשתמש ניחש פעמיים את אותו המספר- צא מהלולאה )break )
# *** אתגר: אם לקח למשתמש יותר מ- 20 ניחושים. חזור שוב על הלולאה )ואתחל מחדש את
# הרשימה(. עד אשר המשתמש יצליח לנחש את כל חמשת המספרים בפחות מ- 20 ניחושים
import random
luckylist = []  # empty list
for i in range(5):  # loop for 5 numbers
    random_num = (random.randrange(2, 50))  # randomizing a number from 2 - 49
    if random_num not in luckylist:     # checking that list doesn't have the same number more than once
        luckylist.append(random_num)    # adding the randomized number to the list
print(luckylist)
# luckylist = [7, 3, 23, 47, 18]    # list of lucky numbers i picked
# luckylist2 = [7, 3, 23, 47, 18]   # backup list in case the user tried more than 20 guesses
luckylist2 = luckylist
stored_nums = []    # empty list that will store all the numbers the user picked
tries = 0    # counter for the number of tries the user used
while True:
    if len(luckylist) == 0:    # if the luckylist is empty break the loop
        break
    number = int(input('Please guess the lucky number: '))    # the user inputs a number
    if number in stored_nums:    # if the number is in the stored numbers list
                                 # which means the number was already picked before
                                 # break the loop
        break
    stored_nums.append(number)    # adding the number into the stored numbers list
    tries += 1    # each time the user picks a number the number of tries is added here
    if tries > 20:    # if the user tries more than 20 times
        luckylist = luckylist2    # resetting the  lucky list
        stored_nums = []    # resetting the stored numbers list
        tries = 0    # resetting the number of tries the user did
    if number in luckylist and 2 <= number <= 49:   # if the number is in the lucky list
                                                    # and the number is between 2 to 49
        luckylist.remove(number)    # remove the number from the lucky list
    else:
        print("Hard luck")
        continue    # return to the beginning of the loop
if len(luckylist) == 0:     # print the number of tries if the user guessed all of them right
    print(f'It took you {tries} tries to guess all the lucky numbers')
else:   # print the message if the user picked the number more than once
    print("sorry you can't pick the same number twice")







