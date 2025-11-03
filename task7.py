#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

#marks from input user

marks=float(input("enter student marks(1-100)"))
if marks >=79:
    print("grde=A")  
elif marks >=60:
    print("grade B")
elif marks>=49:
    print("grade C")  
elif marks>=40:
    print("grdae D")
else:
    print("grade E")
    
