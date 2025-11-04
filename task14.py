#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs
def get_number(prompt):
    try:
        value=float(input(prompt))
        return value
    except ValueError:
        print("invalid character entered.insert valid character")
        
        
#main program
num1=get_number("enter the first number:")
num2=get_number("enter  the second number:")

#concatenate
result=num1 
result=num2
print (  "the {num1} and sum of {num1} ia {result}")