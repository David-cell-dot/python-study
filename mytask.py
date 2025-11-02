#programm
account_type =input("enter account type")
amount=input('enter amount')
if account_type == "standard":
    if amount > 500:
        print("Transaction exceeds limit for standard account")
    else:
        print("Transaction approved")
elif account_type == "premium":
    if amount > 1000:
        print("Transaction exceeds limit for premium account")
    else:
        print("Transaction approved")
else:
    print("Account type entered is neither standard nor premium")