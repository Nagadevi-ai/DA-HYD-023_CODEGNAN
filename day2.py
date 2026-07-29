'''
Tokens --> Variable ,Punctuators

Variables --> Named memory location, its a placeholder for data
#Rules are to be followed
'''
#MultiAssignment of Variables

name,age,place ='Codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='-')
print(name,age,place,sep='--->')

#a,b=2,3,4 #ValueError as too many values to unpack
#Reassigning variables

name="Codegnan"
a,b = 45,1.5
print(a,b)
a,b = b,a
print(a,b,sep=',')

#a,b = b,c#NameError as c is not defined
print(a,b)

#Deleting the variable -->del
#del a
#print(a)
#del a,b
#print(a,b)

#punctuators -->[](Lists),{}(Dicts,Sets),()(tuples)
name = "Codegnan";age=7;Course='Data Analysis'
print(name,age,Course,sep=',')

#Datatypes --> Numeric (int,float,complex,boolean,None
         #-->Sequences -->Lists,Tuples,sets,Strings,
         #-->Frozensets,mappings(dict)

#Numeric type -->int,float,complex

#int datatype --> quantity,age..
age=7
print(age)
print(type(age)) #type -->returns the datatype of object

print(type(135))

#quantity =03 # it is not allowed
#print(quantity)

#flaot datatype --> temp,salary,price
price =750.45;discount =2.5
print(price,discount)
print(type(price))

#complex --> combination of real and img
i2=5
data = 5+i2
print(data)

data = 5+2j #j is imag represntation
print(data)
print(type(data))

#boolean --> True/False

valid=True
print(type(valid))

error=False
print(type(error))

#TypeCasting --> Converting one type to another type
#python by default follows Implict Type (we need not mention the datatype)

#We will go for Explict Conversion

#Every bulit-in datatype is a built-in function
int,float,complex,bool

#Typecasting -->int--->float,complex,bool

age = 35
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)
e=bool(0)
print(e)

#float Typecasting

age = 35.67
print(type(age))
b=int(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)

#complex Typecasting

age = 2+5j
print(type(age))
#b=int(age)#TypeError
#print(b)
#c=float(age)
#print(c)
d=bool(age)
print(d)
print(type(d))

e = int(float(bool(45)))
print(e)

a=bool(int(float(25)))
print(a)

f=45+2.5+2+3j+False
print(f)
