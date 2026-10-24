# def greet():
#     print("Hello")
#     print("How do you do ? ")
#     print("Isn't the weather nice?")

# greet()

# # functions that allows for inputs 

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")

# greet_with_name("Aniket")

# functions with more that 1 input
"""def greet_with(name, location):
    print(f"Hi I am {name}")
    print(f"I am from {location}")

greet_with(location="Bhopal", name = "Ravi") # Keyword Arguments 
greet_with("Rohan", "Indore")  """

# Love calculator 
# counter_true = 0
# counter_love = 0 
# name1 = 'Angela Yu'
# name2 = "Jack Bauer"
# single_name = name1+name2
# true_list = list("TRUE".lower())
# love_list = list("LOVE".lower())
# for char in single_name :
#     if char in true_list:
#         counter_true +=1
#     if char in love_list:
#         counter_love+=1
# print(str(counter_true)+str(counter_love))

# cesar cypher 

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(original_text,shift_amount):
    encode_letter = ""
    for char in original_text:
        get_index = letters.index(char.lower())
        get_new_index = shift_amount+get_index  
        encode_letter = encode_letter + (letters[get_new_index])
    print(encode_letter)


encrypt("Z",1)


