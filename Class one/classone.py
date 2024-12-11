# //Python is a popular programming language

# // Python can be used on a server to create web applications (Django, Flask ), GUI(tkinker) , 
# DataScience(numpy,Pandas ) , AL(ML, DL ) ,  Moblie Apllication , Window Application ,system scripting, 
# software development,mathematics, system scripting.

#Python is a high-level, interpreted, object-oriented programming language that is
#used to build websites, software, and more more more .....

# Python Install op-system  (Window system)
# https://www.python.org/

#IDE (Integrated Development Environment) 
# pycham
# vscode
# Example  Hello world 
# print("Hello world") 
# DataType 
#  Text Type:	     1) String    "" 
# NumericTypes:	     2) int, float, complex
# Sequence Types:    3) list, tuple, range (numpy)
# Mapping Type:	     4) dict (numpy)
# Set Types:	     5) set
# Boolean Type:	     6) bool

#Topic One 
#Variables 
#example one 
#TextData = "Hello world" #example string
#TextDataInt = 321 #example init 
#example two
#avg = 3.14 # example float
#example three 
#realNum = complex(2,5j)

#Topic Two

# TypeCasting  
# x = str(3.5) 
# print(type(x))  #type function re-built 

#Topic Three 
# List  # collection of strings,Lists are used to store multiple items in a single variable.
# Ex : mylistHasssan = ["apple", "banana", "cherry"]

# 1): Method : AccessItems
#ex : MyList = ["Hello" , "World"]
#print(MyList[1]) 


# 2) Method : ChangeItems
#ex : MyList = ["Hello" , "World"]
# MyList[1]= "Hassan" 
# print(MyList)


# 3) Method : Remove 
# ex : MyList = ["Hello" , "World"]
# MyList.remove("Hello")
# print(MyList) 

# 4) Method : LoopLists
#thisList = ["apple", "banana", "cherry"]
#for i in thisList:
#    print(i)

# 5) Method : ListComprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  #simple list to store the item 
newlist = []

for i in fruits:
    if "a" in i:
        newlist.append(i)
        
print(newlist)