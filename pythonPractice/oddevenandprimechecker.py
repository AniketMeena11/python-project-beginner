#Even and odd and prime number checker with python 

flag = True 
primeflag = True
while(flag):
    user_number = int(input("Please put your number, = "))
    print(user_number)
    if(user_number%2 == 1):
        print("This is odd number")
    else:
        print("This is even number")
    for i in range(2, user_number-1):   
        if(user_number%i==0):
            primeflag = False   
    if(primeflag == False):
        print("Prime Number")
    else:
        print("Not Prime Number")
    input2 = str(input("Do you want to check for other, Y OR N = "))
    if(input2.upper() == "N"):
        flag = False


