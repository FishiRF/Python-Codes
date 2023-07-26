# 1.
# מה עושה פעולת ה – slice על מחרוזת ?
# the slice operator seperate every string that has spaces on it and creates a list out of it
# -----------------------------------------------------------------------
# 2.
# מה עושה פעולת ה – concatenation על מחרוזת?
# it's combining the two strings into one string
# -----------------------------------------------------------------------
# 3.
# מהו List Comprehension ? מתי נשתמש בו ? מה היתרון שהוא מעניק?
# a short way to create new lists by using operations on existing lists
# it provides a compact syntax and combining loops and conditions into one line
# -----------------------------------------------------------------------
# 4.
# מהו dictionary ? מתי נשתמש בו ? מדוע כדאי להשתמש בו?
# a dictionary is an unordered collection of key-value pairs
# Dictionaries are commonly used when you want to store
# and retrieve data based on a specific key rather than a numerical index
# They provide a way to map values to unique keys
# allowing efficient lookup and retrieval of data
# -----------------------------------------------------------------------
# 5.
# מאיזה טיפוסים יכול להיות המפתח ב dictionary ? מאיזה טיפוסים יכול להיות הערך?
# the key type can be int, float, string or tuple (immutable types)
# the value type can be immutable types and also
# mutable types like lists, dictionaries, sets, objects
# -----------------------------------------------------------------------
# 6.
# מהו entry?
# entry is a single key-value pair in dictionary
# -----------------------------------------------------------------------
# 7.
# באיזה פורמט כתוב ה- dictionary ? JSON או XML?
# the format that JSON is written in is dictionary
# -----------------------------------------------------------------------
# 8.
# כיצד נבצע את הפעולות הבאות על dictionary : יצירה, הוספה, דריסה, מחיקה?
# create - dict = {} or dict = {'name': 'Roni', 'age': 29}
# adding a value - dict['name'] = 'Eden', dict['age'] = 28
# changing a value - dict['name'] = 'Fishi'
# deleting a key-value pair - del dict['age']
# -----------------------------------------------------------------------
# 9.
# כיצד אפשר לקבל את כל המפתחות הקיימים ב dictionary?
# you can get all the keys by using the method dict.keys()
# -----------------------------------------------------------------------
# 10.
# כיצד אפשר לקבל את כל הערכים הקיימים ב dictionary
# you can get all the values by using the method dict.values()
# -----------------------------------------------------------------------
# 11.
# נתון המשפט “ I love to eat ice cream in the beach” . השתמש ב List Comprehension כדי:
# • לייצר רשימה של המילים באותיות גדולות
# • לייצר רשימה של אותיות- מהאות הראשונה בכל מילה
# • לייצר רשימה של אותיות- מהאות השלישית בכל מילה )היכן שאפשר(
# • לייצר רשימה של מספרים אשר מייצגים אורך של כל מילה ומילה
# Input
sent = 'I love to eat ice cream in the beach'
sent_list = sent.split() # seperating the string after each space into a list
upper_list = []
let_list =[]
third_let_list = []
len_word_list = []
# Processing
for word in sent_list:
    upper_list.append(word.upper()) # creating list with capital letters
    let_list.append(word[0]) # creating list with the first letter of every word
    if len(word) >= 3:
        third_let_list.append(word[2]) # creating a list with the third letter of every word
    len_word_list.append(len(word)) # creating a list of the length of every word
# Output
print(upper_list)
print(let_list)
print(third_let_list)
print(len_word_list)
# -----------------------------------------------------------------------
# 12.
# השתמש ב List Comprehension כדי לייצר את רשימה של החזקות של 10 , מ- 1 ועד 9
# כלומר 10 בחזקת 1, 10 בחזקת 2... עד 10 בחזקת 9
# Input
number = 10
strength_list = [] # creating an empty list to put all the strengths of the number in it
# Processing
for i in range(1, 10):
    strength_list.append(number ** i) # adding the result of the numbers strength depending on the index that's in the loop
# Output
print(strength_list)
# -----------------------------------------------------------------------
# 13.
# כתוב פונקציה tryGetValue אשר מקבלת מילון + מפתח ובודקת אם המפתח קיים במילון. אם כן
# היא מחזירה את ערכו אחרת- מחזירה None
def tryGetValue(dictionary, key): # creating a function that gets a dictionary and a key
    if key in dictionary:
        return dictionary[key]
    else:
        return None
# the function checks if the key already exists in the dictionary and if so returning its returning the key value
# if the key doesn't exist the function returns None
# -----------------------------------------------------------------------
# 14.
# כתוב פונקציה getSortedKeys אשר מקבלת מילון ומחזירה את רשימת המפתחות הממויינת של
# אותו המילון
def getSortedKeys(dictionary): # creating a function the gets a dictionary
    return sorted(dictionary.keys())
# the function is sorting all the keys in the dictionary and returning the dictionary with keys sorted
# -----------------------------------------------------------------------
# 15.
# כתוב פונקציה mergeDictionary אשר מקבלת שני מילונים כפרמטר, ומחזירה מילון אחד המורכב
# ממיזוג של ערכי שני המילונים שהתקבלו
def mergeDictionary(dictionary1, dictionary2): # creating a function the gets 2 dictionaries
    merged_dict = {**dictionary1, **dictionary2} # ** operator that merge 2 dictionaries
    return merged_dict
# the function is merging the 2 dictionaries into 1 new dictionary and returning the merged dictionary
# -----------------------------------------------------------------------
# 16.
# כתוב תוכנית אשר קולטת מהמשתמש שני ערכים: מס' תעודת זהות + שם מלא. תעודת הזהות
# תשמש בתור המפתח במילון, והשם שנקלט ישמש בתור הערך. ראשית בדוק אם מפתח זה קיים
# במילון- אם כן, אל תדרוס את הערך הקיים והצג הודעה. אם המפתח לא קיים- הוסף ערך זה
# למילון. חזור על הפעולה עד אשר המשתמש יכניס 1 - עבור מספר תעודת הזהות. לאחר שיסתיימו
# כל הקלטים- הדפס את כל ערכי המילון שנצברו: מפתח + ערך
# Input
my_dict = {} # creating an empty dictionary
# Processing
while True:
    id_num = int(input("Please enter your ID number (to EXIT enter 1): "))
    if id_num == 1:
        break   # when the user inputs the number 1 on the ID section the loop breaks
    else:
        if tryGetValue(my_dict, id_num):    # using the tryGetValue function that I built in exercise 13
                                            # in order to check if the key already exists in the dictionary
            print("The data is already in the dictionary")
        else:
            full_name = input("Please enter your full name: ")
            my_dict[id_num] = full_name
            print("The data was added to the dictionary")
# Output
print(my_dict)
