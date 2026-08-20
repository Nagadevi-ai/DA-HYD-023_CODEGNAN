'''
Function -->Arguments Usage(variable length arguments)
         -->keyword variable length arguments(**kwargs)
         
Exceptional Handling/scope of variables/bulit-in functions

Exception handling --> It is a mechanisim that helps to respond or make the flow of execution in normal way,without this error wil occur and disrup the flow of program
common Exception -->Value Error,TypeError,IndexError,Attributeerror,ZerDivisionError...

 Syntax:

 try:
     #code that will cause the exception
except Exception as e:
     #code will catch the exception
finally:
     #runs irrespective of try/except...
     ...

 
#basic Exception handlling
try:
    #a=10
    #a=float(input("Enter the value:"))
    a=[2,3,4,5]
    print(a)
    #result=20/a
    #print(result)
#except Exception as e:
    #print(e) #it returns the msg of error
except ValueError:
    print(f'Invalid entry enter only integer values')
except ZeroDivisionError:
    print(f'Division by zero is not possible')
except NameError:
    print(f'Check the name of varaible properly')

#Similarly if we want to check other error ->IndexError,AttributeError
try:
    a=[10,20,30]
    a.ppend(24)
    print(a[5])
#except Exception as e:
    #print(e) #returns the message of Error
except IndexError:
    print(f'Check the length of list properly and access elements')
except AttributeError:
    print(f'Dont rush write the name properly')
      
try:
    a=[10,20,30]
    a.append(24)
    print(a[5])
except (IndexError,AttributeError)as e:
    print(e)
    a=list(map(int,input("Enter").split(',')))
    print(a)
 

#BMI --> bmi=(weight)/((height)**2)
#Feet --> 12 inches -->1 inch ->2.54cm
while True:
    try:
        weight=int(input("Enter the weight in kgs:"))
        height=float(input("Enter the height in metres:"))
        #write my logical condition
        if weight > 0 and height >0:
            break #stops the flow of execcution of program #continue #skips the current iteration and proceed for rmg items
        else:
            print("Make sure to enter only correct values:")
    except ValueError as e:
        print(f'Make sure to enter weight as integer only, \
                                   height also as numbers')
bmi=((weight)/(height)**2)
print(bmi)

#Use Exception Hanndling along with jumping statemnt in
#function BMI Task


#scope of variable --> scope is basically the region/area where it is accessible
#Local Scope,Global Scope
#Global Keyword,Enclosing Scope(Nested function non local keyword)

#Local Scope --> variables defined inside the function accessible inside


def display():
    """Usage of Local Scope"""
    name="Codegnan" #Local variable
    print(name)
display()
#print(name) #it raises NameError

#Global Scope(variables) -->Defined outside annd can be accessible anywhere in the script

place="Hyderabad" #global variable
def display():
    """Usage of Local&Global Scope"""
    name="codegnan" #Local variable
    print(name)
    print(f'{name} is in {place}')
display()
print(place)

#Modifying global variable inside the function and accessible outside the function
count=20
def data():
    """Usage of global keyword"""
    global count
    count=count+5
    print(f'value inside function is {count}')
data()
print(f'value outside function is{count}')



count=20
def data():
    """Priority of local vs global variable"""
    count=5
    count=count+5
    print(f'value inside function is {count}')
data()
print(f'value outside function is{count}')

#Enclosing Scope (nonlocal keyword)

def outer():
    """Outer function with local variable"""
    count=5
    def inner():
        """Nested Function"""
        nonlocal count
        count=count+10
        print(f'value outside is{count}')
    inner()
    print(f'Value outside is {count}')
outer()
'''
#Bulit-in functions -->variables Bulitinscope
len=56
print(len+4)

print(len('codegnan')) #TypeError --> Never ever use the bulit in functions as variable 
