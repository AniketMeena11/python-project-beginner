
flag = True
def add(first_int, second_int):
    print(first_int + second_int)

def multiply(first_int, second_int):
    print(first_int * second_int)

def subtract(first_int, second_int):
    print(first_int - second_int)

def division(first_int, second_int):
    print(first_int / second_int)

while flag:

    print("Please provide your input")

    try:
        first_int = int(input("provide your first int = "))
        second_int = int(input("provide your second int = "))
        
    except ValueError as e:
        
        print(f"Provide Integer input only, {e}")
        continue

    print("Which Operation you want to perform +, -,*, / ")

    user_input = input("Provide operation = ")

   
    if user_input not in ["+", "-", "*","/"]:
        print(f"Please select right input, you selected wrong input ,{user_input}" )
        continue


    elif user_input == "+":
        add(first_int=first_int, second_int=second_int)
    
    elif user_input == "-":
        subtract(
            first_int=first_int,
            second_int=second_int
        )

    elif user_input == "*":
        multiply(
            first_int=first_int,
            second_int=second_int
        )


    elif user_input == "/":   

        try:
            division(first_int=first_int, second_int=second_int)
        except ZeroDivisionError as e :
            print(f"Don't User Zero for divide {e}")
            
    
    
  
    
    print("Do you want to perfrom more operations select Y or N = ")
    
    operator = input()

    if operator.lower() == "n":
        flag = False 

    














