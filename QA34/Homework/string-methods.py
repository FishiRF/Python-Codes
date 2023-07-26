# Exercise 1
# כתבו תוכנית המקבלת מהמשתמש את מספר הת״ז שלו כטקסט והדפס
# אמת אם המספר האחרון הוא 0 ושקר אם זה כל מספר אחר
# input
id_number = input("Enter your ID number: ")
last_digit = int(id_number[-1]) # converting the last digit in the id number into integer
is_last_digit_zero = (last_digit == 0) # comparing the last digit to zero to verify true or false
# output
print(is_last_digit_zero) # printing true or false depending if the last digit is 0 or not
# אופציה נוספת
positive = True
negative = False
id_number = input("Please enter your ID number: ")
while (len(id_number) == 8):
        if (int(id_number) % 10 == 0):
            print(positive)
        else:
            print(negative)
        id_number = input("Please enter your ID number: ")
        print(id_number[8]=='0')

#-------------------------------------------------------------------------------

# Exercise 2
# כתוב תוכנית המקבלת שם הלקוח ומדפיסה את השם באותיות גדולות
# input
customer_name = input("Please enter your name: ")
# output
print(customer_name.upper()) # printing the customer's name in capital letters

#-------------------------------------------------------------------------------

# Exercise 3
# כתבו תוכנית המקבלת מהמשתמש את מילה ומדפיס את אורכה של המילה
# input
word = input("Please enter a word: ")
# output
print(len(word)) # printing the length of the word that the user entered

#-------------------------------------------------------------------------------

# Exercise 4
# כתבו תוכנית המקבלת את המאכל האהוב עליו של המשתמש ומספר
# הפעמים שהוא אכל את הארוחה הזו בחודש הנוכחי במשתנה אחר,
# והמערכת מדפיסה את המידע הזה בצורה מסודרת
# input
favorite_food = input("Please enter your favorite food: ")
times_eaten = input("Please enter the amount of times that you ate this meal this month: ")
# output
print(f"Your favorite food is {favorite_food} and you ate it {times_eaten} times this month")
# printing the favorite food and the amout of times the user ate it this month

#-------------------------------------------------------------------------------

# Exercise 5
# כתבו תוכנית המקבלת מהמשתמש את שם הכלב שלו ומדפיסה את 3
# התווים הראשונים של השם
# input
dog_name = input("Please enter your dog's name: ")
# output
print(dog_name[:3]) # printing the first 3 letters
