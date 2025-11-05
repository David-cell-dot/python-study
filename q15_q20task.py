#calculate the nhif deduction based on  the gross salary
basic = float(input("enter basic saalary:"))
benefits=float(input("enter benefits"))
def gross_salary(basic_salary,benefits):
    return basic_salary  + benefits

    def calculate_nhif(gross):
        if gross <=5999:
            return 150
        elif gross<=7999:
            return 300
        elif gross<=11999:
            return 400
        elif gross<=14999:
            return 500
        elif gross<=19999:
            return 600
        elif gross<=24999:
            return 750
        elif gross<=29999:
            return 850
        elif gross<=34999:
            return 900
        elif gross<=39999:
            return 950
        elif gross<=44999:
            return 1000
        elif gross<=49999:
            return 1100
        elif gross<=59999:
            return 1200
        elif gross<=69999:
            return 1300
        elif gross<=79999:
            return 1400
        elif gross<=89999:
            return 1500
        elif gross<=99999:
            return 1600
        else:
            return 1700
        print(f"gross salary")
        print("Nhif deduction")
        
        #question 16:Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF


#nssf=6% of gross salary,but capped at 1800/- maximum
def calculate_nssf(gross):
    """ nssf=0.06 of gross,maximum at 18000"""
    maximun_gross=18000
    if gross>maximun_gross:
        nssf=0.06*maximun_gross
    else:
        nssf=0.06*gross
        return nssf
    
    #question 17: 
    







