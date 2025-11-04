#Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# Product_list= [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

#list of products__ 
proucts=   ['omo', '30kshs', '300' ,['bread', '45kshs', '359'],['coffee', '5kshs', '79']]

#initialize the total stock
total_stock=0
#loop through each product and add the last element(stock)
for item in proucts:
    stock=int(item[-1]) # convert the last elememt to an integer
    total_stock+=stock
    print( "total stock in the commpany:{total_stock}")
    


 

 
     
 
