#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
#get user inputs
vars1=float(input("enter the first number:"))
vars2=float(input("enter the second number:"))
vars3=float(input("enter the third number:"))

#compare to get the larges
if vars1>=vars2 and vars1>=vars3:
     print("vars2 is the largest")
elif   vars2>=vars1 and vars2>=vars3:
    print("vars2 is the largest")
else:
    print("vars3 is the largest")
