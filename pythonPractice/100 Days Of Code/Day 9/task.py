# name_dict = {
#     "Rahul":"Indore", 
#     "Rohan":"Bhopal", 
#     "Pradeep":"Delhi"
# }

# print(name_dict["Pradeep"])

# # new added 
# name_dict["Ravi"] = "Jasapura"
# print(name_dict)

# empty_dictionary = {}

# print(empty_dictionary)

# name_dict["Pradeep"] = "Berkheda Chouhan"
# print(name_dict)

# # Loop through a dictionary 

# for  key in name_dict:
#     print(key +" : " + name_dict[key])

# # student score code 

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# print(student_scores)

# student_grades = {}

# for key in student_scores:
#     if student_scores[key]>=91 and student_scores[key]<=100:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key]>=81 and student_scores[key]<=90:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key]>=71 and student_scores[key]<=80:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# print(student_grades)

# Nesting Dictionary and list

# capitals = {
#     "France" : "Paris", 
#     "Germany" : "Berlin"
# }

# Nested dict 
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"], 
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print(travel_log["France"][1])

# Nested List 

# nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])



# travel_log = {
#     "France" : {        
#         "Cities_visited" : ["Paris", "Lille", "Dijon"],
#         "total_visits" : 12
#     }, 
#     "Germany":{
#         "Cities_visited" : ["Berlin","Hamburg", "Stuttgart"],
#         "total_visits": 5 
#     },
# }

# print(travel_log["Germany"]["Cities_visited"][2])


# Blind Auction Program 

from hammer_art import logo


def find_highest_bidder(bidding_dictionary):
    highest_bidder = 0 
    highest_bidder_name = ""
    for key in bidding_dictionary:
        bid_amount = bidding_dictionary[key]
        if bid_amount>highest_bidder:
            highest_bidder = bid_amount
            highest_bidder_name = key
        

    print(f"The winner is {highest_bidder_name} with a bid of {highest_bidder}")
    

print(logo)
is_continue = True
auction_dictionary ={}

while is_continue:
    name_input = input("What is your name? : ")
    bid_amount = int(input("What is your bid? : $"))
    auction_dictionary[name_input] = bid_amount
    feedback = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if feedback == 'no':
        is_continue = False
        find_highest_bidder(bidding_dictionary = auction_dictionary)
    elif feedback == 'yes':
        print("\n"*20)




