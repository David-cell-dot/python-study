#.strip-removes white spaces from a string on both side
a = "   hello world"
print(a.strip())
#.lstrip-removes""" from left
a ="Hello world   "
print(a.lstrip())
# formating
first_name =" david"
second_name ="wafula" 
print(f"this is a statement from{first_name} {second_name}")
#.rstrip()-removes whitespaces from right side
s="Hello python!    "
res = s.rstrip()
print(res)
#title-capitalise each word in a string
text =" welcome home"
x = text.title()
print(x)
#index-finds the index of the fisrt instances of  specified character,if no value is found,throws an error
s = "Python programming"
p =s.index("prog")
print(p)
#find()-find the index of the first instance of a specified character,if no value,returns -1
text ="Hello,welcome to my world"
x =text.find("welcom")
print (x)
#count-gives the no of occurences of a specified character 
text =" hello, hello, my name is wanjiku"
x =text.count("hello")
print(x)
#endswith()-checks wether a string ends with a specified character
s ="geeks for geeks"
x =text.endswith("geeks")
print(x)
#startswith()-checks wether a string has starts with specified character,returns true if he specified character stats with prefix
s ="geeks for geeks"
x = s.startswith("for")
print(x)
#isupper()-checks wether strings are uppercase format
#islower()-"                         lowercase format"
text =" MWALIMU"
x = text.islower()
print(x)
x =text.isupper()
print(x)
#split-splits a strin into substrings using  a specified character
string ="one.two,three"
words = string.split(",")
print(words)
words =string.split(":")
print(words)
#formatting the format specify the value and place anf insert them inside the string place holder
s ="welcome to ()"

#join-concatanates the string representation of the elementsin a sequence into a string,with  separator sring
x =["Hello", "world", "from", "python"]
res = " ".join(a)
print(res)