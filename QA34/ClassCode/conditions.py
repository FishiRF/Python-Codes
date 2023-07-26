# e1 - write a python code to check if person is eligible to vote
#  eligible voting age = 16 and print
age = int(input("Please enter your age: "))
if age >= 16:
    print("You are eligible to vote")
else:
    print("You can't vote yet maybe next time")
# e2 - write a python program to check whether a number is odd or even
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
# e3 - write a python program to print the new price of the items
# if the items cost between 100 and 500 print the price with 30% discount
# else print the price with the 20%
items_price = float(input("Please enter the price of the item: "))
if 100 < items_price < 500:
    print(f"The price after discount is: {items_price * 0.7}")
else:
    print(f"The price after discount is: {items_price * 0.8}")

