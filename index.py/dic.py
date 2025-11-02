#dictionary= a collection of key {key:value} pair


capitals ={"USA" :"WASHINGTON D.C" ,
           "INDIA" :"NEW DELHI", 
           "CHINA" :"BEIJING" ,
           "RUSSIA" :"MOSCOE"}
#print(dir(capitals))
#print(help(capitals))
print(capitals.get("INDIA"))
print(capitals.get("japan"))

if capitals.get("japan"):
    print("That capital exists")
else:
    print("that capital doesnt exist")

    #Capitals.update({"USA":"Detroit"})
    #capitals.pop("CHINA")
    
    keys=capitals.keys()
    print(keys)
    for key in capitals.keys():
        print(key)
        value=capitals.value()
        for value in capitals.values():
            print(value)





