'''
Identity Operators --> checks the identity of an object -->id()
a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print(a==c)

a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))

#AS we have lists(Mutable Collection) both c and a lists will have different
#ida whereas values are same
print(c is a)#output False
print(c==a)#output True
print(a is not c) 

#Bitwise Operators --> we perform bitwise operations over operands
#& (and) ,| (or) , ^(XOR) , Shifting operators(<<,>>)
#NUmber will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5|3) #bitwise OR

print(5^3) #bitwise XOR

print(5 and 3)# output 3 , here logical opertaor checks for both existances

print(5 or 3) # output 5 , here logical operator

#LeftShift operator << , Right SHift operator >>

print(5 < 1)#False Comparsion
print(5<<1) #left shift operator
print(5>>1)#right shift operator

print(15<<2)#convert 15 to binary and perform 2 times left shifting

print(15>>2) #convert 15 to binary and perform 2 times right shifting

#input Formatting --> input(),int(input()),float(input())
#You know -->single input
#2 or 3 inputs --> map()
# group of integers -->list(map(int,input().split(',')

names=input("Enter the Names:").split(',')
print(names)

name1,name2 = map(str,input("Enter the Freinds Nammes:"))
print(name1,name2)

#Tokens -->Numeric Datatypes -->Operators---> Flow of the program
#Control Block Statements --> they control the flow of the program
#Conditional Statements
#repetition Statements

#Conditional Statements --> if usage

syntax :
    if <condition>:
        statement(s)..
        ............
  
#age=15
age=int(input("Enter the age:"))
if age > 18:
        print("your age is:",age)


age=int(input("Enter the age:"))
if age>=18 and age in [19,20,22]:
        print("your age is:",age)
        print(age)
 
#else keyword --> if-else

else:
    statement(s)..
    if-else usage as below:
        if<condition>:
            statement(s)...
            .....
     else:
         statement (s).....
         ....
'''

#vote Eligiblity ->To check his/her voter eligibility and give access..

age=int(input("Enter the age:"))
if age>=18:
    print("you have voter eligibility",age)
    print("Access Granted")
else:
    age=18-age
    print("you have to wait for more ",age,"years")

#same case lets use only nested --> if,else


'''
task: student marks and grade analyzer
90-100 --->'A'
80-89----->'B'
70-79 ---->'C'
60-69---->'D'
>60 -->fail
#also -ve cases should not be allowed and marks should not greater 100























    
         
