from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(shift_c, text_c, direction_c):
    message = ""
    for char in text_c:
        if char in alphabet:     
            if direction_c == 'encode':
                index = alphabet.index(char) + shift_c
                while index >= 25:          #or if shift > 44 then shift % 25 and ans of this will be index
                    if index >= 25:
                        index -= 25
            elif direction_c == 'decode':
                index = alphabet.index(char) - shift_c
                while index < 0:
                    if index <= 0:
                        index += 25
            message += alphabet[index] 
        else:
             message += char  
    print(f"{direction_c}d message : {message}")

#execution starts here
print(logo)
repeat = True

while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(shift, text, direction)

    gg = input("Tyepe 'yes' if you wanna goa gain else type 'no': ").lower()
    if gg == "no":
        repeat = False


# #Write your code below this line 👇   ///// Prime number
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number-1):
#         if number % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print("It's a prime number.")
#     else:
#         print("it's not a prime number.")

# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)




# #Write your code below this line 👇   /// nuber of paint cans required
# import math

# def paint_calc(height, width, cover):
#     paint = (test_h * test_w) / coverage
#     print(f"You'll need {math.ceil(paint)} cans of paint.")
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)