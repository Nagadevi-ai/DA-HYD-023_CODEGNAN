'''
Tokens,Datatpes --> control Flow Statements -->if,elif,else,for,while,break,continue..

Procedure Oriented programming

Functions --> A function is a block of code which performs a specific task
its a reusable group of statements whee we define using
def keyword
Advantage --> Code resuability,code maintainabililty,ease of debuggin,avoiding code duplication,modularity...


synatx:
def fname(parameters):           function defn
     """Doc String"""
      statement(s)...            function body
      .........
      return value(s)...
fname(args)                      function call


#To perform sum of given objects
def add(a,b):
    """Sum of objects"""
    c=a+b
    return c
print(add(12,3)) #Addition
print(add('code','gnan')) #concatenation
print(add([12,5],[12,34])) #Merging
c,d=map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34)) # it returns result along with None


name,age,salary="saketh",32,50000  #Global declaration
#usage of return

def details():
    #return name,age,salary
    #return "Codegnan"
    return #it returns None as output
    
print(details())

There are 5 Types of arugments:

-->postional Arguments
-->default arguments
-->keyword arguments
-->variable length arguments(*args)
-->keyword variable length arguments(**kwargs)


#Postional Arguments --> Number of arguments in function defn should match with function call(order has to be maintained)
#print(len(123,234)) this is as per bulit-in  len(obj) will accept one argumenet

def details(name,place):
    """To store the derails"""
    name="codegnan"
    place="hyderabad"
    return name,place
print(details(name,place))
print(details("saketh","codegnan"))
print(details("sai","vizag"))
print(details("vizag","shyam",34)) #raises TypeError as only 2 arguments to be passed
            
def derails(name,place):
    """To store the derails"""
     print(f'name is{name}')
     print(f'place is{place}')
c,d=map(str,input("Enter the values").split()
details(c,d)

     
#Default arguments --> we can make argument as default but not first argument as default

#def grocery(item,price=35):
#def grocery(item="cheese",price=100):
def grocery(item="Burger",price): #non default always follows default 

    """usage of defauult arguments"""
    print(f'the item is {item} and price is {price}')
grocery("Milk",32)
grocery("Bread") #by default we have given price as 35
grocery("Bread",45)
grocery() #as both item and price as default arguments

'''

#keyword arguments --> whenever we want to specify the name of argument
def employee(name,salary,role,place="Codegnan"):
    """Keyword arguments usage"""
    print(f'Employee name is {name},role is {role}  and salary is {salary},place is {place}')
employee("sai",50000,"Admin")
employee(salary=25000,role="frontdesk",name="Asha")
employee("akash",25000,"IT","Cognizant")










