#Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
#Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

#Use the value from total to get the average and average to find the grade.

#A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

#function to calculate total marks
# average= total/5
from faulthandler import cancel_dump_traceback_later


def calculate_total (maths,eng,swa,sci,sos):
    total=maths,eng,swa,sci,sos
    return total




#to determine the average marks using function
def calculate_average(total):
    average=total/5
    return average
#function to determine the average based on grade
def determine_grade(average):
    if average>=79:
        return "A"
    if average <=79: 
        return "B"
    if average <=59:
        return "C"
    if average <=49:
        return "D"
    else:
        return "E"
    #main program
    def main():
        print(" enter marks of each subject out of 100:")
        maths=int(input('maths:'))
        eng=int(input("eng:"))
        swa=int(input("swa:"))
        sci=int(input("sci:"))
        sos=int(input("sos:"))
        total=calculate_total(maths,eng,swa,sci,sos)
        average=calculate_average(total)
        grade=determine_grade(average)
        
        print("total marks")
        print("average marks")
        print("grades")
        

       
 
 

    
    
    
    
    
    

    
