# randomisation and python Lists

import random
# import my_module
# print(my_module.my_fvt_number)
#Random Integer
# random_integer = random.randint(a=1,b=10)
# print(random_integer)

# Random Floating point Number

# random_0_to_1 = random.random() 
# print(random_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float) 

# heads and tails program


# random_heads_or_tails = random.randint(0,1)
# # print(random_integer)
# if random_heads_or_tails==0:
#     print("Heads")
# else:
#     print("Tails")

# states_of_america = ["Delaware","Pennsylvania","Washington", "California"]
# print(states_of_america[0])

# fruits = ["Cherry", "Apple", "Pear"]

# fruits[1] = "Orange"
# print(fruits)

# fruits.append("Banana")
# fruits.extend(["papaya","Mango"])
# print(fruits)

# Who will pay the bills ? 

# friends = ["Monu", "Sunil", "Pradeep", "Shivendra", "Aniket", "Ravi"]

# # using choice
# random_name = random.choice(friends)
# print(random_name)

# # print(len(friends))
# #using randint
# random_index = random.randint(0,len(friends)-1)
# print(friends[random_index])

#Nested List 

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])

# print(dirty_dozen)
# print(dirty_dozen[0])
# print(dirty_dozen[1])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])

# -------------------------------Developed by aniket ------
# Rock Paper and Scissors 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

#paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
# Scissors

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# -------- Logic Implement by aniket ----

# sign_list = [rock, paper, scissors]

# user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# if(user_input==0):
#     print(rock)
# elif(user_input==1):
#     print(paper)
# else:
#     print(scissors)

# random_sign_index = random.randint(0,len(sign_list)-1)
# print("Computer chose: \n")
# print(sign_list[random_sign_index])

# #0 rock , 1 paper, 2 scissors
# if(user_input==0):
#     if(random_sign_index==0):
#         print("Draw")
#     elif(random_sign_index==1):
#         print("You lose")
#     else:
#         print("You Win")

# if(user_input==1):
#     if(random_sign_index==0):
#         print("You Win")
#     elif(random_sign_index==1):
#         print("Draw")
#     else:
#         print("You lose")

# if(user_input==2):
#     if(random_sign_index==0):
#         print("You lose")
#     elif(random_sign_index==1):
#         print("You win")
#     else:
#         print("Draw")


# --------------------------------Developed by aniket----------------

image_list = [rock,paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#0,1,2

if user_choice>=0 and user_choice<3:
    print(image_list[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose :")
print(image_list[computer_choice])

if user_choice>=3 or user_choice<0:
    print("You typed an invalid number. You lose!")
elif user_choice==0 and computer_choice == 2:
    print("You Wins !!")
elif computer_choice==0 and user_choice ==2 :
    print("You lose !!")
elif computer_choice>user_choice:
    print("You lose !!")
elif user_choice> computer_choice:
    print("You Win !! ")
elif computer_choice == user_choice:
    print("It's a draw !")
