# print(type("Hello"))

# print(type(3.1345))

# print(type(12334))
# print(type(False))

# print(type(bool(123)))

# int()
# float()
# bool()
# str()

# name = input("Enter your name")
# length = len(name)
# print(type("Number of letters in your name : "))
# print(type(length))
# print("Number of letters in your name : "+name+ " "+ str(length))


# print("My age : " + str(23))

# print(123+345)
# print(7-3)
# print(3*2)
# print(6/3)
# print(type(6/3))
# print(6//2)
# print(type(6//2))

# print(3**2)

# #PEMDAS

# bmi = 84/ (1.65**2)
# print(bmi)

# print(round(bmi,2))

# score = 0 
# score +=1 
# print(score)

# score = 0 
# height = 5.6
# is_winning = True

# print(f"Your score is = {score}, Your height is {height}. Your Wining is {is_winning}")


print("Welcome to the tip Calculator!")
bill_price = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
total_pay = (bill_price+((bill_price*tip)/100))/people
print(f"Each person should pay: ${round(total_pay,2)}")