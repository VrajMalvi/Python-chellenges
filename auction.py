from art import logo1
import os


repeat = True
auction = {}

def maxbid(auction_):
    highest = 0
    winner = ""
    for  i in auction_:
        temp = auction_[i]
        if temp > highest:
            highest = temp
            winner = i
    print(f"The winner is {winner} with bid of ${highest}.")

while repeat:
    print(logo1)
    Name = input("What is you name? : ")
    bid = int(input("What is your bid? : $ "))
    new = input("Are there any other bidders? Type 'Yes' or 'No' : ").lower()
    auction[Name] = bid

    if new == "no":
        repeat = False
    os.system('cls')


maxbid(auction)





# travel_log = [            #complex experiment
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_, visit_, city_):
#     travel_log.append({ "country" : country_, "visits" : visit_, "cities" : city_})


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)





# #NOTE: nested dictonary and nested list in dictonary        #mixing dictonaries and lists complex testing
# travel_log = {
#     "France": {"city_visisted": ["Paris", "Lille", "Dijon"], 
#                 "total_visits": 12},
#     "Germany": ["berlin", "Humburg", "stuttgart"],
# }

# print(travel_log["France"]["city_visisted"][1])

# #NOTE: nesting Dictonary in a list

# travel_log = [
#     {"Country": "France", 
#         "city_visisted": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12},
#     {"Country": "Germany",
#         "city_visisted": ["berlin", "Humburg", "stuttgart"]}
# ]

# print(travel_log[0]["city_visisted"][2])




# student_scores = {                      #creats new empty dictonary and assign sam ekey but nre values
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# sudent_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     if student_scores[key] >= 91:
#         sudent_grades[key] = "Outstanding"
#     elif student_scores[key] >= 81:
#         sudent_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] >= 71:
#         sudent_grades[key] = "Acceptable"
#     else:
#         sudent_grades[key] = "Fail"
    

# # 🚨 Don't change the code below 👇
# print(sudent_grades)





