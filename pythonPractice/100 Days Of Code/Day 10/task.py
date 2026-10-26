# # Day 10 

# # Format  Name 

# def format_name(f_name, l_name):
#     """This Function used to format name and return the Title based name"""
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return (f"{formated_f_name} {formated_l_name}")



# output = format_name(f_name="aniket", l_name= "meEnA")

# print(output)

# print(len("Aniket"))


# def is_leap_year(year):
#     """This function used to check leap year"""
#     if year%4==0:
#         if year%100==0: 
#             if year%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# print(is_leap_year(1989))



# # Docstrings is like a comment of the information about the any function and all 

# Calculator project 

import art




def add(n1, n2):
    return n1+ n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

# 

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply, 
    "/" : multiply
}

# print(operations["*"](4,8))

def calculator():
    print(art.logo)
    first_num = float(input("What's the first number?:  "))

    is_continue = True

    while is_continue:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation:  ")
        second_num = float(input("What's the next number?:  "))
        carry_forward = 0  
        carry_forward = operations[operator](first_num,second_num)
        print(f"{first_num}{operator}{second_num} = {carry_forward}")
        user_input = input(f"Type 'y' to continue calculation with {carry_forward}, or type 'n' to start a new calculation : ").lower()
        if user_input == 'y':
            first_num = carry_forward
        else:
            is_continue = False
            print("\n"*20)
            calculator()


calculator()






    




