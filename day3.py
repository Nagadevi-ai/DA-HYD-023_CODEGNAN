''''
#Numeric datatype -->int,float,complex along with boolean

#Input formatting -->Accepting input from the user --> input()

#Accepting integer input from user
#by default input() accepts any input --> str
#int(input()) -->will accept only integers
age=int(input('Enter the age:'))
print(age)
print(type(age))

#float(input() -->accepts integers,float values
age=float(input('Enter the age:'))
print(age)
print(type(age))
#str(input() -->accepts string
name=input("Enter the name:")
print(name)
print(type(name))


#Accept group of values

a=input().split() #by default split() has space
print(a)

a=input().split() #now you enter spaces in output
print(a)

#comma separted values
a=input("enter the values:").split(',')
print(a)


#List of integers
marks=list(map(int,input("enter the values:").split(',')))
print(marks)


#Now we want to accept 2 values from user
age,salary = map(int,input("enter the values:").split(','))
print(age)
print(salary)

#Single input --->int(input())
#two inputs -->a,b=map(int,input().split(','))
#any number result as list -->a=list(map(int,input().split(',')))


#float of integers
marks=list(map(float,input("Enter the values:").split())
print(marks)
           
#group of float values
age,salary = map(float,input("enter the values:").split(','))
print(age)
print(salary)

#Accepting input from user --> int,float -->input formtaing

#operators --> operators perform operations between values (operands)
#7 types -->Arithmetic,Assignment,Comparsion(relationship)
#membership,Identity,Logical,Bitwise

#Arithemetic Operators --> Arithmetic operations
# +,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3) #Float Value
print(5//3)#Floor division
print(5%3) #modlus
print(5**3)#Exponential

length=3
breadth=2
area=length*breadth
print(area)

length,breadth =map(int,input("Enter the values:").split(','))
area=length*breadth
print(area)

#Assignment operators -->assign the values
#=,+=,-=
a=45
print(a)
#update the value of a
a=a + 5 #a+=5
print(a)
b=35
b+=a #b=b+a
b-=5 #b=b-5
print(b)
c=22
c-=5
print(c)

#Task : *=,/=,//=,%=,**= workout

#comparsion operators -->we compare the values -->boolean
# ==(equal to), !=(not equal to),<(less than),>(greater than)
#<=(less than or equal to)>=(greater tha or equal to)

age = 25
print(age==25)
print(age != 25)
print(age<25)
print(age<=25)
print(age>35)
print(age>=35)
print(-5<-1)

#Membership Operator -->in,not in --->boolean
#it checks for the existance of an object in a collection

marks = [22,23,26,27,28]
print(22 in marks)
print(25 not in marks)
#print(35 in 355) #TypeError

print('code' in 'codegnan')
print('$ in abcd$)

#Logical Operators -->logical decision making -->and,or,not
#and ---> all conditions to be satisfied
#or ---> any one condition to be satisfied

a=(25 in[25,35,38]) and 45<56
print(a)
b=45>56 or 25<=45
print(b)
c=not(True)
print(c)
'''
#Identity operators ---> check for identity of an object -->id()
#is  is not
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)

a=[1,3,5,4]
print(id(a))
c=a
print(id(c))
print(c is a)
