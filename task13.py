#Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked
correct_password='admin@123'
correct_email="admin@gmail.com"
#no.of attempts allowed
max_attempt=4
attempt=0

while attempt<max_attempt:
    email=input("enter your email:")
    password=input('enter your password')
    
    if email==correct_email and password==correct_password:
        print('log in successful')
        break
    else:
        attempt+=1
        remaining=max_attempt-attempt
        print("invalid userword or invalid password")
        if remaining>0:
            print("you have{remaining}attempts left")
        else:
            print("you have been blocked")
    