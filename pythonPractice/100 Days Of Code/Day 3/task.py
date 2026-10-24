# print("Welcome to the Roller Coaster !!! ")

# height = int(input("What is your height in cm? "))
# bill = 0 
# if height>=120 : 
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age ? "))
#     if age <= 12 : 
#         bill = 5
#         print("Child tickets are $5 ")
#     elif age<=18 : 
#         bill = 7
#         print("Youth tickets ar $7.")
#     elif age>=45 and age<=55:
#         print("Have Safe Journey from our side..")
#     else: 
#         bill = 12 
#         print("Adult tickets ar $12.")

#     wants_photo = input("Do you want to Photo take ? Type Y for Yes and n for No. ")
#     if wants_photo == "y":
#         # Add $3 to the bill 
#         bill += 3 

#     print(f"Your final bill is ${bill}")

# else:
#     print("Sorry you have to grow taller before you can ride.")
#-------------------------------------------------------------------------
# operator 
# > greater than 
# < less than 
# >= greater than equal to 
# <= less than  or equal to 
# == equal to 
# != not equal to 

#syntaxError 
#NameError 

# % --> Modulo Operator  --> Give Remainder after division

# number = int(input("print your number ? "))

# if number%2 == 0: 
#     print("Even")
# else:
#     print("Odd")

# -----------------------------------------------------------------------
# Pizza Delivery 

# print("Welcome to Python Pizza Deliveries !")
# Size = input("What Size Pizza do you want ? S, M Or L : ")
# pepperoni = input("Do you want pepperoni on your pizza ? Y  or N: ")
# extra_cheese = input("Do you want extra cheese ? Y or N: ")

# amount = 0 

# #small - $15, M - 20 , L - 25 
# #pepperoni for small (Y or N) = +$2
# #for medium and large (Y Or N ) = +$3
# # Extra cheese for any size pizza (Y or N) = +$1 

# # How much they need to pay on their size choice 

# if Size == "S":
#     amount += 15
# elif Size == "M":
#     amount += 20 
# elif Size == "L":
#     amount += 25 
# else:
#     print("You typed the wrong inputs.")
# # how much to add to their bill on their pepperoni choice 

# if pepperoni == "Y":
#     if Size == "S":
#         amount +=2
#     else:
#         amount+=3

# # Final Amount based on whether if they want extra cheese 
# if extra_cheese == "Y":
#     amount+=1 
# print(f"Your final bill is :  ${amount}.")
# ---------------------------------------------------------------------------------
# Logical Operator 

# and, or & not 

# -----------------------------------------------------------------------------------------
# Treasure Island



print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______
*******************************************************************************'''
)

# print("Welcome to Treasure Island.\nYour mission is to find the treasure !!")
# input_user = str(input("left or right ?"))
# if input_user == 'Right' or input_user != 'left':
#     print("Fall into a hole.\nGame Over.")
# if input_user =='left':
#     print("swim or wait")

# input_user = str(input("swim or wait"))
# if input_user == "swim" or input_user != "wait":
#     print("Attacked by trout. \nGame Over.")
# if input_user == "wait":
#     print("which door ?")
#---------------created by aniket--------------------------------------
print("Welcome to Treasure Island.\nYour mission is to find the treasure !!")
choice1 = str(input(' You\'re at a crossroad, Where Do you want to go ? left or right ?. ')).lower()


if(choice1 == "left"):
    choice2 = str(input('you\'ve at  come to a lake.' \
    'There is an island in the middel of the lake.' \
    'Type "wait to wait for the boat. '
    'Type "swim" to swim across.')).lower()
    if(choice2 == "wait"):
        choice3 = str(input('You arrive at the island unharmed. '
        'There is house with 3 Doors. One Red, One Blue and One Yellow Which color you would choose ? ')).lower()
        if(choice2=="red"):
            print("Burned By Fire.\nGame Over.")
        elif(choice2== "blue"):
            print("Eaten by beasts.\n Game Over.")
        elif(choice2 == 'yellow'):
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")


#     elif(input_user == 'swim' or input_user != 'swim'):
#         print("Attacked by trout.\nGame Over.")
# elif (input_user != 'left'  or input_user == 'right'):
#     print("Fall into a hole.\nGame Over.")
# -----------------------created by aniket-----------------