from art import logo
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

# def encrypt(original_text,shift_amount):
#     cipher_text = ""
#     for char in original_text:
#         get_new_index = letters.index(char.lower()) + shift_amount
#         get_new_index %= len(letters)  # 0 - 25 
#         cipher_text += (letters[get_new_index])
#     print(cipher_text)


# def decrypt(cipher_text, shift_amount):
#     original_text = ""
#     for char in cipher_text:
#         shifted_position = letters.index(char.lower())-shift_amount
#         shifted_position %=len(letters)
#         original_text += letters[shifted_position]
#     print(original_text)

print(logo)

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar (original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1 
    for char in original_text:
        if char not in letters:
            cipher_text +=char
        else:
            get_new_index = letters.index(char.lower()) + shift_amount
            get_new_index %= len(letters)  # 0 - 25 
            cipher_text += letters[get_new_index]
    print(f"Here is the {encode_or_decode}, result {cipher_text}")


should_countiue = True

while should_countiue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text,shift_amount=shift, encode_or_decode= direction)
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if user_input =='no':
        print("Good Bye !!! ")
        should_countiue = False


    


