#Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
 #if a user enters “0712345678”, the program should display “+254712345678”
#if a user enters “0112345678”, the program should display “+254112345678”
# if a user enters “712345678”, the program should display “+254712345678”

from unittest import result


def format_phone_number(phone):
    phone=phone.strip().replace(",")
    if phone.startwith("+254"):
        return phone
    elif phone.startswith("254"):
         return "+" +phone
    elif phone.stsrtswith("07"):
        return "+254" + phone[1:]#replace 0 with +254
    elif phone.startswith("01"):
        return "+254" + phone[1:]#Replce 0 with+254
    elif phone.startswith("7") or phone. startswith("1"):
        return "+254" + phone
    else:
        return"invalid phone number format"
    
    user_input=input("enter your number:")
    result=format_phone_number("user_input")
    print("formatted number:", results)
    
    

    
    
    