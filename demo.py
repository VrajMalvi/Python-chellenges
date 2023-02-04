# s = input("What is your name? : ")

# print("Hello " + s)  #both + and , works in case of string

# # go to this website to break complex codes : http://pythontutor.com/visualize.html#mode=edit

# print("Length of name: ", len(s))   
# #herre cant use + for adding bcoz error cant convert int to str so use comma for inbuilt function

# #Data types

# #String
# print("hello"[0])  #subscripting

# #Integer

# print(123_456) # it will print 123456 here _(underscore is counted as just comma to saperate number and ignored by compiler just for us humans to understand figure)

# print("hello" + str(6)) #type conversion


# #this code add input deit like 26 will be 8 (2 + 6)
# num = input("Enter two degit number : ") #type of input numbber will str
# num1 = int(num[0])
# num2 = int(num[1])
# result = num1 + num2
# print(result)

# #or 

# print(int(num[0]) + int(num[1]))

# #Note :- type of result of div(/) always gonna be float

# gg = 2 ** 8 # for power use **
# print(gg)

#BMI calculator

# weight = float(input("Weight : "))
# height = float(input("Height : "))

# BMI = int(weight / (height ** 2))

# print(f"BMI =  {BMI}") #f-string put f before quots now we can print var in {} regardless of type

# print(round(8 / 3))

# print( 8 // 3 )  #floor devision directly convert ans to int

# # remaining days months and week calc if your max age is 90
# age = int(input("Enter your age : "))

# r_age = 90 - age

# days = r_age * 365
# weeks = 52 * r_age
# months = 12 * r_age

# print(f"You have {days} days, {weeks} weeks and {months} months left.")

#if - else satement

# print("welcome to the rollercoster!")
# height = int(input("What is your height in cm? : "))

# if height >= 120:           # == checking values right and left ,, === check value and type
#     print("You can ride the rollercoster!")
# else:
#     print("Sorry, you gave to grow taller before you can ride."

#even odd

# num = int(input("Enter a number : "))
# if num % 2 ==0:
#     print("Even number")
# else:
#     print("Odd number")

# print("welcome to the rollercoster!")
# height = int(input("What is your height in cm? : "))

# if height >= 120:           # == checking values right and left ,, === check value and type
#     print("You can ride the rollercoster!")
#     age = int(input("Enter your age : "))
#     if age < 12:
#         print("please pay $5.")
#     elif age >= 12 & age <= 18:
#         print("please pay 7.")
#     else:
#         print("please pay $12.")
# else:
#     print("Sorry, you gave to grow taller before you can ride.")


# weight = float(input("Weight : "))
# height = float(input("Height : "))

# BMI = round(weight / (height ** 2))

# if BMI < 18.5:
#     print(f"your BMI is {BMI}, Underweiht.")
# elif BMI >= 18.5 and BMI < 25:
#     print(f"your BMI is {BMI}, Normal weight.")
# elif BMI >= 25 and BMI < 30:
#     print(f"your BMI is {BMI}, slightly overweight.")
# elif BMI >= 30 and BMI < 35:
#     print(f"your BMI is {BMI}, obese.")
# else:
#     print(f"your BMI is {BMI}, clinically obese.")

# #leap year9
# year = int(input("Enter year to check it is leap or not : "))

# if year % 4 == 0:
#     if (year % 100 != 0) or (year % 400 == 0):
#             print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# print("welcome to the rollercoster!")
# height = int(input("What is your height in cm? : "))
# bill = 0

# if height >= 120:           # == checking values right and left ,, === check value and type
#     print("You can ride the rollercoster!")
#     age = int(input("Enter your age : "))
#     if age < 12:
#         bill = 5
#         print("please pay $5.")
#     elif age >= 12 & age <= 18:
#         bill = 7
#         print("please pay 7.")
#     else:
#         bill = 12
#         print("please pay $12.")

#     wp = input("Do you want a photo taken? Y or N. : ")
#     if wp == "Y":
#          bill += 3

#     print(f"your total amount to pay is ${bill}")    
   
# else:
#     print("Sorry, you gave to grow taller before you can ride.")

# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L : ")
# add_pepperoni = input("Do you want pepperoni? Y or N : ")
# extra_cheese = input("Do you want extra cheese? Y or N : ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bill = 0
# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
   
# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
    
# else:
#     bill = 25
#     if add_pepperoni == "Y":
#         bill += 3
   
# if extra_cheese == "Y":
#     bill += 1
    
# print(f"Your final bill is ${bill}")

#********************** Love Calculator ************************
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1 = name1.lower()
# name2 = name2.lower()
# name = name1 + name2

# T = name.count("t")
# R = name.count("r")
# U = name.count("u")
# E = name.count("e")
# t1 = T + R + U + E

# L = name.count("l")
# O = name.count("o")
# V = name.count("v")
# E = name.count("e")
# t2 = L + O + V + E

# # tt= str(t1) + str(t2)  
# # t= int(tt)
# #or 

# t = t1 * 10  + t2

# if t <= 10 or t >= 90:
#     print(f"Your score is {t}, you go together like coke and mentos.")
# elif t >= 40 and t <= 50:
#     print(f"Your score is {t}, you are alright together.")
# else:
#     print(f"Your score is {t}.")

