#Write a program that prompts the user to enter the base and height of a triangle and returns its area.


height=float(input("enter height"))
base=float(input('enter base area'))
Area=base*height*0.5

def area_triangle(base,height):
    return 0.5*base*height
area= base*height*0.5
print(area)


#Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
# Hint: how does an even / odd number react differently when divided by 2?
    
numb1=float(input("enter the num1"))
numb2=float(input("enter the numb2"))
if numb1%2==0:
    print("even number")
else:
    print("odd numbers")
    