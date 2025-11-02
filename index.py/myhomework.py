#1.single line string
letter ="p"
print(letter)
print(len(letter))

greeting = "Hello, world"
print(greeting)
print(len(greeting))

sentence =" i hope you enjoyed 30 days of python programming"
print(sentence)
print(len(sentence))

#2.multiline-strin

multiline_string ="""I am a teacher and enjoy teaching.
I did"nt find anything rewarding as empowering people.
That is why i created 30 days of python."""
print(multiline_string)

#string_concatenation
first_name ="Asabeneh"
last_name ="Yetayeh"
space=  "@"
full_name =first_name + last_name
print(full_name) # Asabeneh Yetayeh
print(len(first_name))
print(len(last_name))
print(len(first_name)) > len(last_name) # True
print(len(full_name)) 

###unpacking characters
language = "python"
a,b,c,d,e,f =language # unpacking sequence
print(a) # p
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

name = "Dad"
a,b,c = language # unpacking sequence characters into variables
print(a) # D
print(b) # a
print(c) # d
#join
Web_tech = ["HTML" , "CSS" ,"JAVA"]
result  = "#," .join(Web_tech)
print(result)