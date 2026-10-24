import random
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit+" pie")
# print(fruits)    

student_score = [100, 150, 199, 171,69, 40, 65]

# total = sum(student_score)
# print(total)

# total = 0 
# for number in student_score:
#     total = total + number
# print(total)

# max_number = max(student_score)
# print(max_number)

# max_number = 0

# for number in student_score:
#     if number > max_number:
#         max_number = number

# print(max_number)

# Range Function 

# for num in range(1,11,3):
#     print(num)

# total = 0 
# for num in range(1,101):
#     total = total + num
# print(total)

# number = 1 
# print(number%3==0)

# num = [1,2,3,4,5,6,7,9,10,15]

# for number in range (1,101):
#     if(number%3==0 and number%5==0):
#         print("FizzBuzz")
#     elif(number%3==0):  
#         print("Fizz")
#     elif(number%5==0):
#         print("Buzz")  
#     else:
#         print(number)


numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '/', '?']
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Easy Level (abZ23#%)--> letters, number, symbol order wise

password = ""

for i in range (0,nr_letters):
    random_keyword = random.choice(letters)
    password +=random_keyword

for i in range (0,nr_symbols):
    random_symbols = random.choice(symbols)
    password += random_symbols

for i in range (0,nr_numbers):
    random_number = random.choice(numbers)
    password += random_number



print("Your Password :"+password)


# Hard Level

password_list= []
password_hard_level = ""

for i in range (0,nr_letters):
    random_keyword = random.choice(letters)
    password_list.append(random_keyword)

for i in range (0,nr_symbols):
    random_symbols = random.choice(symbols)
    password_list.append(random_symbols)

for i in range (0,nr_numbers):
    random_number = random.choice(numbers)
    password_list.append(random_number)


# reshuffling 
# print(f"Your Password_list :{password_list}")
random.shuffle(password_list)

for char in password_list:
    password_hard_level+= char



# print(f"Your Password_list :{password_list}")
print(f"Your Password_hard_level :{password_hard_level}")





    
        



