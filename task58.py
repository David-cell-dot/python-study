# # 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
#  If start_date comes before end_date, print "Valid period",
#  If start_date is after end_date, print "Invalid period".
#  If both dates are the same, print "One-day period".


#question 1
start_date ="2024-01-01"
end_date= "2024-12-31"
# in comparison
if start_date < end_date:
    print("valid period")
elif start_date > end_date:
    print("invalid period")
else:
    print("one day period")
    
#  #2.Given two strings str1 and str2, write a conditional statement that checks:
# If str1 is longer than str2, print "str1 is longer".
# If str2 is longer than str1, print "str2 is longer".
# If both have equal length, print "Both are of equal length"

str1=0
str2=0
#str1==str2
if str1>str2:
    print("str1 is longer")
elif str2 > str1:
    print("str2 is longer")
else:
    print("both are of equal length")
    
       #3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
valid_id=[101,102,103]
user_id=105
if user_id  in valid_id:
    print("Access granted")
elif user_id not in valid_id:
 print('Access denied')
 
 #.Given a variable value that could be of any type, write a conditional statement that:
#Prints "String Detected" if value is a string.
#Prints "Integer Detected" if value is an integer.
#Prints "Unknown Type" for any other type.

value=("string","integer")
#value may be a string or an integer.
if isinstance  (value,str):
   print("value is detected")
elif isinstance(value,int):
     print("Integer is detected")
else:
     print("unkwon type")
     #.Given x = 7 and y = 14, write nested conditional statements that print:
#"x and y are both even" if both x and y are even numbers.
#"Only y is even" if only y is even.
#"Neither x nor y are even" if both are odd.
x=7
y=14
# both x anf y are even numbers
if x%2==0:# x is an even number
    if y%2==0:# y is an even number
        print("x and y is both even")
    else:
        print("only y is even")
else:
         print("neither x nor y are even numbers")