#************************  END **************************

#**********************  //// Treasure hunt //// ****************

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# lor = input('You\'re at crossroad, Wchich way? "Left" or "Right" : ').lower()

# if lor == "left":
#     sow = input("Swim or Wait? : ").lower()
#     if sow == "wait":
#         wd = input("Which door? Red, Blue or Yellow : ").lower()
#         if wd == "yellow":
#             print("You win!")
#         elif wd == "red":
#             print("Burned by fire.\nGame Over.")
#         elif wd == "blue":
#             print("Eaten byy Beasts.\nGame Over.")
#         else:
#             print("Game over.")
#     else:
#         print("Attacked by trout.\nGame Over.")
# else:
#     print("Fall into hole.\nGame Over.")

#***************************** ///// END ///// ****************************


#******************************** Randomization and lists *****************************

# import random 

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()   # prints random number from [0,1)
# print(random_float)

# random_integer = random.randint(1, 2)
# if random_integer == 1:
#     print("Heads")
# elif random_integer == 2:
#     print("Tails")

#///////////////////////  end ///////////////////////

#********************** List ***********************

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # print(states_of_america[-1])

# # states_of_america[1] = "pencilvaniia"       #edit
# # states_of_america.append("vraj")            # addition at last
# states_of_america.extend(["malvi", "meet", "gandhi"])   # add list 

# print(states_of_america)

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]



#***************************** practical of list and random *****************************
#//////////////////////// who will buy the meal

# Split string method
# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# length = len(names) - 1
# random_listno = random.randint(0, length)
# print(f"{names[random_listno]} will pay the bill.")

#more about random : https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

#more about lists: https://www.askpython.com/python/string/convert-string-to-list-in-python

# ab = "vraj"
# print(list(ab))   # list convert string to list of single character

#NOTE: you can generate random iteam from specific list using random.choice(_name of list var_)

#***************************** END */****************************

#***//*/*/*/*/*/*/*/*/*/*/*/**/*/*/*/*/  nested list
# a = ["a", "b", "c", "d"]
# b = ["1", "2", "3"]
# ab = [a, b]
# print(ab[1][1])  # it iwll print 2 because first [1] is fo b list and in b list 1th element

#////////////////////////////////// exersice IMP ONE  *********

# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# position = list(position)
# col = int(position[0]) - 1
# row = int(position[1]) - 1

# map[row][col] = "X"

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

#******************************** ROCK paper Scissors ************************

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code above this row 👆

# rps = [rock, paper, scissors]

# user = int(input("What do tou choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user <= 2:
#     print(rps[user])

#     computer = random.choice(rps)
#     print(f"Computer chose:\n{computer}")

#     if user == 0:
#         if computer == scissors:
#             print("You win!")
#         elif computer == paper:
#             print("You lose!")
#         else:
#             print("Draw!")
#     elif user == 1:
#         if computer == scissors:
#             print("You lose!")
#         elif computer == rock:
#             print("You win!")
#         else:
#             print("Draw!")
#     elif user == 2:
#         if computer == paper:
#             print("You win!")
#         elif computer == rock:
#             print("You lose!")
#         else:
#             print("Draw!")
# else:
#     print("Wrong input")

#//////////// or


# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")


# /////////////////////////////////////// END of list and random

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// LOOOPS /////////////////////////////////////////////////////

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# count = 0
# total = 0
# for i in range(0, len(student_heights)):
#     count += 1
#     total += student_heights[i]

# avg = round(total / count)
# print(f"Avarage : {avg}")

#/*/*/**/**/**/**/*/ same code in short cut 7 to 2

# avg = sum(student_heights) / len(student_heights)
# print(avg)


#NOTE: max and min

# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

#Write your code below this row 👇

# print(max(student_scores), min(student_scores))

# or

# temp = student_scores[0]
# for i in range(1 , len(student_scores)):
#     if temp < student_scores[i]:
#         temp = student_scores[i]
# print(f"Max : {temp}")
        
# for i in range(1, 11, 2):   #jump 2 steps
#     print(i)

# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# t = 0
# for i in range(2, 101, 2):
#     t += i
# print(t)

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i %3 == 0:
#         print("Fizz")
#     else:
#         print(i)

#****------------------------------- password generator -------------------------------------

# #Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""

# for i in range(0, nr_letters):
#     password += random.choice(letters)

# for i in range(0, nr_numbers):
#     password += random.choice(numbers)

# for i in range(0, nr_symbols):
#     password += random.choice(symbols)

# print(f"Your pass: {password}")


#Hard Level - Order of characters randomised:  ------------------------------------ hard level
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# import string_utils
# string = string_utils.shuffle(password)
# print(f"Your password: {string}")

# OR 

# l = list(password)     # convert stting to list
# random.shuffle(l)       # shuffle list
# result = ''.join(l)     # convert list to string using ''.join(var)
# print(f"Your password: {result})

#OR 

# password_list = []

# for char in range(1, nr_letters + 1):
# 	password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
# 	password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
# 	password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""    #to convert list to string
# for char in password_list:
# 	password += char

# print(f"Your password is: {password}")

# def my_function():
#     print("my fun")

# my_function()


#---------------------------- END of loop -**--*--*--*--*-*---*-*-*--*--*-*-*--*-*

