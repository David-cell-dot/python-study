#using python,Write a program that prompts the user to enter the base and height of a triangle and returns its area.
#calculate the area of triangle= base*height/2
#prompt user for the base and height



Base=float(input("Enter the base of the triangle:"))
Height =float(input("Enter heght of triangle:"))
#validate the input are positivr
if  Height <=0 or Base <=0:
    print(" both height and base are postives:")

#calculate the area using the formula function

Area =( Base*Height*0.5)
#display the result in 2decimal place
print(f"Area of the triangle:{Area} square units")


