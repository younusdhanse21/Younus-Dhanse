
#datatypes 
#how to take input from the USER?

user_input=input("enter a number:")
print(user_input + 5)

user_input1 = int(input("enter a number:"))
print(user_input1)
print(user_input1 + 4)

#what are datatypes?
#data tpyes in python are categories of values 
#that tell python how to store and use them

# some of common data types!
#1) basic types 

#int--> whole number:10,-5
#float--> decimals: 3.14,-0.5
#str--> text :"hello"
#bool--> True or False 
#nonetype--> none(represents "no values")

#2) collection types 

#list--> ordered, changeble:[1,2,3]
#tuple--> oredered, unchangeble:(1,2,3)
#set--> unordered, unique(no duplicates):{1,2,3}
#dict--> key value pairs :{"name":"ravi", "age":20}


#operators
#types of operators 

#1) Arithmetic operators
#print(9*4)##--> 36
#print(9+4)##--> 13
#print(9-4)##--> 5
#print(9/4)##--> 2.25
# % ##--> modulus operator
#print(9%4)##--> 1(REMAINDER value)
# // ##--> floor Division 
#print(9//4)##--> 2


#2) comparison operators (==,<,>,>=,<=,!=)


# var = 5 --> assignmenet
# LHS==RHS --> comaprison

# example
# calculate if the candidati is eligible tp vote 

age_of_candidate=int(input("enter your age:"))

if age_of_candidate>18:
    print("congrats you are eligible to vote!!")
elif age_of_candidate==18:
    print("great! you are eligible from this year to vote!!")
else:
    print("sorry! you are not eligilble to vote ")
     
## control flow statement
# condition : if/elif/else 
# example given above

# assignment operator [+=,-=,**=,//=,/=]

a=5
b=10

a+=2
print(a)

b-=3
print(b)

# membership operators 
# operator ---------> meaning
# in       ---------> true if value is present
# not in   ---------> true if the value is not present

#a] list example:
numbers = [1,3,5,7]
print(3 in numbers)
print(10 in numbers)
print(10 not in numbers)

#b] string 

text="python programing"
print("python" in text)
print("java" in text)
print("gram" in text)

#c] tuple




#d] set 
vowels={"A","E","I","O","U"}
print('A' in vowels)

#e] dictionary 




## identity operators checks whether two variable refer 
#to same in memory operator

# is ----> true if refers to same object 
# is not ------> true if refers to different object

a = 10
b = 10
 
print(a is b)
print(a==b)


x = [1,2,3]
y = [1,2,3]

print(x is y)# false because different objects
print(x == y)# true because same value 


# is not example 

a1 = "Hello"
b1 = "Hello"

print(a1 is not b1)# both objects are same hence not value gives false respone
print(a1 is b1)
print(a1 == b1)

# bitwise operators work on the binary (bit) representation of itegers 

# operators symbol 
 
# &AND
# |OR
# ^XOR 
# ~NOT 
# << left shift 
# >> right shift 

a = 1 # --> 1
bin(a) # ---> conversion to binary number 
a = 6
bin(6) # 110 -----> '0b110'
b = 3 # 011 ------> '0b11'
bin(3)
print(a & b) # 2 ----> 010
print(bin(a),bin(b))

print(a/b)
print(a^b)
print(~a)
print(a<<1)
print(a>>1)
