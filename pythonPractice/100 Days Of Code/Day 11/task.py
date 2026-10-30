# #Capstone Project BlackJack 
# import random
# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# user_card_list = []
# computer_card_list = []
# current_score = 0
# user_counter = 2 
# computer_counter = 1


# for i in range(user_counter):
#     user_card_list.append(random.choice(cards))

# print(f"Your cards: {user_card_list}, current score: {sum(user_card_list)}")
# computer_card_list.append(random.choice(cards))
# print(f"Computer's first card : {computer_card_list}")
# user_input = input("Type 'y' to get another card, type 'n' to pass: ").lower()

# user_continue = True
# while user_continue:
#     if user_input == 'y':
#         user_card_list.append(random.choice(cards))
#         while 11 in user_card_list and sum(user_card_list)>21:
#             index = user_card_list.index(11)
#             user_card_list[index] = 1    
#         if sum(user_card_list)>=21:
#             print(f"Your cards: {user_card_list}, current score: {sum(user_card_list)}")
#             user_continue = False
#             print(f"Your final hand: {user_card_list}, final score: {sum(user_card_list)} ")
#             print("You Lose !!! ")
#         elif user_input=='n':
#             print(f"Your cards: {user_card_list}, current score: {sum(user_card_list)}")
#             user_continue = False
#             print(f"Your final hand: {user_card_list}, final score: {sum(user_card_list)} ")
            
        
#     if user_input == 'n':
#         computer_card_list.append(random.choice(cards))
#         while 11 in computer_card_list and sum(user_card_list)>21:
#                 index = computer_card_list.index(11)
#                 computer_card_list[index] = 1 
#         if sum(computer_card_list)>sum(user_card_list):
#             user_continue = False
#             print(f"Your final hand: {user_card_list}, final score: {sum(user_card_list)} ")
#             print(f"Computer's final hand: {computer_card_list}, final score: {sum(computer_card_list)}")
#             print("You Lose")
#         elif sum(computer_card_list)>=21:
#             user_continue = False
#             print(f"Your final hand: {user_card_list}, final score: {sum(user_card_list)} ")
#             print(f"Computer's final hand: {computer_card_list}, final score: {sum(computer_card_list)}")
#             print("You Win")

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

# make a list of 1 to 10 

# List_10 = []
# for i  in range (1,11):
#     List_10.append(i)
# result = []

# for i in range(0,len(List_10),2):
#     first_num = List_10[i]
#     second_num = List_10[i+1]
#     result.append((first_num, second_num))
# print(result)

name = "aniket"

namelist = []

for char in name:
    namelist.append(char)

print(namelist)
newlist = []
for i in range(0,len(namelist)-1,2):
    firstchar = namelist[i]
    secondchar = namelist[i+1]
    newlist.append((firstchar,secondchar))

print(newlist)
    











            







