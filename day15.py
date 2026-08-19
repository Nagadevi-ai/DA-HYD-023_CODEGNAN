'''
Function--> Variable length arguments(*args)
        -->keyword variable length arguments(**kwargs)

Variable length arguments -->The number of positional arguments are not limit,we can pass any number of arguments,but we need to use the * represntation,data is stored in tuple

def sample(*args):
     """Simple demo for *args"""
     print(args)
     print(type(args))
sample() #no arguments
sample(1,3,5,6)#any number
sample('codegnan','saketh',23)
details=[24,45,35,65]
sample(details) #passing a collection
sample(*details) #unpacking values
values={6,7,8,9}
sample(*values)


a,b,c=13,4,'da'
#print(a,b,c)
#a,*b,c='python','codegnan',34,56,78,'data'
#print(a,b,c)
#a,b,*c='python','codegnan',34,56,78,'data'
a,b,*c=36,'data'
print(a)
print(b)
print(c)
c.append([23,67,43])
print(c)


#Task -->We wanted to calculate the sum of given objects using function
def add(*a):
    """Sum of given objects"""
    print(a)
    print(type(a))
    #take a output variable
    result=0
    for i in a:
        #if type(i)==int or type(i)==float:
        if type(i) in (int,float,complex):
            result=result+i
    return result
#print(add())
#print(add(12,34,2,4,5))
#print(add(3,4,5,'poll','dear',45,4.5,2+4j))
b=list(map(int,input("Enter the values:").split(',')))
print(add(*b)) #* is used to unpack side by side
print(*b)
for i in b:
    print(i,end=' ') #same as here

#keyword variable length aruguments -->We can pass any number of keyword arguments we use ** representation,data is stored in dictionary

def details(**kwargs):
    """usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details()
details(name='codegnan',place='hyd',batch='da')
batch={'name':'code','place':'vizag'}
details(**batch)
'''

#Now let us include both of them into a function
def sample(*a,**b):
    """usage of both variable length and keyword variable length args"""
    result=0
    for i in a:
        if type(i) in (int,float,complex):
            result=result+i
    print(result)
    for i in b.items():
        print(f'key is {key}')
        print(f'Value is{value}')
sample(2,4,5,'police','codegnan',3.5,name='codegnan',place='hyd',batch='da23')

#sample(name='codegnan',23,ids=23453) #postional args follows keyword args
