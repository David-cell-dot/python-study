#Using python,Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. Hint: Check if it contains an “@” symbol and “.” symbol. Once you learn functions,revisit this and write this code inside a function.
#validation of email from the user
email=input('enter email your email:')
if " @" and " ." in email:
    print("valid email address")
else:
    print("invalid email")