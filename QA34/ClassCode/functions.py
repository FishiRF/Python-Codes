import random


# def avg(*args):     # *args gets more than one value
#     print(sum(args) / len(args))
# def foo(name,*args):    # *args gets more than one value
#     print(name, args)
#     if args:    # if the list is not empty
#         for a in args:
#             print(a)
# def print_only_id(**kwargs):    # returns more than one key
#                                 # and value in dictionary
#     print(kwargs)

# def gen_list(start, end): # return list of the given range
#     list1 = list(range(start, end+1))
#     print(list1)

# def get_random():
#     return random.randint(0, 100)
#
# def love_calc(name:str, crush: str):
#     love = get_random()
#     return f'{name} {love}% {crush}'
#
# # main
# avg(15, 20, 23, 24, 25)
# foo('roni', 'amir', 'orel', 'hodi', 'netanel')
# print_only_id(name='roni', age=29, id=313327603)
# gen_list(15, 20)
# print(love_calc('roni', 'eden'))

# write a function to return maximum number between 3 given numbers
# my_max(1,5,8)
# expected output = 8
#
# def my_max(num1, num2, num3):
#     if num1 < num2 > num3:
#         return f'The maximum number is {num2}'
#     elif num1 > num3:
#         return f'The maximum number is {num1}'
#     else:
#         return f'The maximum number is {num3}'
# print(my_max(1,3,2))
# option 2
# def my_max(num1, num2, num3):
#     return f'The maximum number is {max(num1, num2, num3)}'
# print(my_max(1, 13, 5))
# option 3
# def my_max(*args):  # option 2 with args
#     max_num = max(args)
#     return f' The maxiumum number is {max_num}'
# print(my_max(1, 13, 5))
# ----------------------------------------------------------------------------
# write a function to return maximum number between any given numbers
# def my_max(*args):
#     for i in range(1, len(args)):
#         if args[i - 1] > args[i]:
#             max_num = args[i - 1]
#         else:
#             max_num = args[i]
#     return f'The maximum number is {max_num}'
# print(my_max(1, 2, 3, 4, 7, 5, 3, 9, 12432, 43))
# ----------------------------------------------------------------------------
# כתבו פונקציה המקבלת 3 מספרים ובודקת
# אם המספר השלישי נופל בטווח של 2 המספרים הראשונים
# inside(1,9,5)>>> True
# inside(1,4,5)>>> False
#
# def inside(st, en, num):
#     return st <= num <= en
#     return num in range(st, en+1)    # another option
# print(inside(1, 9, 5))
# print(inside(1, 4, 5))

# file = open('names.txt', 'w')     # deletes the last text and write
                                    # new one to read also use w+
# i = input('insert your name: ')
# file.write('i')
# file.write(i)
# file.close()
#
# file = open('names.txt', 'a')    # adds text to last to read and add use a+
# i = input('insert your name: ')
# file.write('i')
# file.write(i)
# file.close()

# file = open('names.txt', 'r')   # can only read and to use r+ write
#                                 # before the text that you have already written
#
# # print(file.readline())   # one single line
# # print(file.readlines())  # list of all the lines
#
# print(file.read(2))     # prints the first 2 characters
# print(file.tell())      # tells you the index of the curser (מצביע)
# print(file.seek(0))     # change the position of the curser (מצביע)



