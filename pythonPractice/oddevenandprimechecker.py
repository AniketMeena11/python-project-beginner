#Even and odd and prime number checker with python 

flag = True 
while(flag):
    
    primeflag = False
    try:
        user_number = int(input("Please put your number, = "))
        
    except ValueError:
        print("Please only put numeric value")
        continue
    
    if(user_number>=2):
        print(user_number)
        if(user_number%2 == 1):
            print("This is odd number")
        else:
            print("This is even number")
        for i in range(2, user_number-1):   
            if(user_number%i==0):
                primeflag = True  
        if(primeflag == True):
            print("Not Prime Number")
        else:
            print("Prime Number")
        input2 = str(input("Do you want to check for other, Y OR N = "))
        if(input2.upper() == "N"):
            flag = False
    elif(user_number==1):
        print("This Odd Number and Not Prime Number")
    elif(user_number<=0):
        print("Numeric should be start from 1 and not less than zero")
        continue


