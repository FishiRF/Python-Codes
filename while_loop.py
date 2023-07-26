# write a python program to sum all the user inputs
# until he adds a negative values
# sum = 0
# number = int(input("Please enter a number: "))
# while number >= 0:
#     sum += number
#     number = int(input("Please enter a number: "))
# print(sum)
#------------------------------------------------------------------------------
# Exercise 1
# Write a python program to convert temperatures from Celsius to Fahrenheit
# Formula: Celsius = 5/9 * (Fahrenheit - 32), f = 1.8 * c + 32
# expected output:
# '60 C' is 140 in Fahrenheit
# '45 F' is 7 in Celsius
# temp = input('Please enter a temperature in C or F: ')
# temp_new = temp.split()
# if 'C' in temp:
#     temp_c = int(temp_new[0]) * 1.8 + 32
#     print(f'{temp} is {temp_c} Fahrenheit')
# elif 'F' in temp:
#     temp_f = int((temp_new[0]) - 32) * 5/9
#     print(f'{temp} is{temp_f} Celsius')


# write a python program to check the validity of passwords input by users.
# validation:
# at least 4 letters, at least 2 numbers, min length 6 char, max length 16 char
# if the user insert invalid pass ask him to insert another one
# exit when the password is valid
while True:
    password = input("Please enter a password: ")
    letters = 0
    digits = 0
    for char in password:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
    if 6 <= len(password) <= 16 and digits >= 2 and letters >= 4:
        break
print(password)






