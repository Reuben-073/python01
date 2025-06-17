# correct_password="reub123"
# entered_password=""
# while entered_password!=correct_password:
#     entered_password=input("enter correct password: py")
#     #the in
# print("access_granted")

correct_password="reub123"
entered_password=""

initial_attempts=0
maximum_attempts=6
while initial_attempts < maximum_attempts: 
    entered_password=input("enter password:")
    if entered_password==correct_password:
        print("access granted")
        break
    else:  
        initial_attempts+=1
        print(f"incorrect password. {maximum_attempts-initial_attempts} attempts remaining.")
if initial_attempts==maximum_attempts:
    print("locked")
