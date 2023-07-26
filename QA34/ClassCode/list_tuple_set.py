# 1
# כתוב תוכנית שקולטת מהמשתמש 7 מספרים ומדפיסה את הסכום של המספרים
# המספר הגדול ביותר
# הממוצע של כל המספרים
# numbers = []
# for i in range(7):
#     numbers.append(int(input("Please enter a number: ")))
# print(max(numbers)) # the highest number in the list
# print(sum(numbers)) # the sum of the list
# print(sum(numbers) / len(numbers)) # average
#------------------------------------------------------------------------------
# 2
# כתוב תוכנית העוברת על הרשימה הזאת ומדפיסה כל ערך חיובי
# [-22, 14, 555, 616, -99, -414, 156, 0.266]
# num_list = [-22, 14, 555, 616, -99, -414, 156, 0.266]
# for num in num_list:
#     if num > 0:
#         print(num)
#------------------------------------------------------------------------------
# 3
# כתוב תוכנית המבקשת מהמשתמש להכניס מספר ומדפיסה לו hello מספר הפעמים שהוא ביקש
# times = int(input("Please enter a number: "))
# for i in range(times):
#     print("Hello")
#------------------------------------------------------------------------------

# כתבו תוכנית בפייתון שעוברת על הרשימה הבא ומדפיסה כל מילה שמכילה את האות 'n'
# ['hello', 'my', 'Name', 'is', 'not', 'Tal', 'or', 'roni']
# wordslist = ['hello', 'my', 'Name', 'is', 'not', 'Tal', 'or', 'roni']
# for word in wordslist:
#     if 'n' in word.lower():
#         print(word)
#------------------------------------------------------------------------------

# given the following list
# ws = ['121', 'tot', 'dead', 'yoomaay', 'choco']
# print all the words that starts and ends with sam char

ws = ['121', 'tot', 'dead', 'yoomaay', 'choco', 'dead', 'tot']
for word in ws:
    if word[0] == word[-1]:
# another option - if word.startswith(word[0]) AND word.endswith(word[0])]:
        print(word)
print(ws)
# write a python program that remove duplicates from a list
# option 1
print(set(ws))
# option 2
list =[]
for word in ws:
    if word in list:
        continue
    list.append(word)
print(list)



