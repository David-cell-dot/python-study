#dictionary
d={110:"xyz", 110:"abc" ,105:"bcd" , 109:"bcd"}
print(d)
d={}
d["laptop"]=40000
d["mobile"]=1500
d["earphones"]=1000
print(d)
print(d["mobile"])
print(d.get(110))
print(d.get(110))
d[110]="wxy"
print(d)
#revision 2
d={1: 'Geeks', 2: 'For', 3: 'Geeks'}
#creat
# 
# e a dictionary using dic constructor()
d2=dict(a="Geeks", b="for",c="geeks")
print(d2)
#accessing dictionary items
d={ "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }
#accessing using key
print(d["name"])
print(d)
#using get method
print(d.get("name"))
#adding and updating dictionary
d={1: 'Geeks', 2: 'For', 3: 'Geeks'}
#adding anew value-pair
d["age"]=22
#updating an existing value
d[1]="Python Dic"
print(d)
#removing dictionary items
d={1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}
#delete to remove an item
del d["age"]
print(d)
del d[1]
print(d)
#pop
val=d.pop(3)
print(val)
#pop item
key,val=d.popitem()
print(f"key:{key} ,value:{val}")
#clear
d.clear()
print(d)
#iterating  thriough a dictinary
d = {1: 'Geeks', 2: 'For', 'age':22}
#iterate over keys
for key in d:
    print(key)
# iterate over values
for value in d.values():
    print(value)
    # iterateusing key-value method 
for key,value in d.items():
 print(f"{key}:{value}")
