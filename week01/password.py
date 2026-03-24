correct_password = "ABCDEFGH"
x= 0
while x<3:
    input_password = input("What is your password?")
    x = x+ 1
    if input_password == correct_password:
        print("Access granted")
        break
    elif input_password != correct_password and x<3:
        print("Try again")  
    else:
        print("Locked Out")



    
