# 1.
# מתי כדאי להשתמש בלולאה?
# we use loop when we need to repeat a certain block of code multiple times
# -----------------------------------------------------------------------
# 2.
# של לולאה בפייטון? syntax מה ה
# for range:
# for index in range(start, stop, step):
# for list:
# for name in names:
# while:
# while condition:
# -----------------------------------------------------------------------
# 3.
# וארצה לעבור בלולאה על מחצית , [100, 8, 7, 5 ,1] אם נתונה לי רשימה של מספרים, לדוגמא
# המספרים הראשונים, כיצד אכתוב זאת?
list = [1, 5, 7, 8, 100]
for num in range(len(list) // 2):   # splitting the range of the list in half
    print(list[num])
# -----------------------------------------------------------------------
# 4.
# כתוב לולאה העוברת .[‘hello’, ‘python’, ‘pen’, ’world of coding’] :  ייצר רשימה של מילים לדוגמא
# על הרשימה ומדפיסה כל מילה באותיות גדולות
words_list = ['hello', 'python', 'pen', 'world of coding']
for word in words_list:
    print(word.upper())
# -----------------------------------------------------------------------
# 5.
# שנה את תרגיל 4, אם נתקלת במילה הקצרה מ- 4 אותיות, צא מהלולאה
words = ['hello', 'python', 'pen', 'world of coding']
for word in words:
    if len(word) < 4:
        break
    print(word.upper())

# -----------------------------------------------------------------------
# 6.
# צור מחרוזת המכילה את שמך המלא: פרטי + משפחה )מופרד ברווח)
# • הדפס את חמשת התווים האחרונים במחרוזת
# • הדפס את השליש הראשון של המחרוזת
# מופיעה במחרוזת ‘a ‘ • ספור כמה פעמים האות
# מופיעה במחרוזת (מחזירה אמת/שקר) ‘b ‘ • כתוב פקודה הבודקת האם האות
# • הפרד את המחרוזת לרשימה המכילה בתא הראשון את שמך הפרטי ובתא השני את
# שם המשפחה שלך
# • הפוך את סדר האיברים ברשימה
# • שנה את שם המשפחה לאותיות גדולות
# • הסר את התו האמצעי משמך הפרטי
# • צור והדפס מחרוזת המכילה את שמך המלא לאחר השינוי
# Input
fullname = input("Please enter your full name: ")
first_third = len(fullname) // 3
letter_a = 'a'
letter_b = 'b'
name_list = fullname.split()    # splitting the string into two strings and switching to list
# Output
print(f'The first 5 letters in the name are {fullname[:5]}')
print(f'The first third of the full name is {fullname[:first_third]}')
count = fullname.count('a')
print(f"The count number of the letter a is {fullname.count('a')}")     # counting the letter 'a' in the string
print('b' in fullname)    # checking if the letter b is in the string and printing true or false
print(name_list)    # printing the list with the first name and last name
name_list.reverse()    # switching places in a list
print(name_list)
# another option
# print(name_list[::-1]
name_list[0] = name_list[0].upper()
print(name_list)
mid_index = len(name_list[1]) // 2  # splitting the length in 2
name_list[1] = (name_list[1])[:mid_index] + (name_list[1][mid_index + 1:])  # removing the middle letter
print(name_list)
names = ' '    # creating a string format
new_name = names.join(name_list)    # converting a list into a string
print(new_name)
# -----------------------------------------------------------------------
# 7.
# “Hello world!” : הראשונה + האחרונה במשפט ‘o ‘  הדפס את מיקום האות
# הראשונה ‘o ‘ הדפס את המשפט מתחילתו ועד ל
# האחרונה ועד לסוף המשפט - ‘o ‘ הדפס את המשפט מה
# Input
sen = 'Hello world!'
# Output
print(f"{sen.find('o')}, {sen.rfind('o')}")    # printing the indexes of the letter 'o' in general
print(sen[:sen.find('o')])  # printing the sentence from the beginning to the last 'o'
print(sen[sen.rfind('o'):])    # printing the sentence from the last 'o' to the end of the sentence
# -----------------------------------------------------------------------
# 8.
# ‘o’ ללא האות “Hello World” הדפס את המשפט
sen = 'Hello World'
sen.lower().replace('o', '')
print(sen.replace('o', ''))
# -----------------------------------------------------------------------
# 9.
# [8, 1000, -3, 2, צור רשימה של חמישה מספרים: [ 5
# הדפס את סכום הרשימה
# הדפס את האיבר הגדול ביותר
# הדפס את האיבר הקטן ביותר
# הדפס את ממוצע הרשימה )סכום הרשימה חלקי אורך הרשימה(
# הסר את האיבר האמצעי ברשימה
# מיין את הרשימה
# הדפס את הרשימה משוכפלת 5 פעמים
# הסר מהרשימה את האיבר הראשון
# צור תת רשימה המכילה את כל האיברים הקטנים מהממוצע
# Input
numlist = [8, 1000, -3, 2, 5]
# Processing
print(f'Sum: {sum(numlist)}')
print(f'Maximum: {max(numlist)}')
print(f'Minimum: {min(numlist)}')
avg = sum(numlist) / len(numlist)
print(f'Average: {avg}')
half_list = len(numlist) // 2
numlist = numlist[:half_list] + numlist[half_list + 1:]
print(f'List without the middle value: {numlist}')
numlist.sort()
print(f'Sorted list: {numlist}')
print('The list * 5:')
for i in range(1, 6):
    print(f'{i}. {numlist}')
numlist.pop(0)
print(f'List without the first value: {numlist}')
min_list = []
for num in numlist:
    if num < avg:
        min_list.append(num)
    else:
        continue
# Output
numlist.append(min_list)
print(f'List with a list below the avg in it: {numlist}')
# -----------------------------------------------------------------------
# 10.
# *אתגר: ייצר רשימה של מספרים. לדוגמא: . [1, 5, 7, 8, 100] . כתוב לולאה העוברת על הרשימה
# ומוצאת את האיבר הגדול ביותר )ללא שימוש בפונקצית max )
# Input
num_list = [1, 5, 7, 8, 100]
max_num = num_list[0]   # we assume the first number in the list will be the highest number to begin with
# Processing
for num in num_list:
    if num > max_num:
        max_num = num
# Output
print(f'The highest number is the list is: {max_num}')
# -----------------------------------------------------------------------
# 11.
# . **אתגר: ייצר רשימה של רשימות. לדוגמא: [ [4, 8, 200], [4, 3000, -1], [5, 87, 12] ] . כתוב לולאה
# בלוך לולאה העוברת על כל הרשימות ומוצאת את המספר הקטן ביותר )ללא שימוש בפונקציית min
# Input
matrix = [[4, 8, 200],
          [4, 3000, -1],
          [5, 87, 12]]
min_num = matrix[0][0]  # we assume the first number is the matrix lowest number to begin with
# Processing
for num_list in matrix:
    for num in num_list:
        if num < min_num:
            min_num = num
# Output
print(f'The lowest number in the matrix is: {min_num}')
