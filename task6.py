# using pythonWrite a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked
# the correct password and validate not more than 4 times
correct_password="admin@123"

# no.of attempts
minimum_attempt=0
maximum_attempts=4
if minimum_attempt<maximum_attempts:
   password=input("enter your password")
if password==correct_password:
    print("access granted")
elif maximum_attempts>4 and minimum_attempt>0:
    print("password is incorrect")
else:
    print("account blocked")
    