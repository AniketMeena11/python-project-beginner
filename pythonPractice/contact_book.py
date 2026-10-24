
# Contact book replication in this file 

print("""
Select the Action which you want to perfrom in the contact book !!!
1. Add Contact 
2. View All
3. Search 
4. Remove
5. Exit

""")


user_input = int(input())

if(user_input>1 and user_input<5):
    print(f"You select the following option {user_input}")
else:
    print("Range of User Input lies b/w 1 to 5 only !!!")